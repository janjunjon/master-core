import numpy as np

from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF

class MaskedRain(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        # 0,3,6,9,12,15,18,21時は欠損
        # self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.filename = file.split('/')[-1].split('.')[0]
        self.indexes = np.load(file='/home/jjthomson/fdrive/ra/tanaka2019/undef.npy')

    def recreateRain(self):
        # rain_Ra = self.putMaskedValue('rain_Ra')
        # rain_MSMs = self.putMaskedValue('rain_MSMs')
        rain_Ra = np.load('/home/jjthomson/fdrive/npy/MaskedRain_Ra.npy')
        rain_MSMs = np.load('/home/jjthomson/fdrive/npy/MaskedRain_MSMs.npy')
        # rain_MSMs = self.nc.variables['rain_MSMs'][:]
        CreateNetCDF.createNcFileRaMSMsRain(
            path='/home/jjthomson/fdrive/nc/recreated/rains2.nc',
            filename='20200701',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=rain_Ra,
            rainList2=rain_MSMs
        )

    def putMaskedValue(self, varname):
        for time in self.time:
            rain = np.ravel(self.nc.variables[varname][time])
            rains = np.array([])
            for i in range(253*241):
                if i in self.indexes:
                    rain[i] = -999
                rains = np.append(rains, rain[i])
            rains = np.reshape(rains, (253,241))
            if self.time.index(time) == 0:
                MaskedRain = np.array([rains])
            else:
                MaskedRain = np.append(MaskedRain, [rains], axis=0)
            print(f'ndim: {MaskedRain.ndim}', len(MaskedRain), len(MaskedRain[0]), len(MaskedRain[0][0]))
        setattr(self, f'MaskedRain_{varname}', MaskedRain)
        return MaskedRain

class NoMaskedRain(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        # 0,3,6,9,12,15,18,21時は欠損
        # self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.filename = file.split('/')[-1].split('.')[0]
        self.indexes = np.load(file='/home/jjthomson/fdrive/ra/tanaka2019/undef.npy')
        # self.nc = NetCDF('/home/jjthomson/fdrive/nc/combined/rains.nc')

    def recreateRain(self):
        rain_Ra = self.putMaskedValue('rain_Ra')
        rain_MSMs = self.putMaskedValue('rain_MSMs')
        # rain_Ra = self.nc.variables['rain_Ra']
        # rain_MSMs = self.nc.variables['rain_MSMs']
        # rain_MSMs = self.nc.variables['rain_MSMs'][:]
        CreateNetCDF.createNcFileRaMSMsRain(
            path='/home/jjthomson/fdrive/nc/combined/rains_nomask.nc',
            filename='20200701',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=rain_Ra,
            rainList2=rain_MSMs
        )

    def putMaskedValue(self, varname):
        for time in self.time:
            rain = np.ravel(self.nc.variables[varname][time])
            rains = np.array([])
            for i in range(253*241):
                if i in self.indexes:
                    rain[i] = 0
                rains = np.append(rains, rain[i])
            rains = np.reshape(rains, (253,241))
            if self.time.index(time) == 0:
                MaskedRain = np.array([rains])
            else:
                MaskedRain = np.append(MaskedRain, [rains], axis=0)
            print(f'ndim: {MaskedRain.ndim}', len(MaskedRain), len(MaskedRain[0]), len(MaskedRain[0][0]))
        setattr(self, f'MaskedRain_{varname}', MaskedRain)
        return MaskedRain