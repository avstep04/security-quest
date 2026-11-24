# Security Quest

A 200-day hands-on cybersecurity journey: Python, Linux, networking,
crypto and smart contracts, web and cloud security (AWS + Azure),
detection engineering, and AI agent security built with Claude.

**Started:** November 22, 2026
**Goal:** Build and secure AI-powered security tools, one commit a day.

## Progress
| Day | Project | Skills developed |
|-----|---------|------------------|
| 1 | Secure lab setup | Set up a Linux security lab (WSL2 Ubuntu) and Git version control. Used a Python .gitignore to keep secrets and build files out of the repo, kept the repo off cloud-synced storage to protect its integrity, and gave an AI code reviewer access to only what it needs. |
| 2 | [Hashing 101](zone-01-python-arsenal/day-002-hashing-101/) | Hashed data with MD5, SHA-1 and SHA-256 in Python and showed the avalanche effect. Reproduced the SHAttered SHA-1 collision to prove why MD5 and SHA-1 fail for integrity checks. Built a command-line tool that verifies downloads against published SHA-256 checksums, using chunked file reading and constant-time comparison. |
| 3 | [Encoding is not encryption](zone-01-python-arsenal/day-003-encoding-is-not-encryption/) | Distinguished encoding, encryption and hashing. Decoded Base64, hex, URL-encoded and ROT13 data in CyberChef, including a two-layer obfuscated payload, and reproduced each in Python. Built a command-line decoder that detects encodings automatically and peels nested layers, the same triage analysts use on obfuscated attacker commands. |
| 4 | [Password strength](zone-01-python-arsenal/day-004-password-strength/) | Calculated password entropy and showed why length beats complexity. Built a password checker that screens against the 10,000 most common passwords and enforces NIST SP 800-63B-4's 15-character minimum, reading input securely with getpass. Identified the entropy formula's blind spot: predictable human patterns like "Summer2024!" score high but get guessed early. |
| 5 | [Salted password storage](zone-01-python-arsenal/day-005-salted-password-storage/) | Cracked a leaked unsalted SHA-256 password database in 0.011 seconds with a dictionary attack, then measured why slow hashes matter: Argon2id was ~77,000× and bcrypt ~400,000× slower to compute than SHA-256. Built a register/login system storing salted Argon2id hashes, with identical failure messages to prevent username enumeration, and kept user data out of Git. |
| 6 | [Regex log hunting](zone-01-python-arsenal/day-006-regex-log-hunting/) | Parsed SSH authentication logs with regex and built a sliding-window brute-force detector. Investigated a simulated server: found a successful brute-force compromise of root, a username-spraying attack, and a low-and-slow attacker that only a longer window caught, while correctly clearing a user who forgot their password. Wrote it up as an incident report with a timeline and response plan. |
| 7 | [Sockets](zone-01-python-arsenal/day-007-sockets/) | Built a TCP echo server and client with Python sockets, then attacked my own server with malformed bytes, oversized messages and idle connections. Hardened it with input validation, size limits and timeouts so it survived every test without crashing, and confirmed open and closed ports with Test-NetConnection: the groundwork for a port scanner. |
| 8 | [Port scanner](zone-01-python-arsenal/day-008-port-scanner/) | Built a multi-threaded TCP port scanner with an enforced target allowlist (threading cut scan time ~9×), then benchmarked it against Nmap: same 13 open ports, but Nmap was ~28× faster and added version detection. Used Nmap -sV on scanme.nmap.org to identify outdated OpenSSH and Apache versions, and traced an unexpected service listening on all interfaces on my own PC to its owning process. |

## Rules of engagement
I only test systems built for practice or that I own.
