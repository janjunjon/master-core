from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self) -> None:
        self.nc_Ra = NetCDF('/home/jjthomson/fdrive/ra/ra.nc')
        self.nc_MSMs = NetCDF('/home/jjthomson/fdrive/nc/reversedMSMs.nc')
        self.rain_Ra = self.nc_Ra.variables['rain'][:][:][:].tolist()
        self.rain_MSMs = self.nc_MSMs.variables['rain'][:][:][:].tolist()
        self.lat = self.nc_Ra.variables['lat'][:].tolist()
        self.lon = self.nc_Ra.variables['lon'][:].tolist()
        self.time = range(0, 248)

    def main(self):
        CreateNetCDF.createNcFileRaMSMsRain(
            path='/home/jjthomson/fdrive/rains.nc',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=self.rain_Ra,
            rainList2=self.rain_MSMs
        )

    