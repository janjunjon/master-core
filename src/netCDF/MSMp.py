from netCDF.NetCDF import *
from Module.Reverse import Reverse

class MSMp(NetCDF):
    def __init__(self, path) -> None:
        super().__init__(path)
        lat = self.nc.variables['lat'][:].tolist()
        lat.reverse()
        self.lat = lat
        self.lon = self.variables['lon'][:].tolist()
        self.p = [
            1000.,  975.,  950.,  925.,  900.,  850.,  800.,  700.,  600.,  500.,  400.,  300.,  250.,  200.,  150.,  100.
        ]
        self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.varNcMSMp  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.getVars()
        self.reverse()

    def getVars(self):
        for var_name in self.varNcMSMp:
            setattr(self, var_name, self.nc.variables[var_name][:].tolist())

    def reverse(self):
        for var_name in self.varNcMSMp:
            setattr(self, var_name, Reverse.reverseLat(getattr(self, var_name)))