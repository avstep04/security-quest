import re
from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).parent / "sample_auth.log"

FAILED = re.compile(r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")
ACCEPTED = re.compile(r"Accepted (?P<method>\w+) for (?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)")

failed_by_ip = Counter()
users_tried = Counter()
accepted = []

with open(LOG_FILE, encoding="utf-8") as f:
    for line in f:
        m = FAILED.search(line)
        if m:
            #add 1 to failed_by_ip for m.group("ip")
            #and add 1 to users_tried for m.group("user")
            failed_by_ip[m.group("ip")] += 1
            users_tried[m.group("user")] += 1
            continue
        m = ACCEPTED.search(line)
        if m:
            accepted.append((m.group("user"), m.group("ip"), m.group("method")))

print("== Failed logins by IP ==")
for ip, count in failed_by_ip.most_common():
    print(f"{ip:15} {count:3}")

print("\n== Usernames attackers tried ==")
for user, count in users_tried.most_common():
    print(f"{user:10} {count:3}")

print("\n== Successful logins ==")
for user, ip, method in accepted:
    print(f"{user:8} from {ip:15} via {method}")