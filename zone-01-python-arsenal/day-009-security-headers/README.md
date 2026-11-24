# Day 9: Security headers
**Zone 1: Python Arsenal** · Completed: Nov 24, 2026

## What it does
| File | Purpose |
|---|---|
| `headers_audit.py` | Fetches a site's HTTP response headers and grades 7 security checks out of 100 |

## How to run
```
python -m pip install requests
python headers_audit.py https://github.com
```
Passive check: one normal page request, the same as visiting in a browser.

## Results

**Header grades**
| Site | Status | Score | Grade | Key findings |
|---|---|---|---|---|
| github.com | 200 | 80 | B | Strong HSTS, CSP with frame-ancestors, nosniff; CSP allows `unsafe-inline`; no Permissions-Policy |
| google.com | 200 | 20 | F | Only X-Frame-Options; may rely on protections my tool doesn't check (e.g. report-only CSP) |
| example.com | 200 | 5 | F | Documentation placeholder with no security headers |
| unc.edu | **403** | 15 | F* | *Blocked by the site's firewall, so this graded the block page, not the real site |
**Validating my tool against MDN HTTP Observatory**
| Site | My tool | MDN Observatory | Agree? |
|---|---|---|---|
| github.com | B (80/100) | A+ (115/100, 11/12 tests passed) | ❌ Mine was stricter |
| example.com | F (5/100) | F (10/100, 7/12 tests passed) | ✅ Yes |

Observatory awards bonus points beyond 100 and checks each CSP directive separately; mine docks points for `unsafe-inline` anywhere and caps at 100. Same verdict on the weak site, harsher on the strong one.

**What each header defends against**
| Header | Protects against |
|---|---|
| Strict-Transport-Security | Downgrade to unencrypted HTTP |
| Content-Security-Policy | Cross-site scripting (XSS) |
| X-Frame-Options / `frame-ancestors` | Clickjacking |
| X-Content-Type-Options: nosniff | Content-type confusion |
| Referrer-Policy | Leaking page addresses to other sites |
| Permissions-Policy | Unwanted camera, mic and location access |
| No version numbers in Server / X-Powered-By | Giving attackers versions to look up (see Day 8) |

**Limitations I found in my own tool**
| Limitation | Improvement |
|---|---|
| Graded a 403 block page as if it were the site | Added a warning for status codes 400 and above |
| Penalizes `unsafe-inline` anywhere in the CSP | Check `script-src` separately from `style-src` |
| Only checks headers | Professional tools (MDN HTTP Observatory) also check cookies, redirects and more |

## What I learned
- Security headers are cheap, server-side instructions that switch on browser protections. Many sites skip them.
- CSP `frame-ancestors` has replaced X-Frame-Options, and X-XSS-Protection is deprecated (OWASP).
- A header grade is one signal, not a verdict: Google scores F, yet uses other protections.
- Always check the status code: firewalls can block scanners and serve a different page.

## Key notes
### New today
| Term | What it does |
|---|---|
| HTTP headers | Instructions a server sends before the page content |
| HSTS (Strict-Transport-Security) | Forces HTTPS for a set time (`max-age` in seconds) |
| CSP (Content-Security-Policy) | Lists which scripts and resources a page may load |
| XSS (cross-site scripting) | Attack that injects malicious scripts into a website |
| Clickjacking | Hiding a real page inside another to trick clicks |
| `frame-ancestors` | CSP rule controlling who may embed the page |
| X-Content-Type-Options: nosniff | Stops browsers guessing file types |
| Referrer-Policy | Controls what page address is shared with other sites |
| Permissions-Policy | Limits camera, mic, location and other features |
| Information leakage | Revealing internal details, like software versions |
| HTTP status codes (200, 403) | Server's result: 200 OK, 403 forbidden |
| WAF (web application firewall) | Filters web traffic; may block scripts |
| User-Agent | Header that tells servers which browser or tool is asking |
| Redirect | Server sending you to another URL (e.g. http → https) |
| OWASP | Non-profit publishing web security standards and guides |
| MDN HTTP Observatory | Mozilla's free website header scanner |
| DevTools Network tab (F12) | Browser panel showing every request and its headers |
| `curl.exe -I <url>` | Shows only a site's response headers (PowerShell) |
| `import requests` | Popular library for making web requests |
| `requests.get(url, timeout=, headers=)` | Fetches a page with a time limit and custom headers |
| `resp.status_code` / `.headers` / `.url` / `.history` | Response status, headers, final URL and redirects |
| `requests.exceptions.RequestException` | Catches any request failure |
| `IndexError` | Error for asking for a list position that doesn't exist |
| `.split()` | Breaks text into a list at a separator |
| `"; ".join(list)` | Glues a list into one string with a separator |
| `.isdigit()` / `.upper()` / `int()` | Is it a digit / uppercase / convert to whole number |
| `for name, (points, note) in checks:` | Unpacks nested pairs while looping |
| `{x:>4}` | Right-aligns a value in 4 characters |
| `{"a", "b"}` | A set written directly (fast membership checks) |

### Already seen
`argparse` (Day 2) · f-strings (Day 2) · `def` / `return` (Day 2) · `try` / `except` / `ValueError` (Day 3) · `any()` (Day 4) · `python -m pip install` (Day 5) · `.get()` (Day 5) · `{x:28}` padding (Day 5) · list comprehensions (Day 8) · `.lower()` / `in` (Days 2–3) · version detection (Day 8)