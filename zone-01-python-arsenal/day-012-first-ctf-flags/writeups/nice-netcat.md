# Nice netcat
**Category:** General Skills · **Platform:** CyLab Security Academy · **Difficulty:** Easy

## Goal
Connect to a remote service and decode the flag it sends.

## Method
1. Connected with `nc chatelaine.cylabacademy.net 19749`. The server replied with a column of numbers.
2. Recognized them as decimal ASCII codes (97 = `a`, 123 = `{`, 125 = `}`).
3. Piped the output into Python to convert each number to its character:
   `nc ... | python3 -c "import sys; print(''.join(chr(int(n)) for n in sys.stdin.read().split()))"`

## Flag
`academy{g00d_k1tty!_n1c3_k1tty!_f6739}` (redacted)

## Lesson
`nc` connects to any TCP port, like my Day 7 client. The flag was encoded as decimal ASCII, not encrypted, so anyone can reverse it. Piping one tool into another solved it in one line.