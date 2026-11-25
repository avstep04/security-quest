# Day 13: Meet Claude as a pair
**Zone 1: Python Arsenal** · Completed: Nov 25, 2026

## What it does
| File | Purpose |
|---|---|
| `hello_claude.py` | My first Claude API call: asks one question, prints the answer and token usage |
| `ask_claude.py` | Error explainer: paste a Python error, it **redacts API keys and personal paths**, then asks Claude to explain the cause and fix |
| `.env.example` | Committed template showing the setting the scripts need (no real key) |
| `.env` | My real API key, **never committed** (ignored by `.gitignore`) |

## How to run
```
python -m pip install anthropic python-dotenv
copy .env.example .env              # then paste in a real key from platform.claude.com
python hello_claude.py
python ask_claude.py                # paste an error, then press Enter on an empty line
python ask_claude.py --file error.txt
```

## Results

**First API call**
| Check | Result |
|---|---|
| `python hello_claude.py` | ✅ Two-sentence answer on hashing vs encryption, plus token usage |
| Key handling | ✅ Loaded from `.env` and never printed or hard-coded |

**ask_claude tests**
| Test | Result |
|---|---|
| Error with a personal Windows path | ✅ Path redacted to `C:\Users\<user>`, correct explanation (163 tokens in, 470 out) |
| Error containing a fake API key (`sk-ant-api03-FAKE...`) | ✅ Key redacted to `<ANTHROPIC_KEY>` **before sending**, 401 explained correctly (123 in, 808 out) |
| Error with nothing sensitive | ✅ Sent unchanged, no redaction message |

**Bugs found and fixed**
| Problem | Cause | Fix |
|---|---|---|
| `AttributeError: 'ThinkingBlock' object has no attribute 'text'` | Replies can contain thinking blocks as well as text blocks | Kept only blocks where `block.type == "text"` |
| Empty answer, no error | Thinking used the whole 500-token budget | Raised max_tokens to 2000 and print the stop_reason when no text comes back |
| Claude blamed the `<user>` placeholder as my mistake | Redaction removed context without telling the model | Added a system-prompt line explaining redacted placeholders |

**Checking the AI's answers**
| What Claude said | Reality | What I did |
|---|---|---|
| Get a key at console.anthropic.com | The Console now lives at platform.claude.com | Used the current site |
| Suggested model `claude-sonnet-4-5` | That's an older model name | Used `claude-haiku-5-5` |
| Set the key with `export` / `$env:` | Works, but puts the key in shell history | Kept `.env` + `load_dotenv()` |
| 808 tokens out for a ~200-word answer | Hidden thinking is billed as output tokens | `max_tokens` is the real cost cap, not "keep it under 200 words" |

**Credential incident (real, handled)**
I accidentally pasted my API key into a chat while asking for help. I treated it as exposed:
1. **Revoked** the key right away in the Console
2. **Rotated** it: created a new key with a **30-day expiry** and stored it only in `.env`
3. Set a **monthly spend limit** so a leaked key can't run up a large bill

Lesson: nobody needs your key to help you. Share the error, not the credential.

## What I learned
- A paid Claude subscription doesn't include API access. The API is billed separately through the Console with prepaid credits.
- An API reply is a list of content blocks, not one string. Code has to handle every block type it might get.
- Data minimization: before sending anything to an AI service, strip what it doesn't need (keys, usernames, paths). The tool redacts first, then sends.
- Redaction has a trade-off. Removing context can mislead the model unless you tell it what was removed.
- AI answers need checking. Claude gave me an outdated site name and model name, so I verified both against current docs.
- `max_tokens` controls both answer length and cost, and thinking counts against it.
- Read a traceback from the bottom up: the last line names the error.

## Key notes
### New today
| Term | What it does |
|---|---|
| API | A way for one program to use a service over the internet |
| LLM / generative AI | An AI model that generates text from a prompt |
| Claude Console | Website for API keys, billing, usage and limits (platform.claude.com) |
| Key expiry / rotation / revoke | Keys that stop working on a date / replacing a key / disabling one immediately |
| Spend limit | A monthly cap on API costs |
| Prepaid credits | Money loaded in advance that API calls draw from |
| `import anthropic` / `anthropic.Anthropic()` | Loads the Claude SDK / creates a client (reads `ANTHROPIC_API_KEY` automatically) |
| `client.messages.create()` | Sends a request to Claude and returns the reply |
| `model=` / `max_tokens=` | Which model answers / the most tokens it may produce |
| `messages=[{"role": "user", "content": ...}]` | The conversation sent to Claude; each message has a role |
| `system=` (system prompt) | Instructions that set Claude's role and answer format |
| Tokens / `message.usage` | Chunks of text that are billed / how many went in and out |
| Content blocks / `block.type` | The pieces of a reply (`"thinking"` or `"text"`) |
| Thinking tokens | Hidden reasoning that counts as billed output |
| `message.stop_reason` | Why Claude stopped (e.g. `max_tokens` means it ran out of budget) |
| `claude-haiku-5-5` | Fast, inexpensive Claude model |
| `AuthenticationError` / `BadRequestError` | Bad or missing key / request rejected (e.g. no credits) |
| `APIConnectionError` / `APIStatusError` | Couldn't reach the API / any other error status |
| HTTP 401 vs 400 | Not authenticated vs request rejected |
| Data minimization | Send only the data a service actually needs |
| Redaction | Replacing sensitive values with placeholders like `<user>` |
| `pattern.sub(replacement, text)` | Regex find-and-replace |
| `(?i)` / `\1` | Case-insensitive matching / reuse capture group 1 in the replacement |
| `for line in sys.stdin:` | Reads typed or pasted input one line at a time |
| Reading a traceback | Start at the last line (the error), then work upward |

### Already seen
Secret / API key (Day 11) · `.env` / `load_dotenv()` (Day 11) · `git check-ignore -v` (Day 11) · masking (Day 11) · `import argparse` (Day 2) · `try:` / `except` (Day 3) · `re.compile()` (Day 6) · `.join()` (Day 9) · list comprehension with `if` (Day 8) · `with open` (Day 2) · `python -m pip install` (Day 5) · HTTP status codes (Day 9) · `sys.stdin` (Day 12) · f-strings (Day 2)