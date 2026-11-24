# Day 8: Port scanner
**Zone 1: Python Arsenal** · Completed: Nov 24, 2026

## What it does
| File | Purpose |
|---|---|
| `port_scanner.py` | Multi-threaded TCP connect scanner with a target allowlist (localhost only) |

## How to run
```
python port_scanner.py 127.0.0.1 -p 1-10000
python port_scanner.py 127.0.0.1 -p 1-1024 --workers 100 --timeout 0.5
```
Scope: my scanner only runs against machines I own. Remote practice scans use Nmap against `scanme.nmap.org`, which Nmap's makers allow (up to a dozen scans a day).

## Results

**My scanner vs Nmap on localhost:** ports 1–10,000, same connect-scan method
| | My scanner | Nmap `-sT` |
|---|---|---|
| Open ports found | 13 | 13 (same list) |
| Time | 51.2 s | 1.8 s |
| Closed vs filtered | ❌ Couldn't tell apart on Windows | ✅ Reported correctly |

**Threading:** 1,024 ports, 0.5 s timeout
| Threads | Time |
|---|---|
| 10 | 52.6 s |
| 100 | 5.6 s (~9× faster) |

The timings match ports × timeout ÷ threads: on Windows, closed localhost ports time out rather than refuse, so parallelism is what makes the scan usable.

**Version detection:** `nmap -sV scanme.nmap.org` (permitted target)
| Port | State | Service and version |
|---|---|---|
| 22 | open | OpenSSH 6.6.1p1 (Ubuntu), very old, so worth a CVE lookup |
| 80 | open | Apache httpd 2.4.7, outdated |
| 9929 | open | Nping echo |
| 25, 135, 139, 445 | filtered | Likely blocked by my internet provider, not necessarily the target |

**Nmap fingerprinted my own echo server (port 9000):** it read the banner `Welcome to the echo server...` and sent test probes. My server's log recorded the scan.

**What my scanner misses**
| Nmap can... | Mine can't |
|---|---|
| Identify service versions (`-sV`) | Only says "open" |
| Tell closed from filtered reliably | Lumps them together on Windows |
| Scan ~28× faster with optimized timing | Limited by timeouts |
| Guess the operating system, scan UDP, run scripts | TCP only |

**Investigating my own attack surface**
| Port | Owner | Listening on | Finding |
|---|---|---|---|
| 9012 | ArmourySocketServer (ASUS Armoury Crate) | `0.0.0.0` (all interfaces) | Vendor service exposed beyond localhost; protected only by Windows Firewall |

**Scope enforcement:** `python port_scanner.py scanme.nmap.org` → *Refusing to scan: not on my allowlist* ✅

## What I learned
- Ports are open (listening), closed (refused) or filtered (no reply, usually a firewall).
- Threads let a scanner wait on many slow ports at once. Timeouts, not CPU, are the bottleneck.
- Version detection is what turns a port list into a vulnerability list: old versions point to known CVEs.
- Scanning needs permission. I enforced my scope in code with an allowlist.
- Scanning myself showed a real finding: a vendor service listening on all interfaces.

## Key notes
### New today
| Term | What it does |
|---|---|
| Open / closed / filtered | Port states: listening / refused / no reply (firewall) |
| TCP connect scan | Scanning by completing a full connection (Nmap `-sT`) |
| SYN scan | Faster, quieter scan that only half-opens connections (Nmap `-sS`, needs admin) |
| Scope / allowlist | The targets you're permitted to test, enforced in code |
| Nmap | Industry-standard network scanner |
| Npcap | Windows driver Nmap uses to send and capture packets |
| `nmap -sT -p 1-10000` | Connect scan of a port range |
| `nmap -sV` | Version detection: identifies the software on each port |
| Banner / fingerprint | What a service says when you connect; used to identify it |
| CVE | Public ID for a known vulnerability, e.g. CVE-2024-1234 |
| Attack surface | Everything an attacker could reach, such as listening ports |
| `0.0.0.0` vs `127.0.0.1` | Listening on all interfaces vs this machine only |
| Concurrency / threads | Doing many waiting tasks at the same time |
| `from concurrent.futures import ThreadPoolExecutor` | A pool of worker threads |
| `pool.map(fn, items)` | Runs a function on every item using the threads |
| `socket.getservbyport()` | Looks up the usual service name for a port |
| `OSError` | General operating-system error (parent of network errors) |
| `.partition("-")` | Splits text into before, separator and after |
| `[x for x in ... if ...]` | List comprehension with a filter |
| `type=float` / `-p` short flag | Decimal-number argument / one-letter argparse option |
| `{p:<8}` | Left-aligns a value in 8 characters |
| `Get-NetTCPConnection -State Listen` | Lists listening ports (PowerShell) |
| `Get-Process -Id` | Finds the program behind a process ID |
| `Select-Object` | Picks which columns to show (PowerShell) |
| PATH / `$env:Path` | The folders Windows searches for programs |

### Already seen
`socket.create_connection()` (Day 7) · `ConnectionRefusedError` / `socket.timeout` (Day 7) · `argparse` (Day 2) · `time.perf_counter()` (Day 5) · `lambda` (Day 5) · `range()` (Day 3) · `try` / `except` (Day 3) · `with` (Day 2) · `\|` pipe (Day 6) · `Test-NetConnection` (Day 7) · `127.0.0.1` / port (Day 7)