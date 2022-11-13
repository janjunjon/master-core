import os

from netCDF.ConvertedMSMs import ConvertedMSMs
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self, path) -> None:
        self.path = path
        self.saveDir = '/home/jjthomson/fdrive/nc/convertedMSMs'

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            startString = file[0]
            if startString == 's':
                filepath = '{}/{}'.format(self.path, file)
                nc = ConvertedMSMs(filepath)
                CreateNetCDF.createNcFileMSMs(
                    filename=file[1:9],
                    path='{}/{}'.format(self.saveDir, file[1:]),
                    lonList=nc.lon,
                    latList=nc.lat,
                    timeList=nc.time,
                    rainList=nc.rain,
                    pseaList=nc.psea,
                    spList=nc.sp,
                    uList=nc.u,
                    vList=nc.v,
                    tempList=nc.temp,
                    rhList=nc.rh,
                    ncld_upperList=nc.ncld_upper,
                    ncld_midList=nc.ncld_mid,
                    ncld_lowList=nc.ncld_low,
                    ncldList=nc.ncld,
                    dswrfList=nc.dswrf
                )