# Verified findings: password_store.py

Reviewed `day-005-salted-password-storage/password_store.py` with my `review_code.py` tool (claude-haiku-5-5), 2 runs. Every finding checked by hand on Windows 11.

**Verdicts:** Real · False positive · Partly true (some of the claim holds, some doesn't)

| # | Finding | Run 1 | Run 2 | How I checked | Verdict | My severity |
|---|---|---|---|---|---|---|
| 1 | No login throttling (lines 36-49) | Medium | Medium | Threat model: only my account and admins can run the CLI or read `users.json` (icacls). Anyone who could guess online could copy the hashes and crack them offline instead | Partly true | Low (High if put behind a web service) |
| 2 | Username enumeration on login: no prompt + timing (lines 37-41) | Medium | Low | `login nobody_here` printed "Login failed." instantly with **no password prompt**; `login testuser` asked for a password. Visible without any timing measurement | Real | Medium |
| 3 | Username enumeration on register: "already exists" (line 26) | n/a | Low | Registering `testuser` twice printed "User 'testuser' already exists." | Real (common accepted tradeoff) | Low |
| 4 | Full hash printed on register (line 33) | Low | Low | `register testuser` printed the full `$argon2id$...` hash to the terminal | Real | Low |
| 5 | users.json readable by other users (line 20) | Low | Medium | `icacls users.json`: only SYSTEM, Administrators and my account have access (inherited from my user folder). `umask`/`0644` are Linux/macOS concepts | False positive on my Windows setup (Real on a shared Linux host) | Info |
| 6 | Non-atomic write can truncate users.json (line 20) | Low | Low | Read line 20: `write_text` empties the file, then writes. An interrupt in between leaves broken JSON, and `json.loads` (line 16) then fails on every run | Real | Low |
| 7 | Registration race condition (lines 24-32) | Low | Low | Read lines 24-32: read-modify-write with no lock. Needs two registrations at the same instant, which doesn't happen in a single-user CLI | Partly true | Info |
| 8 | No password policy, empty password allowed (line 28) | Low | Low | `register emptytest` + Enter: empty password accepted. Also, `login testuser` failed with the password I meant to register; with no echo and no confirmation, a typo silently became the password | Real | Medium |
| 9 | `InvalidHashError` not caught (line 45) | n/a | Low | Replaced testuser's hash with `garbage` in `users.json`; login crashed with `argon2.exceptions.InvalidHashError` instead of "Login failed." | Real | Low |
| 10 | No `check_needs_rehash` (line 45) | n/a | Low | `help(PasswordHasher.check_needs_rehash)`: docs say to check and rehash after each successful login. My script never calls it | Real (hardening) | Info |

**Scoreboard:** 10 findings → 7 Real · 2 Partly true · 1 False positive

**Claude's "not flagged" claim checked:** Argon2 defaults are `3 65536 4` (time cost 3, 64 MiB memory, 4 threads), matching RFC 9106's recommended low-memory profile. The stored hash string shows the same (`m=65536,t=3,p=4`). ✅ Correct.

## Run 1 vs run 2
- Same file, same prompt, same model: **6 findings vs 10.** AI review isn't repeatable.
- Severity flipped on two findings (file permissions Low → Medium, login enumeration Medium → Low) with nothing changed.
- Run 2 found three issues run 1 missed (#3, #9, #10). Run 1 had the stronger evidence for #2 (the missing password prompt), which run 2 dropped.
- Every line number in both runs was correct.

## What Claude got wrong or missed
- **Assumed Linux.** Finding 5 used Unix permissions (`umask`, `0644`) that don't apply to Windows ACLs on my machine.
- **Unusable fix advice.** Both runs suggested `fcntl` for file locking. It doesn't exist on Windows (`ModuleNotFoundError`), so the fix would crash. `os.replace()` works on both systems.
- **Severity is a guess.** I raised #2 and #8 to Medium (both easy to trigger) and lowered #1, #5, #7 and #10 based on who can actually reach this tool.

## Takeaway
Claude is a fast first-pass reviewer: accurate line numbers and real findings. But it doesn't know my OS or threat model, its severity ratings change between runs, and its fixes need testing. Run it more than once, verify every finding, and assign severity yourself.