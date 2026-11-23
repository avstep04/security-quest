import getpass
import math
import string
from pathlib import Path

from torch import add

WORDLIST = Path(__file__).parent / "common_passwords.txt"
MIN_LENGTH = 15  # NIST minimum when a password is the only factor


def load_wordlist(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return {line.strip().lower() for line in f if line.strip()}


def pool_size(pw):
    size = 0
    #A: add 26 for uppercase (string.ascii_uppercase),
    #10 for digits (string.digits),
    #33 for symbols or spaces (c in string.punctuation or c == " ")

    if any(c in string.ascii_lowercase for c in pw):
        size += 26
    if any(c in string.ascii_uppercase for c in pw):
        size += 26
    if any(c in string.digits for c in pw):
        size += 10
    if any(c in string.punctuation or c == " " for c in pw):
        size += 33
    return size


def entropy_bits(pw):
    size = pool_size(pw)
    return 0.0 if size == 0 else len(pw) * math.log2(size)


def rate(bits):
    #B: return "WEAK" under 40, "MODERATE" under 60,
    #"STRONG" under 80, otherwise "VERY STRONG"
    if bits < 40:
        return "WEAK"
    elif bits < 60:
        return "MODERATE"
    elif bits < 80:
        return "STRONG"
    else:
        return "VERY STRONG"


def check(pw, common):
    bits = entropy_bits(pw)
    print(f"Length:  {len(pw)}")
    print(f"Entropy: {bits:.1f} bits ({rate(bits)})")
    #C: if pw.lower() is in `common`, print a FAIL (cracked instantly).
    #elif it's shorter than MIN_LENGTH, print a WARN with the NIST minimum.
    #else print a PASS.
    if pw.lower() in common:
        print("FAIL: password is in the common password list (cracked instantly)")
    elif len(pw) < MIN_LENGTH:
        print(f"WARN: password is shorter than the NIST minimum of {MIN_LENGTH} characters")
    else:
        print("PASS: password is not in the common password list and meets the NIST minimum length")

def main():
    common = load_wordlist(WORDLIST)
    pw = getpass.getpass("Password to check (hidden): ")
    check(pw, common)


if __name__ == "__main__":
    main()