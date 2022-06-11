import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

# in case of HDF
# import h5py
# h5='GPMMRG_MAP_1702010000_H_L3S_MCH_04B.h5'

# with h5py.File(h5,"r") as infile: 
#     Lat=np.array(infile['Grid'+'/Latitude']) 
#     Lon=np.array(infile['Grid'+'/Longitude'])
#     hprecipRateGC=np.array(infile['Grid'+'/hourlyPrecipRateGC'])
# '''
# in case of netCDF
import netCDF4
nc=netCDF4.Dataset('GPMMRG_MAP_1702010000_H_L3S_MCN_04A.nc','r')
Lon=nc.variables['Longitude'][:]
Lat=nc.variables['Latitude'][:]
hprecipRateGC=nc.variables['hourlyPrecipRateGC'][:]
nc.close()

# in case of binary
import gzip
import struct
filename='gsmap_gauge.20170201.0000.v6.4133.0.dat.gz'
i=0
rain=[0]*3600*1200
with gzip.open(filename, "rb") as f:
    while True:
        data=f.read(4)
        if data=="":
            break
        rain[i]=struct.unpack('f',data)[0]
        i=i+1
hprecipRateGC=np.reshape(rain, (1200,3600))
# generate meshgrid because GSMaP binary does not contain lacations
lo=[5+10*i for i in range(0,1800)]
lo.extend([-17995+10*i for i in range(0,1800)])
Lo=0.01*np.array(lo)
la=[5995-10*i for i in range(0,600)]
la.extend([-5-10*i for i in range(0,600)])
La= 0.01*np.array(la)
Lon,Lat=np.meshgrid(Lo,La)
# end of binary case

#plot with Matplotlib
fig=plt.figure(figsize=(20,20))
# set the color interval
interval=list(np.arange(1,30,1)) 
interval.insert(0,0.1)
#set colormap
cmap=cm.jet
cmap.set_under('w', alpha=0)

#set map
m=Basemap(projection='cyl',
         resolution='c',
         llcrnrlat=-65, urcrnrlat=65, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines(color='black')
m.drawmeridians(np.arange(0,360,30))
m.drawparallels(np.arange(-90,90,30))
x,y=m(Lon, Lat) #compute map projection
im=plt.contourf(x,y,hprecipRateGC, interval, cmap=cmap, latlon=True) 
# set colorbar
cb=m.colorbar(im, "right", size="2.5%")

plt.show()
plt.close()
