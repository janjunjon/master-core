import sys
sys.path.append('../')
from module import netcdf

class ConvertedMSMs:
    def __init__(self, nc) -> None:
        self.nc = nc
        self.lat, self.lon = self.getLatLon(nc)
        self.r1h = self.getRain(nc)
        pass

    def getLatLon(self, nc):
        lat, lon = netcdf._returnConvertedLatLon(nc)
        return lat, lon

    def getRain(self, nc):
        r1h = netcdf.convertMSMsTo3hours(nc) 
        return r1h