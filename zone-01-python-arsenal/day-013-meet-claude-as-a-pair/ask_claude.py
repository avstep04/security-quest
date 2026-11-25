import argparse
import re
import sys

import anthropic
from dotenv import load_dotenv

MODEL = "claude-haiku-5-5"
SYSTEM = (
    "You are a patient Python and security tutor for a beginner. "
    "Given an error message, explain in plain English: (1) what the error means, "
    "(2) the most likely cause, (3) how to fix it, with a short code example if useful. "
    "Keep it under 200 words. "
    "Text in angle brackets like <user> or <ANTHROPIC_KEY> was redacted for privacy; "
    "treat it as a stand-in for the real value, not as a mistake."
)

# Data minimization: scrub things that should never leave my machine
REDACTIONS = [
    (re.compile(r"sk-ant-[A-Za-z0-9_\-]+"), "<ANTHROPIC_KEY>"),
    (re.compile(r"ghp_[A-Za-z0-9]{36}"), "<GITHUB_TOKEN>"),
    (re.compile(r"(?i)(C:\\Users\\)[^\\\s]+"), r"\1<user>"),
]


def redact(text):
    #for each (pattern, replacement) in REDACTIONS,
    #       set text = pattern.sub(replacement, text). Then return text.
    for pattern, replacement in REDACTIONS:
        text = pattern.sub(replacement, text)
    return text


def read_error(path):
    if path:
        with open(path, encoding="utf-8") as f:
            return f.read()
    print("Paste the error, then press Enter on an empty line:")
    lines = []
    for line in sys.stdin:
        if not line.strip():
            break
        lines.append(line)
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Ask Claude to explain an error message")
    parser.add_argument("--file", help="read the error from a file instead of pasting")
    parser.add_argument("--model", default=MODEL)
    args = parser.parse_args()

    load_dotenv()
    error_text = read_error(args.file).strip()
    if not error_text:
        print("No error text given.")
        return

    safe_text = redact(error_text)
    if safe_text != error_text:
        print("(Redacted sensitive details before sending.)")

    client = anthropic.Anthropic()
    try:
        message = client.messages.create(
            model=args.model,
            max_tokens=2000,
            system=SYSTEM,
            messages=[{"role": "user", "content": f"Explain this error:\n\n{safe_text}"}],
        )
    except anthropic.AuthenticationError:
        print("Authentication failed: check ANTHROPIC_API_KEY in your .env file.")
        return
    except anthropic.APIConnectionError:
        print("Could not reach the Claude API. Check your internet connection.")
        return
    except anthropic.APIStatusError as e:
        print(f"API error {e.status_code}: {e.message}")
        return

    answer = "".join(block.text for block in message.content if block.type == "text")
    print("\n" + answer)
    print(f"\n[{message.model} · {message.usage.input_tokens} tokens in, {message.usage.output_tokens} out]")


if __name__ == "__main__":
    main()