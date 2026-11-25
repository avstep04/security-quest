# strings it
**Category:** General Skills · **Platform:** CyLab Security Academy · **Difficulty:** Easy

## Goal
Find a flag hidden inside a compiled program that's too large to read by hand.

## Method
1. Downloaded the program with `wget <link>`. The file is named `strings`.
2. `cat` showed unreadable binary, so I used the `strings` tool to extract readable text.
3. Piped that into `grep` to keep only the flag line: `strings strings | grep "academy{"`
   (first `strings` = the system tool via PATH, second = the downloaded file).

## Flag
`academy{5tRIng5_1T_DAEbE8bd}` (redacted)

## Lesson
`strings` + `grep` pulls readable text out of binaries, the same technique analysts use to find URLs, passwords and clues in suspicious programs.