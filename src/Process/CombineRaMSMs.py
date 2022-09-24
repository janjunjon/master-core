from netCDF.NetCDF import NetCDF
import netCDF4
import os
import numpy as np
from numpy import dtype

class Execution:
    def __init__(self) -> None:
        self.nc_Ra = NetCDF('/home/jjthomson/fdrive/ra/ra.nc')
        self.nc_MSMs = NetCDF('/home/jjthomson/fdrive/nc/reversedMSMs.nc')
        self.rain_Ra = self.nc_Ra.variables['rain'][:][:][:].tolist()
        self.rain_MSMs = self.nc_MSMs.variables['rain'][:][:][:].tolist()
        self.lat = self.nc_Ra.variables['lat'][:].tolist()
        self.lon = self.nc_Ra.variables['lon'][:].tolist()
        self.time = range(0, 248)

    def main(self):
        self.makeNetcdfFile(
            path='/home/jjthomson/fdrive/rains.nc',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList1=self.rain_Ra,
            rainList2=self.rain_MSMs
        )

    def makeNetcdfFile(self, path, lonList, latList, timeList, rainList1, rainList2):
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

        rain_Ra = nc.createVariable("rain_Ra", dtype('int16'), ("time", "lat", "lon"))
        rain_Ra.scale_factor = 0.006116208155
        rain_Ra.add_offset = 200.0
        rain_Ra.long_name = 'RadarAmedas rain_fall in 1 hour'
        rain_Ra.units = 'mm/h'
        rain_Ra.standard_name = 'rainfall_rate'

        rain_MSMs = nc.createVariable("rain_MSMs", dtype('int16'), ("time", "lat", "lon"))
        rain_MSMs.scale_factor = 0.006116208155
        rain_MSMs.add_offset = 200.0
        rain_MSMs.long_name = 'MSMs rain_fall in 1 hour'
        rain_MSMs.units = 'mm/h'
        rain_MSMs.standard_name = 'rainfall_rate'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        rain_Ra[:, :, :] = np.array(rainList1)
        rain_MSMs[:, :, :] = np.array(rainList2)
        nc.close()