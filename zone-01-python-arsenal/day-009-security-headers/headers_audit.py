import argparse

import requests

TIMEOUT = 10


def check_hsts(value):
    if not value:
        return 0, "Missing: browsers may connect over plain HTTP"
    try:
        max_age = int(value.lower().split("max-age=")[1].split(";")[0])
    except (IndexError, ValueError):
        return 5, "Present but max-age unreadable"
    if max_age >= 31536000:
        return 20, f"Good: max-age {max_age} (1 year or more)"
    return 10, f"Weak: max-age {max_age} is under 1 year"


def check_csp(value):
    if not value:
        return 0, "Missing: no defense-in-depth against XSS"
    if "unsafe-inline" in value or "unsafe-eval" in value:
        return 15, "Present but allows 'unsafe-inline'/'unsafe-eval'"
    return 25, "Good: present without unsafe keywords"


def check_frame(xfo, csp):
    if csp and "frame-ancestors" in csp:
        return 15, "Good: CSP frame-ancestors set"
    if xfo and xfo.upper() in ("DENY", "SAMEORIGIN"):
        return 15, f"Good: X-Frame-Options {xfo.upper()}"
    return 0, "Missing: page can be framed (clickjacking)"


def check_nosniff(value):
    #A: if value exists and value.lower() == "nosniff":
    #           return 15, "Good: nosniff"
    #         otherwise return 0, "Missing: browser may guess (sniff) content types"
    if value and value.lower() == "nosniff":
        return 15, "Good: nosniff"
    return 0, "Missing: browser may guess (sniff) content types"


def check_referrer(value):
    good = {"no-referrer", "same-origin", "strict-origin", "strict-origin-when-cross-origin"}
    if value and value.lower().split(",")[-1].strip() in good:
        return 10, f"Good: {value}"
    if value:
        return 5, f"Present but leaky: {value}"
    return 0, "Missing: browser default applies"


def check_permissions(value):
    if value:
        return 10, "Good: present"
    return 0, "Missing: no limits on camera, microphone, location, etc."


def check_leaks(headers):
    #B: build a list called `leaks` of "Name: value" strings for the headers
    #         "Server" and "X-Powered-By", but only when the value contains a digit
    #         (a version number like nginx/1.25.3). Hint: any(ch.isdigit() for ch in text)
    #         If leaks: return 0, "Leaks software details: " + "; ".join(leaks)
    #         Else:     return 5, "Good: no software version numbers exposed"
    leaks = [
        f"{name}: {value}"
        for name in ["Server", "X-Powered-By"]
        if (value := headers.get(name)) and any(ch.isdigit() for ch in value)
    ]
    if leaks:
        return 0, "Leaks software details: " + "; ".join(leaks)
    return 5, "Good: no software version numbers exposed"


def grade(score):
    for cutoff, letter in [(90, "A"), (75, "B"), (60, "C"), (40, "D")]:
        if score >= cutoff:
            return letter
    return "F"


def audit(url):
    resp = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": "security-quest-headers-audit/1.0"})
    h = resp.headers  # case-insensitive dictionary
    print(f"URL:    {resp.url}  (status {resp.status_code})")
    if resp.history:
        print(f"Redirects: {' -> '.join(r.url for r in resp.history)} -> {resp.url}")

    csp = h.get("Content-Security-Policy")
    checks = [
        ("Strict-Transport-Security", check_hsts(h.get("Strict-Transport-Security"))),
        ("Content-Security-Policy", check_csp(csp)),
        ("Clickjacking protection", check_frame(h.get("X-Frame-Options"), csp)),
        ("X-Content-Type-Options", check_nosniff(h.get("X-Content-Type-Options"))),
        ("Referrer-Policy", check_referrer(h.get("Referrer-Policy"))),
        ("Permissions-Policy", check_permissions(h.get("Permissions-Policy"))),
        ("Information leakage", check_leaks(h)),
    ]

    total = 0
    print(f"\n{'HEADER':28} {'PTS':>4}  NOTE")
    for name, (points, note) in checks:
        total += points
        print(f"{name:28} {points:>4}  {note}")

    print(f"\nScore: {total}/100  Grade: {grade(total)}")


def main():
    parser = argparse.ArgumentParser(description="Grade a website's HTTP security headers")
    parser.add_argument("url", help="full URL, e.g. https://example.com")
    args = parser.parse_args()
    try:
        audit(args.url)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
 

if __name__ == "__main__":
    main()