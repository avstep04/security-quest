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

## Rules of engagement
I only test systems built for practice or that I own.
