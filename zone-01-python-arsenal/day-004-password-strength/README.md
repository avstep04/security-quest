#entropy = length × log₂(pool size)

# Day 4: Password strength
**Zone 1: Python Arsenal** · Completed: Nov 23, 2026

## What it does
| File | Purpose |
|---|---|
| `pw_check.py` | Scores a password's entropy, checks it against the 10,000 most common passwords, and applies NIST's 15-character minimum |
| `common_passwords.txt` | Top-10k common passwords from [SecLists](https://github.com/danielmiessler/SecLists) (MIT license) |

## How to run
```
python pw_check.py
```
Type the password at the hidden prompt. Input is not shown or saved.

## Results

**Length vs complexity:** entropy in bits
| Password style | Calculation | Entropy |
|---|---|---|
| 8 characters, all types | 8 × log₂(95) | ~53 bits |
| 16 characters, lowercase only | 16 × log₂(26) | ~75 bits |

The longer, simpler password is stronger. Length beats complexity.

**Sample passwords tested**
| Password | Entropy | Result |
|---|---|---|
| `password` | 37.6 bits (WEAK) | ❌ FAIL, on common list |
| `qwerty123` | 46.5 bits (MODERATE) | ❌ FAIL, on common list |
| `P@ssw0rd` | 52.6 bits (MODERATE) | ⚠️ WARN, under 15 characters |
| `Summer2024!` | 72.3 bits (STRONG) | ⚠️ WARN, under 15 characters |
| `correct horse battery staple` | 164.7 bits (VERY STRONG) | ✅ PASS |

`Summer2024!` scores STRONG but is one of the first patterns attackers try. The entropy formula assumes random characters, and people aren't random.

## What I learned
- Each bit of entropy doubles the guesses needed, and length adds bits faster than character types do.
- Entropy only measures brute force. Dictionary attacks beat predictable passwords, so a blocklist check is essential.
- NIST SP 800-63B-4: 15-character minimum when the password is the only factor, blocklist screening, no composition rules, no routine expiration.
- Passwords should never be passed as command-line arguments, because they end up in shell history. Use `getpass`.

## Key notes
### New today
| Term | What it does |
|---|---|
| Entropy | How unpredictable a password is, in bits; each bit doubles the guesses needed |
| Brute force attack | Trying every possible combination |
| Dictionary attack | Trying the most common real passwords first |
| Blocklist screening | Rejecting passwords that appear on lists of known-common ones |
| NIST SP 800-63B-4 | The US government's password and authentication standard (2025) |
| SecLists | Open-source collection of wordlists used by security testers |
| `Invoke-WebRequest -OutFile` | Downloads a file from a URL (PowerShell) |
| Python REPL (`>>>`) | Interactive prompt for trying Python line by line; open with `python`, leave with `exit()` |
| `import math` / `math.log2()` | Math library; `log2` gives the bits needed to represent a number |
| `import string` | Library of ready-made character sets |
| `string.ascii_lowercase` / `ascii_uppercase` / `digits` / `punctuation` | The a–z, A–Z, 0–9 and symbol character sets |
| `import getpass` / `getpass.getpass()` | Asks for input without showing it on screen |
| `from X import Y` | Imports just one thing (Y) from a library (X) |
| `from pathlib import Path` | Modern way to work with file paths |
| `Path(__file__).parent / "file.txt"` | Builds a path to a file next to the script, wherever it's run from |
| `__file__` | The path of the current script |
| `open(..., encoding="utf-8", errors="ignore")` | Opens text safely, skipping characters it can't read |
| `{x for x in f if ...}` | Set comprehension: builds a set (fast lookup, no duplicates) in one line |
| `any(... for c in pw)` | True if at least one item matches |
| `or` | True if either side is true |
| `elif` | "Else if": checks another condition when the first was false |
| `+=` | Adds to a variable, e.g. `size += 26` |
| `<` | "Less than" comparison |
| `{bits:.1f}` | Formats a number with 1 decimal place inside an f-string |

### Already seen
`def` / `return` (Day 2) · `print()` (Day 2) · `len()` (Day 2) · `with open(...)` (Day 2) · `.strip()` / `.lower()` (Day 2) · `if / else` (Day 2) · f-strings (Day 2) · `if __name__ == "__main__":` (Day 2) · constants in CAPS (Day 2) · `dir` (Day 2) · `in` (Day 3) · `for` loops (Day 3) · `pass` (Day 3) · `a if cond else b` (Day 3)