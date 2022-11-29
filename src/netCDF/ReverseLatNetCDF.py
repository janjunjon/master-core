from netCDF.NetCDF import NetCDF
from Module.Reverse import Reverse
from Module.CreateNetCDF import CreateNetCDF

class ReverseRains(NetCDF):
    def __init__(self) -> None:
        super().__init__('/home/jjthomson/fdrive/nc/reversed/rains.nc')
        self.rain_Ra = self.nc.variables['rain_Ra'][:]
        self.rain_MSMs = self.nc.variables['rain_MSMs'][:]
        self.savePath = f'{self.fdrive_path}/nc/grads/rains.nc'

    def main(self):
        rain_Ra = Reverse.reverseLat(self.rain_Ra)
        rain_MSMs = Reverse.reverseLat(self.rain_MSMs)
        CreateNetCDF.createNcFileRaMSMsRain(
            path=self.savePath,
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=rain_Ra,
            rainList2=rain_MSMs
        )

class ReverseMSMs(NetCDF):
    pass