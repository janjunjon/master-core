import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

class Draw:
    def drawMapByNC(self, nc, v):
        var = np.array(nc[v][0][:][:])
        Lo = np.array(nc['lon'])
        La = np.array(nc['lat'])
        Lon, Lat = np.meshgrid(Lo, La)
        fig = plt.figure(figsize=(10, 10))
        interval = list(np.arange(200, 300, 10))
        interval.insert(0, 0.1)
        cmap = cm.jet
        cmap.set_under('w', alpha=0)
        basemap = self.return_basemap()
        x, y = basemap(Lon, Lat)
        im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
        cb = basemap.colorbar(im, "right", size="2.5%")
        plt.show()
        plt.savefig("./img/test.png")
        plt.close()

    def drawMapByArray(self, v_array, v_lat, v_lon, t, path, region):
        var = np.array(v_array[t][:][:])
        La = np.array(v_lat)
        Lo = np.array(v_lon)
        Lon, Lat = np.meshgrid(Lo, La)
        fig = plt.figure(figsize=(10, 10))
        plt.rcParams['font.size'] = 16
        interval = list(np.arange(0, 65, 5))
        cmap = cm.jet
        cmap.set_under('w', alpha=0)
        basemap = self.return_basemap(region)
        x, y = basemap(Lon, Lat)
        im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
        cb = basemap.colorbar(im, "right", size="2.5%")
        plt.show()
        plt.savefig(os.path.expanduser(path))
        plt.close()

    def drawMapByArrayNotMultidimensional(self, v_array, v_lat, v_lon, path, region):
        var = np.array(v_array)
        La = np.array(v_lat)
        Lo = np.array(v_lon)
        Lon, Lat = np.meshgrid(Lo, La)
        fig = plt.figure(figsize=(10, 10))
        plt.rcParams['font.size'] = 16
        interval = list(np.arange(0, 65, 5))
        cmap = cm.jet
        cmap.set_under('w', alpha=0)
        basemap = self.return_basemap(region)
        x, y = basemap(Lon, Lat)
        im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
        cb = basemap.colorbar(im, "right", size="2.5%")
        plt.show()
        plt.savefig(os.path.expanduser(path))
        plt.close()

    def return_basemap(self, region):
        m=Basemap(
            projection='cyl',
            resolution='i',
            llcrnrlat=region[0],
            urcrnrlat=region[1],
            llcrnrlon=region[2],
            urcrnrlon=region[3]
        )
        m.drawcoastlines(color='black')
        # m.drawmeridians(np.arange(128,133,0.5))
        # m.drawparallels(np.arange(30,35,0.5))
        return m