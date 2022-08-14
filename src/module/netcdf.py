from itertools import accumulate
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

def convertMSMsResolution(v_array):
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

def convertMSMsTo3hours(nc, var='r1h'):
    v_array = nc.variables[var][:][:][:].tolist()
    normal_array_with_time = convertMSMsResolution(v_array)
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

def makeNetCDF():

    # オブジェクトを作成し，各次元数を設定します．

    nc = netCDF4.Dataset('filename.nc', 'w', format='NETCDF3_CLASSIC')
    nc.createDimension('ntime', len(time_out))  # e.g. time_out = [0, 1, ...]
    # nc.createDimensions('ntime', None)        # unlimitedにする場合
    nc.createDimension('xi', x)                 # e.g. x = 10
    nc.createDimension('eta', y)                # e.g. y = 10

    # その後，各変数を定義します．
    # 以下の例では，時間，緯度，経度，3次元変数を定義します．

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

    # 最後に，予め np.ndarray 等で作成しておいた値を代入します．

    time[:] = time_out
    lon[:,:] = lon_out
    lat[:,:] = lat_out
    var[:,:,:] = var_out

    nc.close()