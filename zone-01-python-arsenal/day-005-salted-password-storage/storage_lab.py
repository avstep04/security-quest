import hashlib
import time
from pathlib import Path

import bcrypt
from argon2 import PasswordHasher

WORDLIST = Path(__file__).parent / "common_passwords.txt"

# A "leaked" database that stored plain SHA-256 (no salt)
users = {"alice": "password", "bob": "dragon", "carol": "password"}
leaked_db = {name: hashlib.sha256(pw.encode()).hexdigest() for name, pw in users.items()}

print("== Leaked unsalted database ==")
for name, h in leaked_db.items():
    print(f"{name:6} {h}")

# Dictionary attack: hash every common password once, then look each leaked hash up
start = time.perf_counter()
lookup = {}
with open(WORDLIST, encoding="utf-8", errors="ignore") as f:
    for line in f:
        guess = line.strip()
        #store the SHA-256 hex digest of `guess` as the key, and `guess` as the value
        lookup[hashlib.sha256(guess.encode()).hexdigest()] = guess
elapsed = time.perf_counter() - start

print(f"\n== Cracked in {elapsed:.3f} seconds ==")
for name, h in leaked_db.items():
    print(f"{name:6} -> {lookup.get(h, 'not cracked')}")

# How long does ONE hash take with each algorithm?
pw = b"password"
ph = PasswordHasher()

def time_it(label, fn, runs):
    start = time.perf_counter()
    for _ in range(runs):
        fn()
    per_hash = (time.perf_counter() - start) / runs
    print(f"{label:8} {per_hash * 1000:10.4f} ms per hash  ~{1 / per_hash:12,.0f} guesses/sec")

print("\n== Cost per hash ==")
time_it("SHA-256", lambda: hashlib.sha256(pw).hexdigest(), 100000)
time_it("bcrypt", lambda: bcrypt.hashpw(pw, bcrypt.gensalt()), 5)
time_it("argon2", lambda: ph.hash(pw), 5)

# Salt: same password, two different hashes
print("\n== Salted: same password, different hashes ==")
print(ph.hash("password"))
print(ph.hash("password"))