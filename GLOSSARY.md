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
| Salt | Random per-user value mixed in before hashing | Day 5 |
| Rainbow tables | Precomputed hash lookups (defeated by salts) | Day 5 |
| Slow / memory-hard hashing | Deliberately expensive hashing to slow attackers | Day 5 |
| Argon2id | Recommended password-hashing algorithm | Day 5 |
| bcrypt | Older, acceptable password-hashing algorithm | Day 5 |
| Username enumeration | Finding valid usernames from error differences | Day 5 |
| `python -m pip install` | Installs an outside Python library | Day 5 |
| `PasswordHasher()` / `.hash()` / `.verify()` | Argon2 hashing and checking | Day 5 |
| `VerifyMismatchError` | Argon2's wrong-password error | Day 5 |
| `bcrypt.hashpw()` / `gensalt()` | bcrypt hashing and salt | Day 5 |
| `b"text"` | Bytes value | Day 5 |
| `time.perf_counter()` | Precise timer | Day 5 |
| `lambda` | One-line unnamed function | Day 5 |
| `for _ in range(n):` | Repeat n times | Day 5 |
| Dictionary `{}` / `d[key]` | Key → value storage | Day 5 |
| `d.get()` / `d.items()` | Safe lookup / loop over pairs | Day 5 |
| `{k: v for ...}` | Dictionary comprehension | Day 5 |
| `json.loads()` / `json.dumps()` | Read and write JSON data | Day 5 |
| `Path.exists()` / `.read_text()` / `.write_text()` | One-call file checks and I/O | Day 5 |
| `choices=[...]` | Restricts argparse values | Day 5 |
| `{x:6}` / `{x:,.0f}` | Padding / thousands separators | Day 5 |
| `Copy-Item` | Copies a file (PowerShell) | Day 5 |
| `Get-Location` | Shows the current folder (PowerShell) | Day 5 |
| `..\` | The folder above this one | Day 5 |
| `auth.log` | Linux login and authentication log | Day 6 |
| `sshd` | SSH server process | Day 6 |
| Username spraying | Trying many usernames | Day 6 |
| Low-and-slow attack | Spreading attempts out to avoid thresholds | Day 6 |
| Sliding window | Checking every time span of a fixed length | Day 6 |
| False positive / negative | Alert on harmless activity / missed attack | Day 6 |
| Detection threshold | Count at which an alert fires | Day 6 |
| Documentation IP ranges | Reserved example IPs (192.0.2.x, etc.) | Day 6 |
| Regex | Pattern language for matching text | Day 6 |
| regex101.com | Regex builder and tester | Day 6 |
| `re.compile()` / `.search()` / `.group()` | Prepare, find and extract regex matches | Day 6 |
| `r"..."` | Raw string | Day 6 |
| `\d \S \w + ? {n} ^` | Core regex symbols | Day 6 |
| `(?P<name>...)` / `(?:...)` | Named group / non-capturing group | Day 6 |
| `Counter` / `.most_common()` | Automatic counting, ranked | Day 6 |
| `defaultdict(list)` | Dict that auto-creates lists | Day 6 |
| `.append()` | Adds to a list | Day 6 |
| `(a, b)` | Tuple | Day 6 |
| `continue` | Skip to the next loop | Day 6 |
| `while condition:` | Loop while true | Day 6 |
| `sorted()` / `max()` | Sorted copy / largest value | Day 6 |
| `datetime.strptime()` | Text to date and time | Day 6 |
| `timedelta()` | Length of time | Day 6 |
| `{ts:%H:%M:%S}` | Format a datetime | Day 6 |
| `type=int, default=` | Typed optional argparse argument | Day 6 |
| `.gitignore` `!file` | Exception to an ignore rule | Day 6 |
| `Move-Item` | Moves a file (PowerShell) | Day 6 |
| `Measure-Object -Line` | Counts lines (PowerShell) | Day 6 |
| `\|` (pipe) | Sends output to the next command | Day 6 |
| IP address | Identifies a computer on a network | Day 7 |
| Port | Numbered door identifying a program | Day 7 |
| `127.0.0.1` / localhost | This computer | Day 7 |
| TCP | Reliable, ordered connection | Day 7 |
| Socket | One end of a network connection | Day 7 |
| Client / server | Connects / waits for connections | Day 7 |
| Denial of service | Making a service unavailable | Day 7 |
| Input validation | Checking incoming data before trusting it | Day 7 |
| `socket.socket(AF_INET, SOCK_STREAM)` | Creates a TCP socket | Day 7 |
| `.bind()` / `.listen()` / `.accept()` | Server setup and accepting clients | Day 7 |
| `.settimeout()` / `socket.timeout` | Time limits and the timeout error | Day 7 |
| `.recv()` / `.sendall()` | Receive and send bytes | Day 7 |
| `socket.create_connection()` | Client connect shortcut | Day 7 |
| `ConnectionRefusedError` etc. | Network error types | Day 7 |
| `KeyboardInterrupt` | Raised by Ctrl+C | Day 7 |
| `datetime.now()` | Current date and time | Day 7 |
| `input()` | Reads typed input | Day 7 |
| `action="store_true"` | Argparse on/off flag | Day 7 |
| `.startswith()` | Checks how text begins | Day 7 |
| `data[:20]` | Slicing | Day 7 |
| `{x!r}` | Raw form in an f-string | Day 7 |
| `\n` | Newline | Day 7 |
| `Test-NetConnection -Port` | Checks if a port answers (PowerShell) | Day 7 |
| Split terminal (Ctrl+Shift+5) | Side-by-side terminals in VS Code | Day 7 |