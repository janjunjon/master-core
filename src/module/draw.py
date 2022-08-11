import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from mpl_toolkits.basemap import Basemap
import os

def drawMapByNC(nc, v):
    var = np.array(nc[v][0][:][:])
    Lo = np.array(nc['lon'])
    La = np.array(nc['lat'])
    Lon, Lat = np.meshgrid(Lo, La)
    fig = plt.figure(figsize=(10, 10))
    interval = list(np.arange(200, 300, 10))
    interval.insert(0, 0.1)
    cmap = cm.jet
    cmap.set_under('w', alpha=0)
    basemap = return_basemap()
    x, y = basemap(Lon, Lat)
    im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
    cb = basemap.colorbar(im, "right", size="2.5%")
    plt.show()
    plt.savefig("./img/test.png")
    plt.close()

def drawMapByArray(v_array, v_lat, v_lon, t, path):
    var = np.array(v_array[t][:][:])
    La = np.array(v_lat)
    Lo = np.array(v_lon)
    Lon, Lat = np.meshgrid(Lo, La)
    fig = plt.figure(figsize=(10, 10))
    interval = list(np.arange(100, 300, 20))
    interval.insert(0, 0.1)
    cmap = cm.jet
    cmap.set_under('w', alpha=0)
    basemap = return_basemap()
    x, y = basemap(Lon, Lat)
    im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
    cb = basemap.colorbar(im, "right", size="2.5%")
    plt.show()
    plt.savefig(os.path.expanduser(path))
    plt.close()   

def return_basemap():
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