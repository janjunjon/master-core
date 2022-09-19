import netCDF4
from netCDF.NetCDF import NetCDF

class ConvertedMSMs(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        self.nc = netCDF4.Dataset(file, format="NETCDF3_CLASSIC")
        self.lat, self.lon = self.getLatLon()
        # 0,3,6,9,12,15,18,21時は欠損
        self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.rain = self.getRain()
        self.filename = file.split('/')[-1].split('.')[0]
        self.MSMRange = [120, 150, 22.4, 47.6]

    def getLatLon(self):
        lat, lon = self._returnConvertedLatLon()
        return lat, lon

    def getRain(self):
        r1h = self._convertMSMsTo3hoursWithNoAccumulation()
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

    def _returnConvertedLatLon(self):
        lat = self.nc.variables['lat'][:].tolist()
        lon = self.nc.variables['lon'][:].tolist()
        convertedLat = []
        convertedLon = []
        for i in range(0, len(lat), 2):
            convertedLat.append(lat[i])
        for j in range(0, len(lon), 2):
            convertedLon.append(lon[j])
        return [convertedLat, convertedLon]

    def _convertMSMsTo3hoursWithAverage(self, var='r1h'):
        v_array = self.nc.variables[var][:][:][:].tolist()
        normal_array_with_time = self._convertMSMsResolution(v_array)
        accumulate3hours = []    
        for i in range(0, 24, 3):
            lat_a = []
            for j in range(0, 253):
                lon_a = []
                for k in range(0, 241):
                    lon_a.append(
                        (normal_array_with_time[i+1][j][k] + normal_array_with_time[i+2][j][k]) / 2
                    )
                lat_a.append(lon_a)
            accumulate3hours.append(lat_a)
        return accumulate3hours

    def _convertMSMsTo3hoursWithNoAccumulation(self, var='r1h'):
        v_array = self.nc.variables[var][:][:][:].tolist()
        normal_array_with_time = self._convertMSMsResolution(v_array)
        accumulate3hours = []    
        for i in range(0, 24, 3):
            lat_a = []
            for j in range(0, 253):
                lon_a = []
                for k in range(0, 241):
                    lon_a.append(
                        normal_array_with_time[i+1][j][k]
                    )
                lat_a.append(lon_a)
            accumulate3hours.append(lat_a)
        return accumulate3hours

    def makeNetcdfFile(self, path, lonList, latList, timeList, rainList):
        super().makeNetcdfFile(path, lonList, latList, timeList, rainList)

    def drawMapByArray(self, v_array, v_lat, v_lon, t, path):
        super().drawMapByArray(v_array, v_lat, v_lon, t, path)