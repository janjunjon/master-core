from Module.Draw import Draw
from netCDF.NetCDF import NetCDF

class Execution:
    def __init__(self) -> None:
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_MSMp = NetCDF('/home/jjthomson/fdrive/nc/LowLoadMSMp.nc')

        self.rain_Ra = self.nc_rains.variables['rain_Ra'][:][:][:].tolist()
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs'][:][:][:].tolist()
        self.lat = self.nc_rains.variables['lat'][:].tolist()
        self.lon = self.nc_rains.variables['lon'][:].tolist()
        # self.region = [30, 35, 128, 133]
        self.region = [22, 48, 120, 150]

    def main(self):
        for i in range(len(self.rain_Ra)):
            path = '/home/jjthomson/fdrive/images/python/ra/{}.png'.format(i)
            d = Draw()
            d.drawMapByArray(
                v_array=self.rain_Ra,
                v_lat=self.lat,
                v_lon=self.lon,
                t=i,
                path=path,
                region=self.region
            )
            path = '/home/jjthomson/fdrive/images/python/MSMs/{}.png'.format(i)
            d = Draw()
            d.drawMapByArray(
                v_array=self.rain_MSMs,
                v_lat=self.lat,
                v_lon=self.lon,
                t=i,
                path=path,
                region=self.region
            )