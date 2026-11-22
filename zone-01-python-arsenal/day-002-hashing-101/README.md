# Day 2: Hashing 101
**Zone 1: Python Arsenal** · Completed: Nov 22, 2026

## What it does
| File | Purpose |
|---|---|
| `hashing_lab.py` | Hashes a message with MD5, SHA-1 and SHA-256, and shows the avalanche effect |
| `file_hasher.py` | Checks a downloaded file against its published SHA-256 fingerprint |

## How to run
```
python hashing_lab.py
python file_hasher.py <file> <expected_sha256>
```

## Results

**Digest lengths**
| Algorithm | Length (hex chars) |
|---|---|
| MD5 | 32 |
| SHA-1 | 40 |
| SHA-256 | 64 |

**Avalanche effect:** SHA-256 of two nearly identical inputs
| Input | Characters matching |
|---|---|
| `"hello"` vs `"Hello"` | 3 of 64 (about random chance) |

One capital letter scrambles the whole hash.

**SHAttered collision:** two different PDFs
| Algorithm | shattered-1.pdf | shattered-2.pdf | Same? |
|---|---|---|---|
| SHA-1 | `38762cf7...cbb7f0a` | `38762cf7...cbb7f0a` | ❌ Yes, collision |
| SHA-256 | `2bb787a7...e6970d0` | `d4488775...94ba5ff` | ✅ No, told apart |

SHA-1 can't tell the files apart; SHA-256 can.

**file_hasher.py test:** both files checked against shattered-1's SHA-256
| File | Result |
|---|---|
| shattered-1.pdf | ✅ MATCH, file is authentic |
| shattered-2.pdf | ❌ MISMATCH, swapped file caught |

My tool catches the swap that SHA-1 would have missed.

## What I learned
- A one-character change scrambles the whole hash (avalanche effect).
- SHA-1 and MD5 are broken for integrity: two different files can share a hash. Use SHA-256 or stronger.
- Reading files in chunks lets a tool verify files of any size without running out of memory.
- Security values should be compared with `hmac.compare_digest()`, not `==`.

## Key notes
### New today
| Term | What it does |
|---|---|
| `import hashlib` | Loads Python's built-in hashing library |
| `hashlib.md5()` / `.sha1()` / `.sha256()` | Create a hash object for that algorithm |
| `.encode()` | Turns text into bytes; hashes only work on bytes |
| `.hexdigest()` | Returns the finished hash as readable hex text |
| `len()` | Counts the characters in a string |
| `print()` | Shows values in the terminal |
| `zip(a, b)` | Pairs up items from two sequences side by side |
| `sum(x == y for ...)` | Counts how many pairs are equal (True counts as 1) |
| `python file.py` | Runs a Python file from the terminal |
| `dir` | Lists files in a folder (PowerShell) |
| `Get-FileHash -Algorithm` | Windows' built-in file hasher; the flag picks SHA1, SHA256 and so on |
| `$HOME` | Shortcut for your user folder (C:\Users\Andrew) |
| `import argparse` | Loads Python's library for command-line arguments |
| `argparse.ArgumentParser()` | Creates the parser that reads what you type after the script name |
| `.add_argument()` | Defines one input the script expects, such as `file` |
| `.parse_args()` | Reads the typed inputs into `args.file` and `args.expected` |
| `import hmac` | Loads Python's library of message-authentication tools |
| `hmac.compare_digest(a, b)` | Compares two secrets in constant time, so timing leaks nothing |
| `def name():` | Defines a reusable function |
| `return` | Sends a value back out of a function |
| `with open(path, "rb") as f:` | Opens a file for reading in binary mode and closes it automatically |
| `f.read(n)` | Reads the next n bytes of a file; returns empty bytes at the end |
| `.update(chunk)` | Feeds more data into an existing hash |
| `while True:` / `break` | Repeats a loop until `break` stops it |
| `if not x:` | True when x is empty, None or zero |
| `if / else` | Runs one block or the other depending on a condition |
| `.strip()` | Removes spaces and newlines from both ends of text |
| `.lower()` | Converts text to lowercase |
| `f"...{x}..."` | f-string: puts a variable's value inside text |
| `if __name__ == "__main__":` | Runs `main()` only when the file is run directly, not imported |
| `CHUNK_SIZE = 65536` | A constant; capital letters mean "don't change this" |

### Already seen
- None yet