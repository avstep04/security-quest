# Day 7: Sockets
**Zone 1: Python Arsenal** · Completed: Nov 24, 2026

## What it does
| File | Purpose |
|---|---|
| `echo_server.py` | TCP echo server on localhost:9000, hardened against idle, oversized and malformed input |
| `echo_client.py` | Client for chatting with the server, plus `--raw` and `--flood` modes that attack it |

## How to run
Two terminals (split with Ctrl+Shift+5):
```
python echo_server.py          # terminal 1
python echo_client.py          # terminal 2
python echo_client.py --raw
python echo_client.py --flood
```

## Results

**Attacking my own server**
| Test | Input | Server response | Server survived? |
|---|---|---|---|
| Normal | `hello`, `quit` | `ECHO: hello`, `Bye!` | ✅ |
| Malformed | Invalid bytes `\xff\xfe\xfd` | `ERROR: not valid UTF-8 text` (client kept) | ✅ |
| Oversized | 5,000 bytes (limit 1,024) | `ERROR: message too long` (client dropped) | ✅ |
| Idle | Silent for 15+ seconds | `Timed out. Bye.` | ✅ |

**Port check with `Test-NetConnection 127.0.0.1 -Port 9000`**
| Server state | TcpTestSucceeded |
|---|---|
| Running | ✅ True (port open) |
| Stopped | ❌ False (port closed) |

A port only answers while a program is listening on it. A port scanner relies on exactly that.

## What I learned
- An IP address picks the computer and a port picks the program. `127.0.0.1` is always this machine.
- Servers can't trust anything that arrives on a port: every input needs a limit, a timeout and validation.
- Each kind of bad input gets a different response: an honest mistake gets an error, abuse gets disconnected.
- Binding to `127.0.0.1` instead of `0.0.0.0` keeps a test server unreachable from the network.

## Key notes
### New today
| Term | What it does |
|---|---|
| IP address | Identifies a computer on a network |
| Port | Numbered "door" (0–65535) that identifies a program on a computer |
| `127.0.0.1` / localhost | Always means "this computer" |
| TCP | Reliable, ordered connection between two programs |
| Socket | One end of a network connection, as a program sees it |
| Client / server | The side that connects / the side that waits for connections |
| Denial of service | Making a service unavailable, e.g. by tying it up or crashing it |
| Input validation | Checking incoming data's size and format before trusting it |
| `import socket` | Python's networking library |
| `socket.socket(AF_INET, SOCK_STREAM)` | Creates an IPv4 TCP socket |
| `.setsockopt(SO_REUSEADDR, 1)` | Lets the server restart on the same port straight away |
| `.bind((host, port))` | Claims an address and port for the server |
| `.listen()` | Starts waiting for connections |
| `.accept()` | Takes the next incoming connection; returns a new socket and the client's address |
| `.settimeout(seconds)` | Gives up waiting after that many seconds |
| `socket.timeout` | Error raised when a timeout runs out |
| `.recv(n)` | Receives up to n bytes; empty bytes means the other side closed |
| `.sendall(data)` | Sends all the bytes |
| `socket.create_connection((host, port), timeout=5)` | Client shortcut that connects in one call |
| `ConnectionRefusedError` / `ConnectionResetError` / `ConnectionAbortedError` / `BrokenPipeError` | Network errors: nobody listening / connection cut / aborted / writing to a closed connection |
| `KeyboardInterrupt` | Error raised by Ctrl+C, caught to stop cleanly |
| `datetime.now()` | The current date and time |
| `input("> ")` | Reads a line the user types |
| `action="store_true"` (argparse) | An on/off flag like `--raw` |
| `.startswith()` | True if text begins with the given text |
| `data[:20]` | Slicing: the first 20 items or bytes |
| `{x!r}` | Shows a value's raw form in an f-string (reveals hidden bytes) |
| `\n` | Newline character |
| `Test-NetConnection -Port` | Checks whether a TCP port answers (PowerShell) |
| Split terminal (Ctrl+Shift+5) | Two terminals side by side in VS Code |

### Already seen
`.encode()` (Day 2) · `.decode()` (Day 3) · `b"text"` (Day 5) · `try` / `except` (Day 3) · `while True` / `break` (Day 2) · `continue` (Day 6) · `if not` (Day 2) · `len()` (Day 2) · `.strip()` / `.lower()` (Day 2) · `argparse` / `type=int, default=` (Days 2, 6) · tuples (Day 6) · datetime formatting (Day 6) · `with` (Day 2)