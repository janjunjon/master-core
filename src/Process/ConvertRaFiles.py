import subprocess
import os
from Abstract.Abstract import Abstract

class Execution(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def main(self):
        for conbinations in self.filenames():
            command = "{}/src/c/short2f4ra1km {} {}".format(self.root_path, conbinations[0], conbinations[1])
            print(command)
            subprocess.run(command, shell=True)

    def filenames(self):
        combinations = []
        days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        hours = ["0100", "0400", "0700", "1000", "1300", "1600", "1900", "2200"]
        for day in days:
            for hour in hours:
                input = "{}/fdrive/ra/202007/{}/202007{}{}.bin".format(self.localdir, day, day, hour)
                output = "{}/fdrive/ra/converted/202007{}{}_converted.bin".format(self.localdir, day, hour)
                arr = [input, output]
                combinations.append(arr)
        return combinations