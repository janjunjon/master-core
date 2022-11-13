from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF
import netCDF4
import os

class Execution:
    def __init__(self) -> None:
        self.path = '/home/jjthomson/fdrive/ra/reshaped'
        self.nc = netCDF4.Dataset('/home/jjthomson/fdrive/ra/reshaped/20200701.nc')
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.time = range(0, 248)

    def main(self):
        rains = self.conbineRa()
        CreateNetCDF.createNcFileRain(
            path='/home/jjthomson/fdrive/ra/ra.nc',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList=rains
        )

    def conbineRa(self):
        files = os.listdir(self.path)
        rains = []
        for file in files:
            nc = NetCDF('{}/{}'.format(self.path, file))
            rain = nc.variables['rain'][:][:][:].tolist()
            rains.extend(rain)
        return rains