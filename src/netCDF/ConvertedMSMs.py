import netCDF4

from netCDF.NetCDF import NetCDF
from Module.Reverse import Reverse
from Module.CreateNetCDF import *

class ConvertedMSMs(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)

        self.filename = file.split('/')[-1][1:9]
        self.saveDir = '/home/jjthomson/fdrive/nc/converted'

        lon = self.lon
        lat = self.lat
        lat.reverse()
        self.lat, self.lon = self.getLatLon(lat, lon)
        # 0,3,6,9,12,15,18,21時は欠損
        self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.MSMRange = [120, 150, 22.4, 47.6]
        self.varNcMSMs  = ['r1h', 'psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.getVars()
        self.reverse()

    def getVars(self):
        for var_name in self.varNcMSMs:
            if var_name == 'r1h':
                setattr(self, 'rain', self._convertMSMsTo3hoursWithNoAccumulation(var_name))
            else:
                setattr(self, var_name, self._convertMSMsTo3hoursWithNoAccumulation(var_name))

    def reverse(self):
        for var_name in self.varNcMSMs:
            if var_name == 'r1h':
                setattr(self, 'rain', Reverse.reverseLat(getattr(self, 'rain')))
            else:
                setattr(self, var_name, Reverse.reverseLat(getattr(self, var_name)))

    def getLatLon(self, lat, lon):
        lat, lon = self._returnConvertedLatLon(lat, lon)
        return lat, lon

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

    def _returnConvertedLatLon(self, lat, lon):
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