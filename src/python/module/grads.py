import os

def execute_shell(gradsfile, *args):
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