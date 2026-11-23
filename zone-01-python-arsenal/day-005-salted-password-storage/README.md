# Day 5: Salted password storage
**Zone 1: Python Arsenal** · Completed: Nov 23, 2026

## What it does
| File | Purpose |
|---|---|
| `storage_lab.py` | Cracks a leaked unsalted SHA-256 database with a wordlist, then times SHA-256, bcrypt and Argon2 |
| `password_store.py` | Register/login system that stores passwords as salted Argon2id hashes |
| `common_passwords.txt` | Top-10k common passwords from [SecLists](https://github.com/danielmiessler/SecLists) (MIT license) |

## How to run
```
python -m pip install argon2-cffi bcrypt
python storage_lab.py
python password_store.py register <username>
python password_store.py login <username>
```
`users.json` (the local user database) is listed in `.gitignore` and never committed.

## Results

**Cracking an unsalted database:** plain SHA-256, no salt
| User | Stored hash | Cracked as |
|---|---|---|
| alice | `5e884898...1542d8` | password |
| bob | `a9c43be9...f0e74c` | dragon |
| carol | `5e884898...1542d8` | password |

All three were cracked in **0.011 seconds** using the 10k wordlist. Identical hashes revealed that alice and carol share a password.

**Cost per hash:** measured on my PC
| Algorithm | Time per hash | Guesses per second | vs SHA-256 |
|---|---|---|---|
| SHA-256 | 0.0004 ms | ~2,547,816 | baseline |
| Argon2id | 30.3 ms | ~33 | ~77,000× slower |
| bcrypt | 154.1 ms | ~6 | ~400,000× slower |

A 30 ms delay is unnoticeable at login, but it makes cracking each guess enormously more expensive.

**Salting:** the same password hashed twice with Argon2
| Run | Salt | Hash |
|---|---|---|
| 1 | `cZtcmAVYTiXCY6inA6wynQ` | `KQNncHAA...6coo` |
| 2 | `T77FMEc3DV5YBQ3wbLX4mg` | `l3H+zr5u...Fbk` |

Different salts mean different hashes, so attackers can't crack everyone at once.

**Login system tests**
| Test | Result |
|---|---|
| Correct password | ✅ Welcome back, andy! |
| Wrong password | ❌ Login failed. |
| Unknown user | ❌ Login failed. (same message, so usernames aren't revealed) |
| Duplicate registration | ⛔ User 'andy' already exists. |

## What I learned
- Fast hashes like SHA-256 are the wrong tool for passwords. Speed helps attackers.
- A salt makes every user's hash unique, which defeats precomputed tables and "crack once, apply to all."
- Argon2id and bcrypt are slow on purpose; Argon2 is also memory-hard, which makes GPU cracking expensive.
- An Argon2 hash string carries its own algorithm, cost settings and salt, so no separate salt column is needed.
- Identical error messages for "unknown user" and "wrong password" prevent username enumeration.

## Key notes
### New today
| Term | What it does |
|---|---|
| Salt | Random value mixed into each password before hashing, unique per user |
| Precomputed (rainbow) tables | Pre-made hash-to-password lookups that salts make useless |
| Slow / memory-hard hashing | Algorithms deliberately expensive to compute, to slow attackers |
| Argon2id | Recommended password-hashing algorithm for new systems |
| bcrypt | Older, still-acceptable password-hashing algorithm |
| Username enumeration | Discovering valid usernames from different error messages |
| `python -m pip install` | Installs an outside Python library |
| argon2-cffi | Python library for Argon2 hashing |
| `PasswordHasher()` | Creates an Argon2 hasher with safe default settings |
| `ph.hash(pw)` | Hashes a password with a fresh random salt |
| `ph.verify(hash, pw)` | Checks a password against a stored hash; raises an error if wrong |
| `VerifyMismatchError` | The error Argon2 raises for a wrong password |
| `from argon2.exceptions import ...` | Imports an error type so it can be caught |
| `bcrypt.hashpw()` / `bcrypt.gensalt()` | Hash a password with bcrypt and make a salt |
| `b"text"` | A bytes value written directly |
| `import time` / `time.perf_counter()` | Precise timer for measuring how long code takes |
| `lambda: ...` | A tiny unnamed function written in one line |
| `for _ in range(n):` | Repeat n times; `_` means "I don't need the counter" |
| Dictionary `{}` | Stores key → value pairs for fast lookup |
| `d[key] = value` | Adds or updates a dictionary entry |
| `d.get(key, default)` | Looks up a key, or returns the default if it's missing |
| `d.items()` | Gives every (key, value) pair, for looping |
| `{k: v for ...}` | Dictionary comprehension: builds a dict in one line |
| `import json` | Library for reading and writing JSON data files |
| `json.loads()` / `json.dumps(indent=2)` | Turn JSON text into Python data and back (indented) |
| `Path.exists()` / `.read_text()` / `.write_text()` | Check, read and write a file in one call |
| `choices=[...]` (argparse) | Restricts an argument to allowed values |
| `{x:6}` / `{x:,.0f}` | Pad text to