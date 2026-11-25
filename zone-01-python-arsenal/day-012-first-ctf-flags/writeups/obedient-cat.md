# Obedient Cat
**Category:** General Skills · **Platform:** CyLab Security Academy · **Difficulty:** Easy

## Goal
Find the flag hidden in a downloadable file.

## Method
1. Copied the file's download link from the challenge page.
2. Downloaded it in the webshell with `wget <link>`.
3. Confirmed it arrived with `ls`.
4. Printed its contents with `cat flag`, which revealed the flag.

## Flag
`academy{s4n1ty_v3r1f13d_61ddac22}` (redacted)

## Lesson
`cat` prints a file to the screen, the quickest way to inspect a small file in Linux. `wget` downloads files from the command line.