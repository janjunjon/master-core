import numpy as np
from netCDF.NetCDF import NetCDF

class MaskedRain(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        # 0,3,6,9,12,15,18,21時は欠損
        # self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.filename = file.split('/')[-1].split('.')[0]
        self.indexes = np.load(file='/home/jjthomson/fdrive/ra/tanaka2019/undef.npy')

    def putMaskedValue(self):
        MaskedRain = np.array([])
        for time in self.time:
            rain = np.ravel(self.nc.variables['rain'][time])
            rains = np.array([])
            for i in range(253*241):
                if i in self.indexes:
                    rain[i] = -999.0
                if i < 100:
                    print(rain[i])
                rains = np.append(rains, rain[i])
            rains = np.reshape(rains, (253,241))
            MaskedRain = np.append(MaskedRain, rains, axis=0)
        return MaskedRain