import netCDF4
import numpy as np
from numpy import dtype

class CreateNetCDF:
    @classmethod
    def createNcFileMSMsOnlyRain(cls, path, lonList, latList, timeList, rainList):
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
        time.unit = 'hours since 2020-07-03 00:00:00+00:00'
        time.standard_name = 'time'

        rain = nc.createVariable("rain", dtype('int16'), ("time", "lat", "lon"))
        rain.scale_factor = 0.006116208155
        rain.add_offset = 200.0
        rain.long_name = 'rainfall in 1 hour'
        rain.units = 'mm/h'
        rain.standard_name = 'rainfall_rate'

        lon[:], lat[:], time[:], rain[:, :, :] = np.array(lonList), np.array(latList), np.array(timeList), np.array(rainList)
        nc.close()