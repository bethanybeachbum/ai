import subprocess
cmd =input('Enter command to run:  ');
subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
