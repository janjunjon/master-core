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
    for i in range(0, 24, 1):
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
    draw.drawMapByArray(r1h, lat, lon, 0, '/home/jjthomson/master-core/img/test_MSMs20200703.png')

def makeNetCDF(filename):
    nc = netCDF4.Dataset('filename.nc', 'w', format='NETCDF3_CLASSIC')
    nc.createDimension('ntime', len(time_out))
    nc.createDimension('xi', x)
    nc.createDimension('eta', y)

    time = nc.createVariable('time', dtype('int32').char, ('ntime',))
    time.long_name = 'time of test variable'
    time.units = 'days since 1968-05-23 00:00:00'

    lon = nc.createVariable('lon', dtype('double').char, ('eta', 'xi'))
    lon.long_name = 'east longitude'
    lon.units = 'degree of east longitude'

    lat = nc.createVariable('lat', dtype('double').char, ('eta', 'xi'))
    lat.long_name = 'north latitude'
    lat.units = 'degree of north latitude'

    var = nc.createVariable('varname', dtype('double').char, ('ntime', 'eta', 'xi'))
    var.long_name = 'test variable'
    var.units = 'unit of test variable'

    time[:] = time_out
    lon[:,:] = lon_out
    lat[:,:] = lat_out
    var[:,:,:] = var_out

    nc.close()

def arrayToBinary(arr, path):
    nd_arr = np.array(arr)
    np.save(path, nd_arr)
