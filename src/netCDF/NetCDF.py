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

    def makeNetcdfFile(self, path, lonList, latList, timeList, rainList):
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
        time.unit = 'hours since {}'.format(self.filename)
        time.standard_name = 'time'

        rain = nc.createVariable("rain", dtype('float32'), ("time", "lat", "lon"))
        rain.scale_factor = 0.006116208155
        rain.add_offset = 200.0
        rain.long_name = 'rainfall in 1 hour'
        rain.units = 'mm/h'
        rain.standard_name = 'rainfall_rate'

        lon[:], lat[:], time[:], rain[:, :, :] = np.array(lonList), np.array(latList), np.array(timeList), np.array(rainList)
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