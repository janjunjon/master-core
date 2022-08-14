import netCDF4

class MSMs:
    def __init__(self, file) -> None:
        self.nc = netCDF4.Dataset(file)
        self.lat, self.lon = self.getLatLon(self.nc)
        self.r1h = self.getRain(self.nc)
        self.u, self.v = self.getWind(self.nc)
        self.rh = self.getRelativeHumidity(self.nc)
        self.temp = self.getTemperature(self.nc)
        self.psea = self.getSeaLevelPressure(self.nc)
        self.sp = self.getSurfaceAirPressure(self.nc)
        pass

    def getLatLon(self, nc):
        lat = nc.variables['lat']
        lon = nc.variables['lon']
        return lat, lon

    def getRain(self, nc):
        r1h = nc.variables['r1h']
        return r1h

    def getWind(self, nc):
        u = nc.variables['u']
        v = nc.variables['v']
        return u, v
    
    def getRelativeHumidity(self, nc):
        rh = nc.variables['rh']
        return rh

    def getTemperature(self, nc):
        temp = nc.variables['temp']
        return temp

    def getSeaLevelPressure(self, nc):
        psea = nc.variables['psea']
        return psea

    def getSurfaceAirPressure(self, nc):
        sp = nc.variables['sp']
        return sp