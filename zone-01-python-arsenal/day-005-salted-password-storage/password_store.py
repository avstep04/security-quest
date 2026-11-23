import argparse
import getpass
import json
from pathlib import Path

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

DB_FILE = Path(__file__).parent / "users.json"
ph = PasswordHasher()  # Argon2id with safe defaults; makes a new random salt per hash


def load_users():
    if not DB_FILE.exists():
        return {}
    return json.loads(DB_FILE.read_text())


def save_users(users):
    DB_FILE.write_text(json.dumps(users, indent=2))


def register(username):
    users = load_users()
    if username in users:
        print(f"User '{username}' already exists.")
        return
    pw = getpass.getpass("Choose a password: ")
    #A: hash `pw` with ph.hash() and store it in users[username]
    #(the salt is generated and stored inside the hash string automatically)
    users[username] = ph.hash(pw)
    save_users(users)
    print(f"Registered '{username}'. Stored hash: {users[username]}")


def login(username):
    users = load_users()
    if username not in users:
        print("Login failed.")
        return
    pw = getpass.getpass("Password: ")
    #B: call ph.verify(users[username], pw) inside try:
    #on VerifyMismatchError, print "Login failed." and return
    try:
        ph.verify(users[username], pw)
    except VerifyMismatchError:
        print("Login failed.")
        return
    print(f"Welcome back, {username}!")


def main():
    parser = argparse.ArgumentParser(description="Store and verify passwords with Argon2")
    parser.add_argument("action", choices=["register", "login"])
    parser.add_argument("username")
    args = parser.parse_args()
    if args.action == "register":
        register(args.username)
    else:
        login(args.username)


if __name__ == "__main__":
    main()