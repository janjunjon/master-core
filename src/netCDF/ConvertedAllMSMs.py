import netCDF4
import numpy as np
from numpy import dtype
from netCDF.NetCDF import NetCDF

class ConvertedAllMSMs(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        self.nc = netCDF4.Dataset(file, format="NETCDF3_CLASSIC")
        self.lat, self.lon = self.getLatLon()
        # 0,3,6,9,12,15,18,21時は欠損
        self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.filename = file.split('/')[-1].split('.')[0]
        self.MSMRange = [120, 150, 22.4, 47.6]

        # vars
        self.rain = self.getRain()
        self.sp = self.getSp()

    def getLatLon(self):
        lat, lon = self._returnConvertedLatLon()
        return lat, lon

    def getRain(self):
        r1h = self._convertVarsTo3hours(var='r1h')
        return r1h

    def getSp(self):
        sp = self._convertVarsTo3hours(var='sp')
        return sp

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

    def _convertVarsTo3hours(self, var):
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

    def makeNetcdfFile(self, path, lonList, latList, timeList, rainList, spList):
        nc = netCDF4.Dataset(path, "w", format="NETCDF4")
        nc.createDimension("lon", len(lonList))
        nc.createDimension("lat", len(latList))
        nc.createDimension("time", len(timeList))

        lon = nc.createVariable("lon", dtype('float32'), "lon")
        lon.long_name = 'longitude'
        lon.units = 'degrees_east'
        lon.standard_name = 'longitude'

        lat = nc.createVariable("lat", dtype('float32'), "lat")
        lat.long_name = 'latitude'
        lat.units = 'degrees_north'
        lat.standard_name = 'latitude'

        time = nc.createVariable("time", dtype('int16'), "time")
        time.long_name = 'time'
        time.unit = 'hours since {}'.format(self.filename)
        time.standard_name = 'time'

        rain = nc.createVariable("rain", dtype('int16'), ("time", "lat", "lon"))
        rain.scale_factor = 0.006116208155
        rain.add_offset = 200.0
        rain.long_name = 'rainfall in 1 hour'
        rain.units = 'mm/h'
        rain.standard_name = 'rainfall_rate'

        sp = nc.createVariable("sp", dtype('int16'), ("time", "lat", "lon"))
        sp.scale_factor = 0.9174311758
        sp.add_offset = 80000.0
        sp.long_name = 'surface air pressure'
        sp.units = 'Pa'
        sp.standard_name = 'surface_air_pressure'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        rain[:, :, :] = np.array(rainList)
        sp[:, :, :] = np.array(spList)
        nc.close()

    def drawMapByArray(self, v_array, v_lat, v_lon, t, path):
        super().drawMapByArray(v_array, v_lat, v_lon, t, path)