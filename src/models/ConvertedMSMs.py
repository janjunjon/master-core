import sys
sys.path.append('../')
from module import netcdf
import netCDF4

class ConvertedMSMs:
    def __init__(self, file) -> None:
        self.nc = netCDF4.Dataset(file)
        self.lat, self.lon = self.getLatLon(self.nc)
        self.r1h = self.getRain(self.nc)
        pass

    def getLatLon(self, nc):
        lat, lon = netcdf._returnConvertedLatLon(nc)
        return lat, lon

    def getRain(self, nc):
        r1h = netcdf.convertMSMsTo3hours(nc) 
        return r1h