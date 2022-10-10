from netCDF.ConvertedAllMSMs import ConvertedAllMSMs
import os

class Execution:
    def __init__(self, path) -> None:
        self.path = path

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            startString = file[0]
            if startString == 's':
                nc = ConvertedAllMSMs('{}/{}'.format(self.path, file))
                savePath = file[1:9]
                nc.makeNetcdfFile(
                    '/home/jjthomson/fdrive/nc/converted/{}.nc'.format(savePath),
                    nc.lon,
                    nc.lat,
                    nc.time,
                    nc.rain,
                    nc.sp
                )