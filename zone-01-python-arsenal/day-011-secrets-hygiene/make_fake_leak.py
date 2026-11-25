import secrets
import string

fake = "ghp_" + "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(36))
with open("fake_leak.py", "w") as f:
    f.write(f'GITHUB_TOKEN = "{fake}"  # FAKE token for testing gitleaks\n')
print("Wrote fake_leak.py (fake GitHub token)")
