# WARNING: deliberately vulnerable. For learning on my own machine only.
import platform
import subprocess

COUNT_FLAG = "-n" if platform.system() == "Windows" else "-c"

host = input("Host to ping: ")
# BAD: user input is pasted into a shell command string
command = f"ping {COUNT_FLAG} 1 {host}"
print(f"Running: {command}\n")
subprocess.run(command, shell=True)