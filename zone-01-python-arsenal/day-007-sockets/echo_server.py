import socket
from datetime import datetime

HOST = "127.0.0.1"   # localhost only: other machines can't reach it
PORT = 9000
MAX_BYTES = 1024     # reject anything bigger
IDLE_TIMEOUT = 15    # seconds a client may sit silent


def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}")


def handle(conn, addr):
    conn.settimeout(IDLE_TIMEOUT)
    conn.sendall(b"Welcome to the echo server. Type 'quit' to leave.\n")
    while True:
        try:
            data = conn.recv(MAX_BYTES + 1)
        except socket.timeout:
            #A (timeout): log that addr was idle too long,
            #send b"Timed out. Bye.\n", then return
            log(f"{addr} was idle for too long")
            conn.sendall(b"Timed out. Bye.\n")
            return
        if not data:                      # empty bytes = client closed the connection
            log(f"{addr} disconnected")
            return
        if len(data) > MAX_BYTES:
            #B (oversized): log it, send b"ERROR: message too long. Closing connection.\n",
            #then return (drop the client)
            log(f"{addr} sent an oversized message")
            conn.sendall(b"ERROR: message too long. Closing connection.\n")
            return # drop the client
        try:
            text = data.decode("utf-8").strip()
        except UnicodeDecodeError:
            #C (malformed): log the first 20 bytes with {data[:20]!r},
            #send b"ERROR: not valid UTF-8 text\n", then continue (keep the client)
            log(f"{addr} sent malformed data: {data[:20]!r}")
            conn.sendall(b"ERROR: not valid UTF-8 text\n")
            continue
        if text.lower() == "quit":
            conn.sendall(b"Bye!\n")
            log(f"{addr} quit")
            return
        log(f"{addr} said: {text!r}")
        conn.sendall(f"ECHO: {text}\n".encode())


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        server.settimeout(1.0)  # wake up every second so Ctrl+C works on Windows
        log(f"Listening on {HOST}:{PORT} (Ctrl+C to stop)")
        while True:
            try:
                conn, addr = server.accept()
            except socket.timeout:
                continue
            log(f"Connection from {addr}")
            with conn:
                try:
                    handle(conn, addr)
                except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                    log(f"{addr} dropped the connection")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Server stopped.")