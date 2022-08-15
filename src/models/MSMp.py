import netCDF4

class MSMp:
    def __init__(self, file) -> None:
        self.nc = netCDF4.Dataset(file)
        self.lat, self.lon = self.getLatLon(self.nc)
        self.u, self.v = self.getWind(self.nc)
        self.rh = self.getRelativeHumidity(self.nc)
        self.temp = self.getTemperature(self.nc)
        self.w = self.getVerticalVelocity(self.nc)
        self.z = self.getGeopotentialHeight(self.nc)
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