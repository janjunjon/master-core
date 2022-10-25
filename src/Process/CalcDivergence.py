import os
import netCDF4
import numpy as np
from numpy import dtype

from Module.CalcDivergence import Calculation

class Execution:
    def __init__(self) -> None:
        self.path_MSMp = '/home/jjthomson/fdrive/nc/data'
        self.path_ConvertedMSMs = '/home/jjthomson/fdrive/nc/converted'
        self.saveDir = '/home/jjthomson/fdrive/nc/div'

    def main(self):
        files = os.listdir(self.path_MSMp)
        for file in files:
            startString = file[0]
            if startString == 'p':
                filename_MSMp = '{}/{}'.format(self.path_MSMp, file)
                filename_ConvertedMSMs = '{}/{}'.format(self.path_ConvertedMSMs, file[1:])
                calc = Calculation(filename_MSMp, filename_ConvertedMSMs)
                calc.main()
                self.makeNetcdfFile(
                    filename=file[1:],
                    path='{}/{}'.format(self.saveDir, file[1:]),
                    lonList=calc.lon,
                    latList=calc.lat,
                    timeList=calc.time,
                    wList=calc.w,
                    quList=calc.qu,
                    qvList=calc.qv,
                    divList=calc.div
                )
        
    def makeNetcdfFile(self, filename, path, lonList, latList, timeList, wList, quList, qvList, divList):
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
        time.unit = 'hours since {}'.format(filename)
        time.standard_name = 'time'

        w = nc.createVariable("w", dtype('int16'), ("time", "lat", "lon"))
        w.long_name = 'precipitable water vaper'
        w.units = 'mm/h'
        w.standard_name = 'precipitable_water_vaper'

        qu = nc.createVariable("qu", dtype('int16'), ("time", "lat", "lon"))
        qu.long_name = 'specific humidity on u wind'
        qu.units = 'm/s/g'
        qu.standard_name = 'specific_humidity_u'

        qv = nc.createVariable("qv", dtype('int16'), ("time", "lat", "lon"))
        qv.long_name = 'specific humidity on v wind'
        qv.units = 'm/s/g'
        qv.standard_name = 'specific_humidity_v'

        div = nc.createVariable("div", dtype('int16'), ("time", "lat", "lon"))
        div.long_name = 'water vapor divergence'
        div.units = 'mm/h'
        div.standard_name = 'water_vapor_divergence'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        w[:, :, :] = np.array(wList)
        qu[:, :, :] = np.array(quList)
        qv[:, :, :] = np.array(qvList)
        div[:, :, :] = np.array(divList)
        nc.close()