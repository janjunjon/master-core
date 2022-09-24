from netCDF.NetCDF import NetCDF
import netCDF4
import numpy as np
from numpy import dtype
import os

class Execution:
    def __init__(self) -> None:
        self.path = '/home/jjthomson/fdrive/nc/data'
        self.nc = netCDF4.Dataset('/home/jjthomson/fdrive/nc/data/p20200701.nc')
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lat.reverse()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.time = range(0, 248)

    def main(self):
        wList, uList, vList, tempList, rhList = self.conbineMSMpLowLoad()
        self.makeNetcdfFileLowLoad(
            path='/home/jjthomson/fdrive/nc/LowLoadMSMp.nc',
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            wList=wList,
            uList=uList,
            vList=vList,
            tempList=tempList,
            rhList=rhList
        )

    def reverseVar(self, varArray):
        # time -> lat -> lon
        for var in varArray:
            var.reverse()

    def conbineMSMpLowLoad(self):
        files = []
        for file in os.listdir(self.path):
            if file[0] == 'p':
                files.append(file)
        print(files)
        wList = []
        uList = []
        vList = [] 
        tempList = []
        rhList = []
        for file in files:
            nc = NetCDF('{}/{}'.format(self.path, file))
            w = nc.variables['w'][:][:][:][:].tolist()
            u = nc.variables['u'][:][:][:][:].tolist()
            v = nc.variables['v'][:][:][:][:].tolist()
            temp = nc.variables['temp'][:][:][:][:].tolist()
            rh = nc.variables['rh'][:][:][:][:].tolist()
            if file == 'p20200630.nc':
                for i in [5,6,7]:
                    wList.append(w[i][0][:][:])
                    uList.append(u[i][0][:][:])
                    vList.append(v[i][0][:][:])
                    tempList.append(temp[i][0][:][:])
                    rhList.append(rh[i][0][:][:])
            elif file == 'p20200731.nc':
                for i in [0,1,2,3,4]:
                    wList.append(w[i][0][:][:])
                    uList.append(u[i][0][:][:])
                    vList.append(v[i][0][:][:])
                    tempList.append(temp[i][0][:][:])
                    rhList.append(rh[i][0][:][:])
            else:
                for i in range(0,8):
                    wList.append(w[i][0][:][:])
                    uList.append(u[i][0][:][:])
                    vList.append(v[i][0][:][:])
                    tempList.append(temp[i][0][:][:])
                    rhList.append(rh[i][0][:][:])
            print(file)
        self.reverseVar(wList)
        self.reverseVar(uList)
        self.reverseVar(vList)
        self.reverseVar(tempList)
        self.reverseVar(rhList)
        return wList, uList, vList, tempList, rhList

    def makeNetcdfFileLowLoad(self, path, lonList, latList, timeList, wList, uList, vList, tempList, rhList):
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
        time.unit = 'hours since 2020-07-03 00:00:00+00:00'
        time.standard_name = 'time'

        w = nc.createVariable("w", dtype('float64'), ("time", "lat", "lon"))
        w.long_name = 'vertical velocity in p'
        w.units = 'Pa/s'
        w.standard_name = 'lagrangian_tendency_of_air_pressure'

        u = nc.createVariable("u", dtype('int16'), ("time", "lat", "lon"))
        u.scale_factor = 0.006116208155
        u.add_offset = 0.0
        u.long_name = 'eastward component of wind'
        u.units = 'm/s'
        u.standard_name = 'eastward_wind'

        v = nc.createVariable("v", dtype('int16'), ("time", "lat", "lon"))
        v.scale_factor = 0.006116208155
        v.add_offset = 0.0
        v.long_name = 'northward component of wind'
        v.units = 'm/s'
        v.standard_name = 'northward_wind'

        temp = nc.createVariable("temp", dtype('int16'), ("time", "lat", "lon"))
        temp.scale_factor = 0.002613491379
        temp.add_offset = 255.4004974
        temp.long_name = 'temperature'
        temp.units = 'K'
        temp.standard_name = 'air_temperature'

        rh = nc.createVariable("rh", dtype('int16'), ("time", "lat", "lon"))
        rh.scale_factor = 0.002293577883
        rh.add_offset = 75.0
        rh.long_name = 'relative humidity'
        rh.units = '%'
        rh.standard_name = 'relative_humidity'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        w[:, :, :] = np.array(wList)
        u[:, :, :] = np.array(uList)
        v[:, :, :] = np.array(vList)
        temp[:, :, :] = np.array(tempList)
        rh[:, :, :] = np.array(rhList)
        nc.close()