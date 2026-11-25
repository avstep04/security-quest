# Wave a flag
**Category:** General Skills · **Platform:** CyLab Security Academy · **Difficulty:** Easy

## Goal
Run a downloaded program and find the flag in its output.

## Method
1. Downloaded the program with `wget <link>`.
2. Running `./warm` failed with "Permission denied", so I added execute permission with `chmod +x warm`.
3. Ran `./warm`, which suggested using its help option.
4. Ran `./warm -h`, which printed the flag.

## Flag
`academy{b1scu1ts_4nd_gr4vy_57d8c79}` (redacted)

## Lesson
Downloaded files aren't executable until you `chmod +x` them, and `-h` (help) is the first thing to try with any unfamiliar program.