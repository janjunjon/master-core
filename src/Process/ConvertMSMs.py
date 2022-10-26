from netCDF.ConvertedMSMs import ConvertedMSMs
import os

class Execution:
    def __init__(self, path) -> None:
        self.path = path

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            startString = file[0]
            if startString == 's':
                filepath = '{}/{}'.format(self.path, file)
                nc = ConvertedMSMs(filepath)
                nc.createNetcdfFile()