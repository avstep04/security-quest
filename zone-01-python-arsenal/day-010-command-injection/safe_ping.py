import ipaddress
import platform
import re
import subprocess

COUNT_FLAG = "-n" if platform.system() == "Windows" else "-c"
# A hostname: letters, digits and hyphens in dot-separated labels, never starting with "-"
HOSTNAME = re.compile(
    r"^(?=.{1,253}$)[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?(\.[A-Za-z0-9]([A-Za-z0-9-]*[A-Za-z0-9])?)*$"
)


def is_valid_host(host):
    #A (layer 1, input validation):
    #   try: ipaddress.ip_address(host) -> return True if it is a valid IP
    #   except ValueError: return bool(HOSTNAME.match(host))
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return bool(HOSTNAME.match(host))


def main():
    host = input("Host to ping: ").strip()
    if not is_valid_host(host):
        print(f"Rejected: {host!r} is not a valid IP address or hostname.")
        return
    #B (layer 2, no shell): set `command` to a LIST:
    #   ["ping", COUNT_FLAG, "1", host]
    command = ["ping", COUNT_FLAG, "1", host]
    print(f"Running: {command}\n")
    result = subprocess.run(command, capture_output=True, text=True, timeout=10)
    print(result.stdout or result.stderr)


if __name__ == "__main__":
    main()