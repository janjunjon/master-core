import netCDF4
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

class NC:
    def __init__(self, file) -> None:
        self.nc = netCDF4.Dataset(file)
    
    def read_netCDF(self, filename):
        nc = netCDF4.Dataset(filename)
        return nc

    def config_netCDF(self, nc, var=None):
        if var == None:
            config = nc.dimensions
            # config = nc.variables.key()
        else:
            config = nc[var]
        return config

    def makeNetCDF(self, filename):
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

    def arrayToBinary(self, arr, path):
        nd_arr = np.array(arr)
        np.save(path, nd_arr)

    def drawMapByArray(self, v_array, v_lat, v_lon, t, path):
        var = np.array(v_array[t][:][:])
        La = np.array(v_lat)
        Lo = np.array(v_lon)
        Lon, Lat = np.meshgrid(Lo, La)
        fig = plt.figure(figsize=(10, 10))
        interval = list(np.arange(100, 300, 20))
        interval.insert(0, 0.1)
        cmap = cm.jet
        cmap.set_under('w', alpha=0)
        basemap = self._return_basemap()
        x, y = basemap(Lon, Lat)
        im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
        cb = basemap.colorbar(im, "right", size="2.5%")
        plt.show()
        plt.savefig(os.path.expanduser(path))
        plt.close()

    def _return_basemap():
        m=Basemap(
            projection='cyl',
            resolution='i',
            llcrnrlat=30,
            urcrnrlat=35,
            llcrnrlon=128,
            urcrnrlon=133
        )
        m.drawcoastlines(color='black')
        m.drawmeridians(np.arange(128,133,0.5))
        m.drawparallels(np.arange(30,35,0.5))
        return m