import netCDF4
import numpy as np
from numpy import dtype
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

class NetCDF:
    def __init__(self, path) -> None:
        self.nc = netCDF4.Dataset(path)
        self.dimensions = self.nc.dimensions
        self.variables = self.nc.variables
        self.filename = path.split('/')[-1].split('.')[0]
        self.MSMRange = [120, 150, 22.4, 47.6]
    
    @property
    def lat(self):
        return self.nc.variables['lat'][:].tolist()
    
    @property
    def lon(self):
        return self.nc.variables['lon'][:].tolist()
    
    @property
    def time(self):
        return self.nc.variables['time'][:].tolist()

    def arrayToBinary(self, arr, path):
        nd_arr = np.array(arr)
        np.save(path, nd_arr)

    def drawMapByArray(self, v_array, v_lat, v_lon, t, path):
        var = np.array(v_array[t][:][:])
        La = np.array(v_lat)
        Lo = np.array(v_lon)
        Lon, Lat = np.meshgrid(Lo, La)
        fig = plt.figure(figsize=(10, 10))
        interval = list(np.arange(10, 100, 10))
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

    def _return_basemap(self):
        llcrnrlon, urcrnrlon, llcrnrlat, urcrnrlat = self.MSMRange
        m=Basemap(
            projection='cyl',
            resolution='i',
            llcrnrlat=llcrnrlat,
            urcrnrlat=urcrnrlat,
            llcrnrlon=llcrnrlon,
            urcrnrlon=urcrnrlon
        )
        m.drawcoastlines(color='black')
        # m.drawmeridians(np.arange(128,133,0.5))
        # m.drawparallels(np.arange(30,35,0.5))
        return m