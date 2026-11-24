import argparse
import socket


def main():
    parser = argparse.ArgumentParser(description="Talk to the echo server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9000)
    parser.add_argument("--raw", action="store_true", help="send invalid bytes to test the server")
    parser.add_argument("--flood", action="store_true", help="send an oversized message to test the server")
    args = parser.parse_args()

    try:
        with socket.create_connection((args.host, args.port), timeout=5) as sock:
            print(sock.recv(1024).decode().strip())
            if args.raw:
                sock.sendall(b"\xff\xfe\xfd broken bytes")
                print(sock.recv(1024).decode().strip())
                return
            if args.flood:
                sock.sendall(b"A" * 5000)
                print(sock.recv(1024).decode().strip())
                return
            while True:
                msg = input("> ")
                sock.sendall(msg.encode())
                reply = sock.recv(1024).decode().strip()
                print(reply)
                if msg.strip().lower() == "quit" or reply.startswith("Timed out"):
                    break
    except ConnectionRefusedError:
        print("Could not connect. Is the server running?")
    except (ConnectionResetError, ConnectionAbortedError):
        print("The server closed the connection.")


if __name__ == "__main__":
    main()