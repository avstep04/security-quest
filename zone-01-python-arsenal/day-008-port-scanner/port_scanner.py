import argparse
import socket
import time
from concurrent.futures import ThreadPoolExecutor

ALLOWED_TARGETS = {"127.0.0.1", "localhost"}  # only scan machines I own


def scan_port(host, port, timeout):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return port, "open"
    #A: add three except branches:
    #ConnectionRefusedError        -> return port, "closed"
    #(socket.timeout, TimeoutError) -> return port, "filtered"
    #OSError                       -> return port, "error"
    except ConnectionRefusedError:
        return port, "closed"
    except (socket.timeout, TimeoutError):
        return port, "filtered"
    except OSError:
        return port, "error"


def service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def parse_ports(spec):
    start, _, end = spec.partition("-")
    return range(int(start), int(end or start) + 1)


def main():
    parser = argparse.ArgumentParser(description="Threaded TCP connect scanner (localhost only)")
    parser.add_argument("host")
    parser.add_argument("-p", "--ports", default="1-1024", help="port or range, e.g. 80 or 1-1024")
    parser.add_argument("--timeout", type=float, default=0.5)
    parser.add_argument("--workers", type=int, default=100)
    args = parser.parse_args()

    #B: if args.host is not in ALLOWED_TARGETS, print
    #"Refusing to scan <host>: not on my allowlist" and return
    if args.host not in ALLOWED_TARGETS:
        print(f"Refusing to scan {args.host}: not on my allowlist")
        return
    

    ports = parse_ports(args.ports)
    print(f"Scanning {args.host}, {len(ports)} ports, {args.workers} threads...")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda p: scan_port(args.host, p, args.timeout), ports))
    elapsed = time.perf_counter() - start

    open_ports = [p for p, state in results if state == "open"]
    print("\nPORT     STATE  SERVICE")
    for p in open_ports:
        print(f"{p:<8} open   {service_name(p)}")
    print(f"\n{len(open_ports)} open, {len(ports) - len(open_ports)} not open, scanned in {elapsed:.2f}s")


if __name__ == "__main__":
    main()