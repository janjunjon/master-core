import os
import netCDF4
import numpy as np
from numpy import dtype

from Module.CalcDivergence import Calculation
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self) -> None:
        self.path_ConvertedMSMp = '/home/jjthomson/fdrive/nc/convertedMSMp'
        self.path_ConvertedMSMs = '/home/jjthomson/fdrive/nc/convertedMSMs'
        self.saveDir = '/home/jjthomson/fdrive/nc/div'

    def main(self):
        files = os.listdir(self.path_ConvertedMSMp)
        for file in files:
            filename_MSMp = '{}/{}'.format(self.path_ConvertedMSMp, file)
            filename_ConvertedMSMs = '{}/{}'.format(self.path_ConvertedMSMs, file)
            calc = Calculation(filename_MSMp, filename_ConvertedMSMs)
            calc.main()
            CreateNetCDF.createNcFileDivergence(
                filename=file,
                path='{}/{}'.format(self.saveDir, file),
                lonList=calc.lon,
                latList=calc.lat,
                timeList=calc.time,
                pwvList=calc.pwv,
                quList=calc.qu,
                qvList=calc.qv,
                divList=calc.div
            )