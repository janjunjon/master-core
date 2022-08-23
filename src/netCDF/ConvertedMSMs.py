import netCDF4

class ConvertedMSMs:
    def __init__(self, file) -> None:
        self.nc = netCDF4.Dataset(file)
        self.lat, self.lon = self.getLatLon(self.nc)
        self.r1h = self.getRain(self.nc)
        pass

    def getLatLon(self, nc):
        lat, lon = self._returnConvertedLatLon(self, nc)
        return lat, lon

    def getRain(self, nc):
        r1h = self._convertMSMsTo3hours(self, nc)
        return r1h

    def _convertMSMsResolution(self, v_array):
        normal_array_with_time = []
        for time_a in v_array:
            lat_a = []
            for i in range(0, len(time_a), 2):
                lon_a = []
                for j in range(0, len(time_a[i]), 2):
                    lon_a.append(time_a[i][j])
                lat_a.append(lon_a)
            normal_array_with_time.append(lat_a)
        return normal_array_with_time

    def _returnConvertedLatLon(self, nc):
        lat = nc.variables['lat'][:].tolist()
        lon = nc.variables['lon'][:].tolist()
        convertedLat = []
        convertedLon = []
        for i in range(0, len(lat), 2):
            convertedLat.append(lat[i])
        for j in range(0, len(lon), 2):
            convertedLon.append(lon[j])
        return [convertedLat, convertedLon]

    def _convertMSMsTo3hours(self, nc, var='r1h'):
        v_array = nc.variables[var][:][:][:].tolist()
        normal_array_with_time = self._convertMSMsResolution(v_array)
        accumulate3hours = []    
        for i in range(0, 24, 3):
            lat_a = []
            for j in range(0, 253):
                lon_a = []
                for k in range(0, 241):
                    lon_a.append(
                        normal_array_with_time[i][j][k] + normal_array_with_time[i+1][j][k] + normal_array_with_time[i+2][j][k]
                    )
                lat_a.append(lon_a)
            accumulate3hours.append(lat_a)
        return accumulate3hours