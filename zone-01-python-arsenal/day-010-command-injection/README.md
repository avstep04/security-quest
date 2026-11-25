# Day 10: Command injection
**Zone 1: Python Arsenal** · Completed: Nov 25, 2026

## What it does
| File | Purpose |
|---|---|
| `vulnerable_ping.py` | ⚠️ Deliberately vulnerable ping tool: builds a shell command string from user input |
| `safe_ping.py` | Fixed version: validates input and runs ping with an argument list (no shell) |

## How to run
```
python vulnerable_ping.py    # local learning only
python safe_ping.py
```

## Results

**Exploiting the vulnerable version:** my own machine only
| Input | Result |
|---|---|
| `127.0.0.1` | Normal ping |
| `127.0.0.1 & whoami` | 🚨 Ping, then printed my Windows username: a second command ran |
| `127.0.0.1 & dir` | 🚨 Listed the folder's files |
| `127.0.0.1 & echo PWNED > pwned.txt` | 🚨 Created a file on disk |
| `127.0.0.1 && type pwned.txt` | 🚨 Read the file back |

**Attacking the fixed version**
| Input | Result |
|---|---|
| `127.0.0.1` / `localhost` | ✅ Pinged normally: `['ping', '-n', '1', '127.0.0.1']` |
| `127.0.0.1 & whoami` | ❌ Rejected: not a valid IP address or hostname |
| `-t` (argument injection: "ping forever") | ❌ Rejected |

**Two layers of defense**
| Layer | Stops |
|---|---|
| 1. Input validation (`ipaddress` + strict hostname regex, no leading `-`) | Shell characters and argument injection |
| 2. Argument list, no `shell=True` | Shell interpretation: input is always exactly one argument |

**Bug I caught in my own fix:** I first wrote `"host"` in quotes, so the tool pinged the literal word "host". Printing the exact command it ran (`Running: [...]`) exposed the mistake.

## What I learned
- `shell=True` plus user input = command injection: the user can chain their own commands with `&`, `&&` and `|`.
- An argument list (no shell) is the real fix. Validation is a second layer, not a replacement.
- Argument injection is subtler: input like `-t` contains no shell characters but changes the program's behavior.
- Defense in depth: more than one layer, so one mistake isn't fatal.

## Key notes
### New today
| Term | What it does |
|---|---|
| Command injection | Getting a program to run attacker-supplied system commands |
| Shell / `cmd.exe` | The program that interprets command text (Windows' is `cmd.exe`) |
| Shell metacharacters `&` `&&` `\|` `\|\|` | Symbols that chain or redirect commands |
| Argument injection | Smuggling extra options (like `-t`) into a command |
| Defense in depth | Several independent layers of protection |
| `import subprocess` / `subprocess.run()` | Runs another program from Python |
| `shell=True` | Runs the command through the shell: dangerous with user input |
| `["ping", "-n", "1", host]` | Argument list: each item is passed as one argument, no shell |
| `capture_output=True, text=True` | Captures the program's output as text instead of printing it |
| `result.stdout` / `result.stderr` | The program's normal output / error output |
| `import platform` / `platform.system()` | Detects the operating system ("Windows", "Linux") |
| `import ipaddress` / `ipaddress.ip_address()` | Validates an IP address; raises ValueError if invalid |
| `(?=...)` (regex) | Lookahead: checks a condition, here total length, without consuming text |
| `$` (regex) | End of the text |
| `whoami` | Shows the current user |
| `echo text > file` / `type file` | Write text to a file / show a file (cmd) |
| `ping -n 1` / `-t` | Ping once / ping forever (Windows) |

### Already seen
`input()` (Day 7) · `re` / regex basics (Day 6) · `try` / `except ValueError` (Day 3) · `{x!r}` (Day 7) · `.strip()` (Day 2) · `a if cond else b` (Day 3) · input validation (Day 7) · `timeout` (Day 7)