from ..module import netcdf

class MSMs:
    def __init__(self, nc) -> None:
        self.nc = nc
        self.lat, self.lon = self.getLatLon(nc)
        self.r1h = self.getRain(nc)
        pass

    def getLatLon(nc):
        lat, lon = netcdf._returnConvertedLatLon(nc)
        return lat, lon

    def getRain(nc):
        r1h = netcdf.convertMSMsTo3hours(nc) 
        return r1h