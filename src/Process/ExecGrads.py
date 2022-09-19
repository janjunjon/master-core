import subprocess
import os

class Execution:
    def __init__(self, path):
        self.path = path

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            command = ['grads', '-bcp', file]
            print(command)
            subprocess.call(command)