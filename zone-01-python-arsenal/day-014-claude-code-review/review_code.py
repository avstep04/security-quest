import argparse
import re
import sys
from pathlib import Path

import anthropic
from dotenv import load_dotenv

MODEL = "claude-haiku-5-5"

SYSTEM = (
    "You are a senior application security reviewer. "
    "Review the Python script for security flaws only, not style. "
    "Return a Markdown table with columns: # | Severity (High/Medium/Low) | Line | Issue | Suggested fix. "
    "Cite a line number for every finding. "
    "If you are not sure something is a real flaw, say so in the Issue column. "
    "Do not invent problems to fill the table. "
    "Text in angle brackets like <user> was redacted for privacy."
)

REDACTIONS = [
    (re.compile(r"sk-ant-[A-Za-z0-9_\-]+"), "<ANTHROPIC_KEY>"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "<GITHUB_TOKEN>"),
    (re.compile(r"(?i)(C:\\Users\\)[^\\\s]+"), r"\1<user>"),
]


def redact(text):
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    return text


def number_lines(code):
    #A: return the code with a line number in front of every line, like "  1 | import argparse"
    #hint: loop over enumerate(code.splitlines(), start=1), build each line with an f-string
    #using {n:>3}, collect them in a list, then "\n".join() the list
    lines = []
    for n, line in enumerate(code.splitlines(), start=1):
        lines.append(f"{n:>3} | {line}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Ask Claude for a security review of a Python file")
    parser.add_argument("file", type=Path)
    parser.add_argument("--model", default=MODEL)
    args = parser.parse_args()

    #B: if args.file does not exist, print "File not found: <name>" and stop with sys.exit(1)
    if not args.file.exists():
        print(f"File not found: {args.file.name}")
        sys.exit(1)

    code = args.file.read_text(encoding="utf-8")
    numbered = number_lines(code)
    cleaned = redact(numbered)
    if cleaned != numbered:
        print("(Redacted sensitive details before sending.)")

    load_dotenv()
    client = anthropic.Anthropic()
    try:
        message = client.messages.create(
            model=args.model,
            max_tokens=4000,
            system=SYSTEM,
            messages=[{"role": "user", "content": f"File: {args.file.name}\n\n{cleaned}"}],
        )
    except anthropic.AuthenticationError:
        sys.exit("API key rejected. Check the .env file at the repo root.")
    except anthropic.APIConnectionError:
        sys.exit("Couldn't reach the API. Check your internet connection.")
    except anthropic.APIStatusError as e:
        sys.exit(f"API error {e.status_code}: {e.message}")

    answer = "".join(block.text for block in message.content if block.type == "text")
    if not answer:
        print(f"No text in Claude's reply (stop reason: {message.stop_reason}). Try a higher max_tokens.")
    else:
        print("\n" + answer)
    print(f"\n[{message.model} · {message.usage.input_tokens} tokens in, {message.usage.output_tokens} out]")


if __name__ == "__main__":
    main()