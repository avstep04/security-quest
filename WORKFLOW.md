# Security Quest Workflow

My checklist for every day of the 200-day quest. This file is the master copy:
Claude reads it from GitHub before each new day, so any rule I add here gets followed.

---

## 1. Start a day
- [ ] Tell Claude the day number and title, exactly as on the quest page (e.g. "Day 3: Encoding is not encryption").
- [ ] Doing several days in one sitting is fine. Each day still gets its own folder, commit and table row.

## 2. Create the folder and files
- [ ] Folder: `zone-XX-<zone-name>/day-NNN-<title>/` (three-digit day number, lowercase, hyphens)
  - Example: `zone-01-python-arsenal/day-003-encoding-is-not-encryption/`
- [ ] Create files by right-clicking the day folder in VS Code → **New File...**
- [ ] Code goes in the editor (top). The terminal (bottom) only runs commands like `python file.py`.

## 3. Write the day README (`day-NNN-<title>/README.md`)
Same sections every day:
```
# Day N: <Title>
**Zone X: <Zone name>** · Completed: <date>

## What it does        (table: File | Purpose)
## How to run          (code block with the commands)
## Results             (bold label, then a small table, then a one-line takeaway)
## What I learned      (3-4 bullets)
## Key notes
### New today          (table: Term | What it does)
### Already seen       (terms from earlier days, e.g. `.encode()` (Day 2))
```

## 4. Key notes rules (Claude writes these)
- [ ] Every new function, method, command, flag or tool gets a one-line, plain-English note.
- [ ] Anything already explained on an earlier day is NOT re-explained. It goes under **Already seen** with the day it was first used.
- [ ] `GLOSSARY.md` decides what's "already seen."

## 5. Update the three shared files
| File | Where | What to add |
|---|---|---|
| Day `README.md` | inside the day folder | The full write-up (step 3) |
| `GLOSSARY.md` | repo root | New terms only, with `Day N` in the third column. No blank lines inside the table. |
| `README.md` (main) | repo root | One progress row, linked format (below) |

Progress row format:
```
| N | [Title](zone-XX-<zone-name>/day-NNN-<title>/) | 2-4 line skills description from Claude |
```

## 6. Preview, commit, push
- [ ] Save everything (**Ctrl+S**). A white dot on a tab means it's unsaved.
- [ ] Preview Markdown with **Ctrl+Shift+V**.
- [ ] In GitHub Desktop, type in the small **Summary** box (not Description): `Day N: <Title>`
- [ ] Follow-up fixes on the same day: `Day N: tidy code` (or a short description)
- [ ] **Commit to main** → **Push origin**
- [ ] Tell Claude "pushed."

## 7. After pushing
- [ ] Claude pulls the repo, runs the code, and reviews the README, glossary and progress table.
- [ ] Fix anything flagged (stray imports, leftover TODOs, typos).
- [ ] Click **Capture the flag** for the day on the quest page.

## 8. What Claude does every day
- Reminds me of the folder name and commit Summary for the day.
- Walks me through the lesson step by step, with outlines I fill in myself.
- Writes the Key notes (new vs. already seen), glossary rows and progress-table row.
- Reviews my pushed code and formatting.
- Adds a progress check when something matters (see 9).

## 9. Progress checks
- **Pace:** days done, streak.
- **Repo hygiene:** no secrets, passwords or API keys in any file, ever.
- **Going public:** keep the repo private until Day 11 (secret scanning), then make it public.
- **Cloud clocks:** open AWS on Day 91 (Free plan: 6 months or until credits run out). Open Azure on Day 166 ($200 credit lasts 30 days).
- **Boss days (15, 30, 45 ... 200):** go slower. Each one gets a resume bullet, a LinkedIn post idea, and a project card on my website.
- **Website:** start the GitHub Pages portfolio at Day 15, then add a card at every boss.
- **Certification:** pick one on Day 191 (Security+, AWS SCS-C03, AZ-104, SC-200 or SC-500).

## 10. Setup facts
- Repo: `C:\Users\Andrew\code\security-quest` (outside OneDrive) → github.com/avstep04/security-quest
- Windows: VS Code + PowerShell, Python 3.11. Linux: WSL Ubuntu, Python 3.14 (`cd ~` first).
- Rules of engagement: only test systems built for practice or that I own.

## 11. My custom rules
Add new checks here. Claude follows them from the next day on.
- **LinkedIn tool alert:** whenever a day's lesson uses a named industry tool or platform (AWS, Azure, Wireshark, Nmap, Burp Suite, Splunk, Wazuh, Terraform, etc.), Claude flags it at the start of that day as 🔔 **LinkedIn-worthy**, with the exact skill name to add to LinkedIn and my resume.

## Change log
- Nov 22, 2026: Created. Days 1-2 complete.
- Nov 24, 2026: Added LinkedIn tool alert rule.
