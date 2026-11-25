# Python Wrangling
**Category:** General Skills · **Platform:** CyLab Security Academy · **Difficulty:** Easy

## Goal
Use a provided Python script and password to decrypt an encrypted flag file.

## Method
1. Downloaded `ende.py`, `password.txt` and `flag.txt.en` with `wget`.
2. Ran `python3 ende.py` with no arguments to see its usage: `ende.py (-e/-d) [file]`.
3. Read the password with `cat password.txt`.
4. Ran `python3 ende.py -d flag.txt.en` and entered the password when asked, which printed the flag.

## Flag
`academy{4p0110_1n_7h3_h0us3_d6af8f37}` (redacted)

## Lesson
Running a tool with no arguments usually prints its usage. This was real encryption: unlike Day 3's encoding, the flag file was unreadable without the key in `password.txt`.