import os
import netCDF4
import numpy as np
from numpy import dtype

from netCDF.AtmosIndex import *

class Execution:
    def __init__(self) -> None:
        self.path_MSMp = '/home/jjthomson/fdrive/nc/data'
        self.saveDir = '/home/jjthomson/fdrive/nc/atmos'

    def main(self):
        files = os.listdir(self.path_MSMp)
        for file in files:
            startString = file[0]
            if startString == 'p':
                path = '{}/{}'.format(self.path_MSMp, file)
                savePath = '{}/{}'.format(self.saveDir, file[1:])
                filename = file[1:9]
                nc = NetCDFAtmosIndex(path, savePath, filename)
                nc.main()