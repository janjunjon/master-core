from netCDF.ConvertedRa import ConvertedRa
import os

class Execution:
    def __init__(self, path) -> None:
        self.path = path

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            nc = ConvertedRa('{}/{}'.format(self.path, file))
            savePath = file[2:10]
            nc.makeNetcdfFile(
                '/home/jjthomson/fdrive/ra/reshaped/{}.nc'.format(savePath),
                nc.lon,
                nc.lat,
                nc.time,
                nc.rain
            )