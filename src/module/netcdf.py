from itertools import accumulate
import netCDF4
import numpy as np
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

def mkBinary(filename, array):
    with open(filename, 'wb') as f:
        f.write(array)

def test():
    nc = read_netCDF('/home/jjthomson/fdrive/nc/s20200701.nc')
    r1h = convertMSMsTo3hours(nc)
    lat, lon = _returnConvertedLatLon(nc)
    draw.drawMapByArray(r1h, lat, lon, 0, "~/core/img/test.png")

def test2():
    nc = read_netCDF('/home/jjthomson/fdrive/nc/s20200701.nc')
    r1h = nc.variables['r1h']
    lat= nc.variables['lat']
    lon = nc.variables['lon']
    draw.drawMapByArray(r1h, lat, lon, 0, "~/core/img/test2.png")
    grads.execute_shell(
        '~/core/src/gs/draw_netcdf.gs',
        '/home/jjthomson/fdrive/nc/s20200701.nc',
        'test3.png'
    )

# --------------------------------------------------------------------------

def _convertMSMsResolutionByOneDimension(v_array):
    normal_array_with_time = []
    for v_time in v_array:
        normal_array = []
        for i in range(0, len(v_time), 2):
            for j in range(0, len(v_time[i]), 2):
                normal_array.append(v_time[i][j])
        normal_array_with_time.append(normal_array)
    return normal_array_with_time

def _convertArray(v_array):
    normal_array_with_time = []
    for v_time in v_array:
        normal_array = []
        for v_lat in v_time:
            normal_array.extend(v_lat)
        normal_array_with_time.append(normal_array)
    return normal_array_with_time

def _MSMp_to_binary(nc, var):
    # <class 'numpy.ma.core.MaskedArray'>
    # .data = <class 'numpy.ndarray'>
    # time(8) -> p(16) -> lat(253) -> lon(241)
    lon=nc.variables['lon'][:]
    lat=nc.variables['lat'][:]
    p=nc.variables['p'][:]
    time=nc.variables['time'][:]
    v=nc.variables[var][:][:][:][:]
    return

def _MSMs_to_binary(nc, var):
    # <class 'numpy.ma.core.MaskedArray'>
    # .data = <class 'numpy.ndarray'>
    # time(24) -> lat(505) -> lon(481)
    lon=nc.variables['lon'][:]
    lat=nc.variables['lat'][:]
    time=nc.variables['time'][:]
    v=nc.variables[var][:][:][:]
    nc.close()
    return
  