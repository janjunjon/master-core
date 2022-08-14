class MSMp:
    def __init__(self, nc) -> None:
        self.nc = nc
        self.lat, self.lon = self.getLatLon(nc)
        self.u, self.v = self.getWind(nc)
        self.rh = self.getRelativeHumidity(nc)
        self.temp = self.getTemperature(nc)
        self.w = self.getVerticalVelocity(nc)
        self.z = self.getGeopotentialHeight(nc)
        pass

    def getLatLon(self, nc):
        lat = nc.variables['lat']
        lon = nc.variables['lon']
        return lat, lon

    def getWind(self, nc):
        u = nc.variables['u']
        v = nc.variables['v']
        return u, v
    
    def getRelativeHumidity(nc):
        rh = nc.variables['rh']
        return rh

    def getTemperature(self, nc):
        temp = nc.variables['temp']
        return temp

    def getVerticalVelocity(self, nc):
        w = nc.variables['w']
        return w

    def getGeopotentialHeight(self, nc):
        z = nc.variables['z']
        return z