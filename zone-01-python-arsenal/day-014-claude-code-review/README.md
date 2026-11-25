# Day 14: Claude code review
**Zone 1: Python Arsenal** · Completed: Nov 25, 2026

## What it does
| File | Purpose |
|---|---|
| `review_code.py` | Sends a Python file (line-numbered and redacted) to Claude for a security review and prints the findings table |
| `findings.md` | My verification of every finding: how I checked it, my verdict and my own severity rating |

Target reviewed: [`password_store.py`](../day-005-salted-password-storage/password_store.py) from Day 5.

## How to run
```
python review_code.py ..\day-005-salted-password-storage\password_store.py
```
Uses the `.env` at the repo root (one key for every day).

## Results

**Two review runs, same input**
| | Run 1 | Run 2 |
|---|---|---|
| Findings | 6 | 10 |
| Medium findings | Throttling, login enumeration | File permissions, throttling |
| Line numbers correct | ✅ All | ✅ All |
| Tokens (in / out) | 1084 / 2216 | 1084 / 2447 |

**After verifying every finding by hand** ([full table](findings.md))
| Verdict | Count |
|---|---|
| ✅ Real | 7 |
| ⚠️ Partly true | 2 |
| ❌ False positive | 1 (Unix file permissions on a Windows machine) |

**What I caught that Claude didn't**
| Claude said | I tested | Result |
|---|---|---|
| `users.json` readable by other users (`umask 0644`) | `icacls users.json` | Only SYSTEM, Administrators and my account: **false positive on Windows** |
| Use `fcntl` for file locking | `python -c "import fcntl"` | `ModuleNotFoundError`: **the fix would crash on Windows** |
| Argon2 defaults are current | Printed the parameters | `3 65536 4` matches RFC 9106: ✅ **correct** |

Takeaway: AI review is a fast first pass, but it's not repeatable, it assumes an environment, and its severity ratings are guesses. Verification is the job.

## What I learned
- The same prompt can produce different findings and severities, so run AI review more than once and combine the results.
- Every finding needs evidence: read the cited line, run a test, or check the docs.
- Severity depends on the threat model. The same flaw is Low in a single-user CLI and High behind a web service.
- My Day 5 fix (identical error messages) wasn't enough: skipping the password prompt for unknown users still reveals which accounts exist.
- Fix suggestions need testing too. A fix for one OS can crash on another.

## Key notes
### New today
| Term | What it does |
|---|---|
| AI-assisted code review | Using a model to find possible flaws, which a human then verifies |
| Verdict: Real / False positive / Partly true | My judgment of each finding after checking it |
| Severity rating | How serious a flaw is (High / Medium / Low / Info) |
| Threat model | Who could attack this, how, and what they could reach |
| Nondeterminism | Same input, different output between runs |
| `str.splitlines()` | Splits text into a list of lines |
| `enumerate(items, start=1)` | Loops with a counter starting at 1 |
| `type=Path` (argparse) | Turns an argument straight into a `Path` object |
| `sys.exit("message")` | Prints a message and stops the program with an error code |
| `python -c "<code>"` | Runs one line of Python without a file |
| `help(function)` | Prints a function's built-in documentation |
| `ModuleNotFoundError` | The module isn't installed or doesn't exist on this OS |
| `fcntl` | Unix-only file-locking module (not on Windows) |
| `umask` / `0o600` / `0644` | Unix default permissions / owner-only / everyone can read |
| `icacls <file>` | Shows a file's Windows access list |
| ACL / `(I)(F)` | Access control list / inherited full control |
| Atomic write / `os.replace()` | Write a temp file, then swap it in so the file is never half-written |
| Race condition | Two operations overlapping and overwriting each other |
| `InvalidHashError` | Argon2 error for a malformed or tampered hash |
| `check_needs_rehash()` | Says whether a hash uses outdated parameters |
| `time_cost` / `memory_cost` / `parallelism` | Argon2 settings: passes, memory (KiB), threads |
| RFC 9106 | The Argon2 standard, with recommended parameters |

### Already seen
Username enumeration (Day 5) · Argon2id (Day 5) · `PasswordHasher()` / `.hash()` / `.verify()` (Day 5) · `VerifyMismatchError` (Day 5) · `Path.exists()` / `.read_text()` / `.write_text()` (Day 5) · `getpass.getpass()` (Day 4) · False positive / negative (Day 6) · `{x:>4}` (Day 9) · `anthropic.Anthropic()` / `client.messages.create()` (Day 13) · system prompt (Day 13) · redaction / `pattern.sub()` (Day 13) · content blocks (Day 13) · `load_dotenv()` (Day 11) · `.join()` (Day 9) · `try:` / `except` (Day 3)