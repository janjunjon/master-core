from netCDF.NetCDF import NetCDF
import netCDF4
import numpy as np
from numpy import dtype
import os

from Module.CombineMSM import Combine

class Execution:
    def __init__(self) -> None:
        self.path = '/home/jjthomson/fdrive/nc/div'
        self.nc = netCDF4.Dataset('/home/jjthomson/fdrive/nc/data/p20200701.nc')
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.p = [
            1000.,  975.,  950.,  925.,  900.,  850.,  800.,  700.,  600.,  500.,  400.,  300.,  250.,  200.,  150.,  100.
        ]
        self.time = range(0, 248)
        self.vars = vars

    def main(self):
        W = Combine.combine(self.path, 'w')
        QU = Combine.combine(self.path, 'qu')
        QV = Combine.combine(self.path, 'qv')
        DIV = Combine.combine(self.path, 'div')
        