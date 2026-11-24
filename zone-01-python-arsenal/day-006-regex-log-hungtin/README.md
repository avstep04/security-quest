# Day 6: Regex log hunting
**Zone 1: Python Arsenal** · Completed: Nov 24, 2026

## What it does
| File | Purpose |
|---|---|
| `log_parser.py` | Uses regex to count failed logins per IP, list usernames tried, and show every successful login |
| `brute_detect.py` | Flags IPs with too many failures inside a sliding time window, and warns if a flagged IP then logged in |
| `sample_auth.log` | 43 lines of SSH activity from a made-up server, `web01` (documentation-only IP ranges) |

## How to run
```
python log_parser.py
python brute_detect.py sample_auth.log
python brute_detect.py sample_auth.log --window 120 --threshold 5
```

## Results: incident summary for web01, Nov 23

**Detection results**
| Source IP | Attack style | 10-min window | 120-min window | Verdict |
|---|---|---|---|---|
| 203.0.113.45 | Brute force on `root` | 🚨 12 failures | 🚨 12 failures | **Compromised**: root login at 08:14:07 |
| 198.51.100.23 | Username spraying (7 fake accounts) | 🚨 8 failures | 🚨 8 failures | Attack, no access |
| 203.0.113.99 | Low-and-slow on `root` | ✅ missed (peak 1) | 🚨 7 failures | Attack, no access (false negative at 10 min) |
| 192.0.2.77 | 4 tries for `maria`, then success | ✅ ok | ✅ ok | Innocent: user forgot password |

**Timeline of the compromise**
| Time | Event |
|---|---|
| 08:12:06 | First failed root password from 203.0.113.45 |
| 08:12:06 – 08:13:58 | 12 failures, about one every 10 seconds (automated) |
| 08:14:07 | **Accepted password for root** from 203.0.113.45 |

**Recommended response**
| Action | Why |
|---|---|
| Block 203.0.113.45, 198.51.100.23 and 203.0.113.99 | Stop active attackers |
| Reset root's password; review everything root did after 08:14 | Attacker had full control |
| Disable root SSH login and require SSH keys | Removes this attack path (Day 29) |
| Add automatic blocking after repeated failures (fail2ban) | Stops brute force in progress (Day 29) |

## What I learned
- Regex turns messy log lines into structured data: named groups pull out the user, IP and time.
- Total counts aren't enough. A sliding time window separates fast attacks from normal mistakes.
- Thresholds trade off: too strict causes false positives, too loose causes false negatives. Low-and-slow attackers exploit the gap.
- The most important alert isn't the failures. It's a **success right after** many failures.

## Key notes
### New today
| Term | What it does |
|---|---|
| `auth.log` | Linux log recording logins and authentication events |
| `sshd` | The SSH server process that handles remote logins |
| Syslog timestamp | `Nov 23 08:12:06` format; leaves out the year |
| Username spraying | Trying many usernames, often with common passwords |
| Low-and-slow attack | Spreading attempts out over time to stay under alert thresholds |
| Sliding window | Checking every time span of a fixed length for a burst of events |
| False positive / false negative | An alert on harmless activity / a missed real attack |
| Detection threshold | The count at which an alert fires |
| Documentation IP ranges | `192.0.2.x`, `198.51.100.x`, `203.0.113.x`: reserved for examples, never real |
| Regex (regular expression) | A pattern language for matching text |
| regex101.com | Website for building and testing regex, with explanations |
| `import re` / `re.compile()` | Python's regex library / prepare a pattern for reuse |
| `r"..."` | Raw string: backslashes stay as typed (needed for regex) |
| `pattern.search(line)` | Finds the first match in a line, or returns None |
| `m.group("name")` | Gets the text captured by a named group |
| `\d` `\S` `\w` `+` `?` `{3}` `^` | Digit, non-space, letter, one-or-more, optional, exactly 3, start of line |
| `(?P<name>...)` / `(?:...)` | Named capture group / group that captures nothing |
| `from collections import Counter` | Dictionary that counts things automatically |
| `.most_common()` | Lists a Counter's items from highest count to lowest |
| `defaultdict(list)` | Dictionary that creates an empty list for any new key |
| `.append()` | Adds an item to the end of a list |
| `(a, b)` | Tuple: a fixed group of values |
| `continue` | Skips to the next loop iteration |
| `while condition:` | Repeats while the condition is true |
| `sorted()` / `max()` | Returns a sorted copy / the largest value |
| `datetime.strptime(text, format)` | Turns text into a date and time using format codes |
| `%Y %b %d %H:%M:%S` | Format codes: year, month name, day, hour:minute:second |
| `timedelta(minutes=10)` | A length of time, for date math |
| `{ts:%H:%M:%S}` | Formats a datetime inside an f-string |
| `type=int, default=5` (argparse) | Optional argument converted to a number, with a default |
| `.gitignore` `!file` | Exception rule: track this file even if another rule ignores it |
| `Move-Item` | Moves a file (PowerShell) |
| `Get-Content \| Measure-Object -Line` | Counts the lines in a file (PowerShell) |
| `\|` (pipe) | Sends one command's output into the next command |

### Already seen
`argparse` (Day 2) · `def` / `return` (Day 2) · `with open(...)` (Day 2) · f-strings (Day 2) · `if not` (Day 2) · `.gitignore` (Day 1) · `for` loops / `in` (Day 3) · `Path(__file__).parent` (Day 4) · `from X import Y` (Day 4) · brute force attack (Day 4) · dictionaries / `.get()` / `.items()` (Day 5) · `{x:15}` padding (Day 5)