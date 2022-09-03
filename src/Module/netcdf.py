import netCDF4
import numpy as np
from numpy import dtype
from . import draw, grads

def read_netCDF(filename):
    nc = netCDF4.Dataset(filename)
    return nc

def config_netCDF(nc, var=None):
    if var == None:
        config = nc.dimensions
        # config = nc.variables.key()
    else:
        config = nc[var]
    return config

def _convertMSMsResolution(v_array):
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

def _returnConvertedLatLon(nc):
    lat = nc.variables['lat'][:].tolist()
    lon = nc.variables['lon'][:].tolist()
    convertedLat = []
    convertedLon = []
    for i in range(0, len(lat), 2):
        convertedLat.append(lat[i])
    for j in range(0, len(lon), 2):
        convertedLon.append(lon[j])
    return [convertedLat, convertedLon]

def _convertMSMsTo3hours(nc, var='r1h'):
    v_array = nc.variables[var][:][:][:].tolist()
    normal_array_with_time = _convertMSMsResolution(v_array)
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

def _convertMSMsWithNoAcumulation(nc, var='r1h'):
    v_array = nc.variables[var][:][:][:].tolist()
    normal_array_with_time = _convertMSMsResolution(v_array)
    accumulate3hours = []
    for i in range(0, 24, 3):
        lat_a = []
        for j in range(0, 253):
            lon_a = []
            for k in range(0, 241):
                lon_a.append(
                    normal_array_with_time[i][j][k]
                )
            lat_a.append(lon_a)
        accumulate3hours.append(lat_a)
    return accumulate3hours

def test():
    nc = read_netCDF('/home/jjthomson/fdrive/nc/data/s20200703.nc')
    lat, lon = _returnConvertedLatLon(nc)
    r1h = _convertMSMsWithNoAcumulation(nc)
    path = '/home/jjthomson/fdrive/nc/conveted/test2.nc'
    makeNetcdfFile(path, lon, lat, range(1, 25, 3), r1h)

def makeNetcdfFile(path, lonList, latList, timeList, rainList):
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

    rain = nc.createVariable("rain", dtype('float32'), ("time", "lat", "lon"))
    rain.scale_factor = 0.006116208155
    rain.add_offset = 200.0
    rain.long_name = 'rainfall in 1 hour'
    rain.units = 'mm/h'
    rain.standard_name = 'rainfall_rate'

    lon[:], lat[:], time[:], rain[:, :, :] = np.array(lonList), np.array(latList), np.array(timeList), np.array(rainList)
    nc.close()

def arrayToBinary(arr, path):
    nd_arr = np.array(arr)
    np.save(path, nd_arr)
