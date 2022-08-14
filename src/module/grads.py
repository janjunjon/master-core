import subprocess
import os

def main(command):
    subprocess.run(command, shell=True)

def grads_command(*args):
    command = "grads -blc {}".format(*args)
    return command

# ------------------------------------------------------------

def execute_shell(gradsfile, *args):
    gradsfile = os.path.expanduser(gradsfile)
    command = f"grads -blc {gradsfile}"
    if len(args) == 0:
        print("$", command)
        stream = os.popen(command)
    else:
        for argv in args:
            command += f" {argv}"
        print("$", command)
        stream = os.popen(command)
    return stream