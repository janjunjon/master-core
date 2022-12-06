import os
import numpy as np

from netCDF.ConvertedRa import ConvertedRa
from Module.CreateNetCDF import CreateNetCDF
from Module.Reverse import Reverse

class Execution:
    def __init__(self, path) -> None:
        self.path = path

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            nc = ConvertedRa('{}/{}'.format(self.path, file))
            savePath = file[2:10]
            CreateNetCDF.createNcFileRa(
                '/home/jjthomson/fdrive/ra/reshaped/{}.nc'.format(savePath),
                nc.lon,
                nc.lat,
                nc.time,
                nc.rain
            )

class Execution201107260100:
    def __init__(self) -> None:
        self.nc = ConvertedRa('/home/jjthomson/fdrive/ra/tanaka2019/ra201107260100.nc')
        self.savePath = '/home/jjthomson/fdrive/ra/tanaka2019/reshaped201107260100.nc'

    def main(self):
        rains = Reverse.reverseLat(self.nc.rain)
        indexes = self.getIndexes(rains)
        self.saveArray(indexes, '/home/jjthomson/fdrive/ra/tanaka2019/undef')
        self.indexes = indexes

    def getIndexes(self, rains):
        count = 0
        indexes = []
        for lat in range(253):
            for lon in range(241):
                rain = rains[lat][lon]
                if rain == -999.0:
                    indexes.append(count)
                count += 1
        return indexes

    def saveArray(self, array, path) -> None:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        np.save(path, array)