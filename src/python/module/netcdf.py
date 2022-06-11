from itertools import accumulate
import netCDF4
import numpy as np

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

def mkBinaryMSMs(nc, var='r1h'):
    v_array = nc.variables[var][:][:][:].tolist()
    normal_array_with_time = []
    accumulate3hours = []
    for v_time in v_array:
        normal_array = []
        for v_lat in v_time:
            normal_array.extend(v_lat)
        normal_array_with_time.append(normal_array)
    for i in range(0, 24, 3):
        sum3hours = [
            x + y + z for (x, y, z) in zip(
                normal_array_with_time[i],
                normal_array_with_time[i+1],
                normal_array_with_time[i+2]
            )
        ]
        accumulate3hours.append(sum3hours)
    return accumulate3hours   

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
  