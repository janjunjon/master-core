from netCDF.NetCDF import NetCDF
from Module.Reverse import Reverse
from Module.CreateNetCDF import CreateNetCDF

class ReverseRains(NetCDF):
    def __init__(self) -> None:
        super().__init__('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')
        self.rain_Ra = self.nc.variables['rain_Ra'][:]
        self.rain_MSMs = self.nc.variables['rain_MSMs'][:]
        self.savePath = f'{self.fdrive_path}/nc/combined/rains_nomask2.nc'

    def main(self):
        rain_Ra = Reverse.reverseLat(self.rain_Ra)
        rain_MSMs = Reverse.reverseLat(self.rain_MSMs)
        CreateNetCDF.createNcFileRaMSMsRain(
            filename='20200701',
            path=self.savePath,
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=rain_Ra,
            rainList2=rain_MSMs
        )

class ReverseRains2(NetCDF):
    def __init__(self) -> None:
        super().__init__('/home/jjthomson/fdrive/rains.nc')
        self.rain_Ra = self.nc.variables['rain_Ra'][:]
        self.rain_MSMs = self.nc.variables['rain_MSMs'][:]
        self.savePath = f'{self.fdrive_path}/nc/combined/rains_nomask.nc'

    def main(self):
        # rain_Ra = Reverse.reverseLat(self.rain_Ra)
        # rain_MSMs = Reverse.reverseLat(self.rain_MSMs)
        rain_Ra = self.rain_Ra
        rain_MSMs = self.rain_MSMs
        CreateNetCDF.createNcFileRaMSMsRain(
            filename='20200701',
            path=self.savePath,
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=rain_Ra,
            rainList2=rain_MSMs
        )

class ReverseMSMp(NetCDF):
    def __init__(self) -> None:
        super().__init__('/home/jjthomson/fdrive/nc/reversed/MSMp.nc')
        self.savePath = f'{self.fdrive_path}/nc/recreated/MSMp.nc'
        self.p = self.variables['p'][:]
        lat = self.lat
        lat.reverse()
        self.lat = lat

    def main(self):
        varnames = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.z = self.variables['z'][:]
        self.w = self.variables['w'][:]
        self.u = self.variables['u'][:]
        self.v = self.variables['v'][:]
        self.temp = self.variables['temp'][:]
        self.rh = self.variables['rh'][:]
        # for varname in varnames:
        #     setattr(self, varname, self.variables[varname][:].tolist())
        #     print(f'set {varname}')
            # setattr(self, varname, Reverse.reverseLat(getattr(self, varname)))
            # print(f'reverse {varname}')
        CreateNetCDF.createNcFileMSMp(
            filename='20200701',
            path=self.savePath,
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            zList=self.z,
            wList=self.w,
            uList=self.u,
            vList=self.v,
            tempList=self.temp,
            rhList=self.rh
        )