import os
import netCDF4
import numpy as np
from numpy import dtype

from Module.CalcDivergence import Calculation
from Module.CreateNetCDF import CreateNetCDF

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
                CreateNetCDF.createNcFileDivergence(
                    filename=file[1:],
                    path='{}/{}'.format(self.saveDir, file[1:]),
                    lonList=calc.lon,
                    latList=calc.lat,
                    timeList=calc.time,
                    pwvList=calc.pwv,
                    quList=calc.qu,
                    qvList=calc.qv,
                    divList=calc.div
                )