# Day 12: First CTF flags
**Zone 1: Python Arsenal** · Completed: Nov 25, 2026

## What it does
Five solved Capture the Flag challenges from **CyLab Security Academy** (Carnegie Mellon's free platform, formerly picoCTF), each with a method write-up. Flags are redacted.

## Results

**Challenges solved:** 5 of 5, General Skills
| # | Challenge | Skill | Key commands | Write-up |
|---|---|---|---|---|
| 1 | Obedient Cat | Downloading and reading files | `wget`, `ls`, `cat` | [obedient-cat](writeups/obedient-cat.md) |
| 2 | Wave a flag | Making programs runnable, reading help | `chmod +x`, `./warm -h` | [wave-a-flag](writeups/wave-a-flag.md) |
| 3 | Python Wrangling | Running a script with arguments; real decryption | `python3 ende.py -d` | [python-wrangling](writeups/python-wrangling.md) |
| 4 | Nice netcat | Connecting to a remote service; decoding ASCII | `nc`, `\|`, Python `chr()` | [nice-netcat](writeups/nice-netcat.md) |
| 5 | strings it | Extracting text from a binary | `strings`, `\|`, `grep` | [strings-it](writeups/strings-it.md) |

**How this week's skills showed up**
| Earlier day | Used again in |
|---|---|
| Day 3: encoding vs encryption | Nice netcat (ASCII encoding) vs Python Wrangling (real encryption) |
| Day 6: pipes and pattern searching | `strings \| grep`, `nc \| python3` |
| Day 7: TCP connections | `nc` to a remote port |
| Day 8: PATH | `./warm` vs `warm: command not found` |

## What I learned
- CTFs are a safe, legal way to practice: every challenge teaches one tool or idea.
- Run unfamiliar programs with no arguments or `-h` first: they usually explain themselves.
- Pipes (`|`) chain small tools into one solution.
- Write-ups document the method, never the flag. The method is what's valuable.

## Key notes
### New today
| Term | What it does |
|---|---|
| CTF (Capture the Flag) | Security challenges where you find hidden "flags" |
| Flag | The secret answer string, here `academy{...}` |
| CyLab Security Academy | Carnegie Mellon's free CTF practice platform (formerly picoCTF) |
| Webshell | A Linux terminal in the browser |
| Write-up | A step-by-step explanation of how a challenge was solved |
| `wget <url>` | Downloads a file (Linux) |
| `ls` | Lists files in the current folder (Linux) |
| `cat <file>` | Prints a file's contents (Linux) |
| `chmod +x <file>` | Makes a file executable |
| `./program` | Runs a program in the current folder |
| `-h` | Common "help" option for command-line programs |
| Usage message | A tool's summary of its options, e.g. `ende.py (-e/-d) [file]` |
| `man <command>` | Opens a command's manual (`q` to quit) |
| `nc <host> <port>` | Netcat: connects to a remote TCP port |
| ASCII | The standard numbering of characters (97 = `a`) |
| `chr(n)` | Python: number → character |
| `python3 -c "..."` | Runs a short Python snippet from the command line |
| `sys.stdin.read()` | Reads everything piped into a Python program |
| `strings <file>` | Extracts readable text from a binary file |
| `grep "text"` | Keeps only lines containing the text |
| `mkdir` | Creates a folder |
| `mv` / `rm` | Moves / permanently deletes a file |
| `~` | Your home folder |
| `file.1` | What `wget` names a duplicate download |

### Already seen
PATH (Day 8) · `\|` pipe (Day 6) · `cd` (Day 1) · `int()` (Day 9) · `"".join()` (Day 9) · `.split()` (Day 9) · encoding vs encryption (Day 3) · `KeyboardInterrupt` / Ctrl+C (Day 7) · TCP / ports (Day 7)