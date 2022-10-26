from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF
import netCDF4
import os

class Execution:
    def __init__(self) -> None:
        self.path = '/home/jjthomson/fdrive/nc/converted'
        self.nc = netCDF4.Dataset('/home/jjthomson/fdrive/nc/converted/20200701.nc')
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.time = range(0, 248)

    def main(self):
        rains = self.conbineMSMs()
        CreateNetCDF.createNcFileMSMsOnlyRain(
            path='/home/jjthomson/fdrive/nc/MSMs.nc',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList=rains
        )

    def conbineMSMs(self):
        files = os.listdir(self.path)
        rains = []
        for file in files:
            if file == '20200630.nc':
                nc = NetCDF('{}/{}'.format(self.path, file))
                nc.dimensions
                rain = nc.variables['rain'][:][:][:].tolist()
                for i in [5,6,7]:
                    rains.extend([rain[i]])
            elif file == '20200731.nc':
                nc = NetCDF('{}/{}'.format(self.path, file))
                rain = nc.variables['rain'][:][:][:].tolist()
                for i in [0,1,2,3,4]:
                    rains.extend([rain[i]])
            else:
                nc = NetCDF('{}/{}'.format(self.path, file))
                rain = nc.variables['rain'][:][:][:].tolist()
                rains.extend(rain)
            print('length', len(rains))
        return rains