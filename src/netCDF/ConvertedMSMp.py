import netCDF4

from netCDF.NetCDF import NetCDF
from Module.Reverse import Reverse
from Module.CreateNetCDF import *

class ConvertedMSMp(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)

        self.filename = file.split('/')[-1][1:9]
        self.saveDir = '/home/jjthomson/fdrive/nc/converted'

        lat = self.lat
        lat.reverse()
        self.lat = lat
        # 0,3,6,9,12,15,18,21時は欠損
        self.p = self.nc.variables['p'][:].tolist()
        self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.MSMRange = [120, 150, 22.4, 47.6]
        self.varNcMSMs  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.getVars()
        self.reverse()

    def getVars(self):
        for var_name in self.varNcMSMs:
            setattr(self, var_name, self.nc.variables[var_name][:])

    def reverse(self):
        for var_name in self.varNcMSMs:
            setattr(self, var_name, Reverse.reverseLat(getattr(self, var_name)))