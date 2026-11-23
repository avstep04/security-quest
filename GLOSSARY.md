# Glossary
Every tool, command and function I've learned in Security Quest, with the day I first used it.

| Term | What it does | First seen |
|---|---|---|
| `git commit` | Saves a snapshot of your changes with a message | Day 1 |
| `git push` (Push origin) | Uploads your commits to GitHub | Day 1 |
| `.gitignore` | Lists files Git should never track, like secrets and junk | Day 1 |
| `wsl --install` | Installs Linux (Ubuntu) inside Windows | Day 1 |
| `cd ~` | Moves to your Linux home folder | Day 1 |
| `sudo` | Runs a Linux command as administrator | Day 1 |
| `apt update / upgrade` | Refreshes and installs Linux software updates | Day 1 |
| `--version` | Shows which version of a tool is installed | Day 1 |
| Workspace Trust | VS Code setting that allows code in a folder to run | Day 1 |
| `import hashlib` | Loads Python's built-in hashing library | Day 2 |
| `hashlib.md5/sha1/sha256()` | Create a hash for that algorithm | Day 2 |
| `.encode()` | Turns text into bytes | Day 2 |
| `.hexdigest()` | Returns a hash as readable hex text | Day 2 |
| `len()` | Counts characters or items | Day 2 |
| `print()` | Shows values in the terminal | Day 2 |
| `zip(a, b)` | Pairs items from two sequences | Day 2 |
| `sum(x == y for ...)` | Counts matching pairs | Day 2 |
| `python file.py` | Runs a Python file | Day 2 |
| `dir` | Lists files (PowerShell) | Day 2 |
| `Get-FileHash` | Windows' built-in file hasher | Day 2 |
| `$HOME` | Your user folder | Day 2 |
| `import argparse` | Loads Python's library for command-line arguments | Day 2 |
| `argparse.ArgumentParser()` | Creates the parser that reads what you type after the script name | Day 2 |
| `.add_argument()` | Defines one input the script expects | Day 2 |
| `.parse_args()` | Reads the typed inputs into `args` | Day 2 |
| `import hmac` | Loads Python's library of message-authentication tools | Day 2 |
| `hmac.compare_digest(a, b)` | Compares two secrets in constant time | Day 2 |
| `def name():` | Defines a reusable function | Day 2 |
| `return` | Sends a value back out of a function | Day 2 |
| `with open(path, "rb") as f:` | Opens a file in binary mode and closes it automatically | Day 2 |
| `f.read(n)` | Reads the next n bytes of a file | Day 2 |
| `.update(chunk)` | Feeds more data into an existing hash | Day 2 |
| `while True:` / `break` | Repeats a loop until `break` stops it | Day 2 |
| `if not x:` | True when x is empty, None or zero | Day 2 |
| `if / else` | Runs one block or the other depending on a condition | Day 2 |
| `.strip()` | Removes spaces and newlines from both ends of text | Day 2 |
| `.lower()` | Converts text to lowercase | Day 2 |
| `f"...{x}..."` | f-string: puts a variable's value inside text | Day 2 |
| `if __name__ == "__main__":` | Runs `main()` only when the file is run directly | Day 2 |
| `CHUNK_SIZE = 65536` | A constant; capital letters mean "don't change this" | Day 2 |
| Base64 | Encoding into letters, digits, + and / (often ends in =) | Day 3 |
| Hex encoding | Each byte written as two characters, 0–9 and a–f | Day 3 |
| URL encoding | Special characters replaced with % codes | Day 3 |
| ROT13 | Letters shifted 13 places; reversible | Day 3 |
| CyberChef | GCHQ's browser tool for decoding with recipes | Day 3 |
| Magic (CyberChef) | Guesses an encoding automatically | Day 3 |
| `import base64` | Loads Python's Base64 library | Day 3 |
| `base64.b64encode()` / `b64decode()` | Encode to and decode from Base64 | Day 3 |
| `.decode()` | Turns bytes back into text | Day 3 |
| `bytes.fromhex()` | Turns a hex string into bytes | Day 3 |
| `codecs.encode(s, "rot13")` | Applies ROT13 | Day 3 |
| `urllib.parse.unquote()` | Decodes % codes in URLs | Day 3 |
| `binascii.Error` | Error raised by invalid Base64 or hex | Day 3 |
| `try:` / `except` | Catches errors instead of crashing | Day 3 |
| `ValueError` / `UnicodeDecodeError` | Bad-input and not-valid-text errors | Day 3 |
| `None` | Python's "no value" | Day 3 |
| `pass` | Placeholder that does nothing | Day 3 |
| `.isprintable()` | True if all characters are visible | Day 3 |
| `and` | True only if both sides are true | Day 3 |
| `in` / `not in` | Checks whether text appears inside a string | Day 3 |
| `for x in [...]:` | Loops over each item in a list | Day 3 |
| `range(a, b)` | Counts from a up to b−1 | Day 3 |
| `a if cond else b` | One-line if/else | Day 3 |
| `x, y = f()` | Unpacks two returned values | Day 3 |
| `--help` | Shows a script's usage text | Day 3 |
| Entropy | Password unpredictability in bits | Day 4 |
| Brute force attack | Trying every possible combination | Day 4 |
| Dictionary attack | Trying the most common real passwords first | Day 4 |
| Blocklist screening | Rejecting known-common passwords | Day 4 |
| NIST SP 800-63B-4 | US password and authentication standard (2025) | Day 4 |
| SecLists | Open-source wordlists for security testing | Day 4 |
| `Invoke-WebRequest -OutFile` | Downloads a file (PowerShell) | Day 4 |
| Python REPL (`>>>`) | Interactive Python prompt | Day 4 |
| `math.log2()` | Bits needed to represent a number | Day 4 |
| `string.ascii_lowercase` etc. | Ready-made character sets | Day 4 |
| `getpass.getpass()` | Hidden password input | Day 4 |
| `from X import Y` | Imports one thing from a library | Day 4 |
| `Path(__file__).parent` | Folder the script lives in | Day 4 |
| `{x for x in ...}` | Set comprehension | Day 4 |
| `any(...)` | True if at least one item matches | Day 4 |
| `or` | True if either side is true | Day 4 |
| `elif` | Checks another condition | Day 4 |
| `+=` | Adds to a variable | Day 4 |
| `{x:.1f}` | Formats to 1 decimal place | Day 4 |