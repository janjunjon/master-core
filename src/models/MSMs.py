from ..module import netcdf

class MSMs:
    def __init__(self, nc) -> None:
        self.nc = nc
        self.lat, self.lon = self.getLatLon(nc)
        self.r1h = self.getRain(nc)
        self.u, self.v = self.getWind(nc)
        self.rh = self.getRelativeHumidity(nc)
        self.temp = self.getTemperature(nc)
        self.w = self.getVerticalVelocity(nc)
        self.z = self.getGeopotentialHeight(nc)
        pass

    def getLatLon(nc):
        lat = nc.variables['lat']
        lon = nc.variables['lon']
        return lat, lon

    def getRain(nc):
        r1h = nc.variables['r1h']
        return r1h

    def getWind(nc):
        u = nc.variables['u']
        v = nc.variables['v']
        return u, v
    
    def getRelativeHumidity(nc):
        rh = nc.variables['rh']
        return rh

    def getTemperature(nc):
        temp = nc.variables['temp']
        return temp

    def getVerticalVelocity(nc):
        w = nc.variables['w']
        return w

    def getGeopotentialHeight(nc):
        z = nc.variables['z']
        return z