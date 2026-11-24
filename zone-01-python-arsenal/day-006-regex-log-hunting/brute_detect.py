import argparse
import re
from collections import defaultdict
from datetime import datetime, timedelta

LINE = re.compile(
    r"^(?P<ts>\w{3}\s+\d+ \d{2}:\d{2}:\d{2}) \S+ sshd\[\d+\]: "
    r"(?P<result>Failed|Accepted) \w+ for (?:invalid user )?(?P<user>\S+) "
    r"from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)
YEAR = 2026  # classic syslog timestamps leave out the year


def parse(path):
    failures = defaultdict(list)    # ip -> [times of failures]
    successes = defaultdict(list)   # ip -> [(time, user) of logins]
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = LINE.search(line)
            if not m:
                continue
            ts = datetime.strptime(f"{YEAR} {m.group('ts')}", "%Y %b %d %H:%M:%S")
            if m.group("result") == "Failed":
                failures[m.group("ip")].append(ts)
            else:
                successes[m.group("ip")].append((ts, m.group("user")))
    return failures, successes


def max_in_window(times, window):
    # Sliding window: grow the right edge, shrink the left edge while the span is too long
    times = sorted(times)
    best, start = 0, 0
    for end in range(len(times)):
        while times[end] - times[start] > window:
            start += 1
        best = max(best, end - start + 1)
    return best


def main():
    p = argparse.ArgumentParser(description="Flag SSH brute-force attempts in an auth.log")
    p.add_argument("logfile")
    p.add_argument("--threshold", type=int, default=5, help="flag above this many failures")
    p.add_argument("--window", type=int, default=10, help="window in minutes")
    args = p.parse_args()

    window = timedelta(minutes=args.window)
    failures, successes = parse(args.logfile)
    flagged = 0
    for ip, times in sorted(failures.items()):
        peak = max_in_window(times, window)
        #A: if peak is greater than args.threshold:
        #           add 1 to flagged and print an ALERT line with the ip, peak and window
        #         else: print an "ok" line
        #B: inside the ALERT branch, check successes.get(ip, []):
        #         if this IP logged in successfully after its failures, print
        #         "  !! POSSIBLE COMPROMISE: '<user>' logged in from <ip> at <time>"
        if peak > args.threshold:
            flagged += 1
            print(f"ALERT: {ip} had {peak} failures in {args.window} minutes")
            for ts, user in successes.get(ip, []):
                if ts > max(times):
                    print(f"  !! POSSIBLE COMPROMISE: '{user}' logged in from {ip} at {ts}")
    print(f"\n{flagged} IP(s) flagged.")


if __name__ == "__main__":
    main()