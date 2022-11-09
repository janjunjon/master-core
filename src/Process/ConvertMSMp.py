import os

from netCDF.MSMp import *
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self, path) -> None:
        self.path = path
        self.saveDir = '/home/jjthomson/fdrive/nc/convertedMSMp'

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            startString = file[0]
            if startString == 'p':
                filepath = '{}/{}'.format(self.path, file)
                nc = MSMp(filepath)
                CreateNetCDF.createNcFileMSMp(
                    filename=file[1:9],
                    path='{}/{}'.format(self.saveDir, file[1:]),
                    lonList=nc.lon,
                    latList=nc.lat,
                    pList=nc.p,
                    timeList=nc.time,
                    zList=nc.z,
                    wList=nc.w,
                    uList=nc.u,
                    vList=nc.v,
                    tempList=nc.temp,
                    rhList=nc.rh
                )