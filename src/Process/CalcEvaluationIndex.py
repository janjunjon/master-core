import time as Time
import numpy as np
from netCDF.NetCDF import NetCDF
from Module.Calculation import *

class Execution:
    def __init__(self) -> None:
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')
        self.nc_correct = NetCDF('/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern1.nc')

    def main(self):
        starttime = Time.time()

        RMSE1, FSS1, TS1 = self.calcEvalIndex_RA_MSMs()
        RMSE2, FSS2, TS2 = self.calcEvalIndex_Real_Correct()
        value1 = Calculation.welchT(RMSE1, RMSE2)
        value2 = Calculation.welchT(FSS1, FSS2)
        value3 = Calculation.welchT(TS1, TS2)
        self.RMSE1, self.RMSE2, self.FSS1, self.FSS2, self.TS1, self.TS2 = RMSE1, RMSE2, FSS1, FSS2, TS1, TS2
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        print(value1, value2, value3)

        elapsedtime = Time.time() - starttime
        print ("Elapsed time to calculate Evaluation Indexes: {0} [sec]".format(elapsedtime))

    def debug(self):
        time = 0
        real = self.nc_rains.variables['rain_Ra'][:]
        correct = self.nc_correct.variables['rain'][:]
        FSS = Calculation.FSS_(threshold=2, real=real[time], pred=correct[time])
        print(FSS)
        self.FSS = FSS

    def calcEvalIndex_Real_Correct(self):
        ALL1 = []
        ALL2 = []
        ALL3 = []
        real = self.nc_rains.variables['rain_Ra'][:]
        correct = self.nc_correct.variables['rain'][:]
        for time in range(248):
            FSS = Calculation.FSS_(threshold=2, real=real[time], pred=correct[time])
            TS = Calculation.ThreatScore(real=real[time], pred=correct[time])
            rain1 = np.ravel(real[time])
            rain2 = np.ravel(correct[time])
            RMSE = Calculation.calcRMSE(rain1, rain2)
            ALL1.append(RMSE)
            ALL2.append(FSS)
            ALL3.append(TS)
        return ALL1, ALL2, ALL3

    def calcEvalIndex_RA_MSMs(self):
        ALL1 = []
        ALL2 = []
        ALL3 = []
        rain_Ra = self.nc_rains.variables['rain_Ra'][:]
        rain_MSMs = self.nc_rains.variables['rain_MSMs'][:]
        for time in range(248):
            FSS = Calculation.FSS_(threshold=2, real=rain_Ra[time], pred=rain_MSMs[time])
            TS = Calculation.ThreatScore(real=rain_Ra[time], pred=rain_MSMs[time])
            rain1 = np.ravel(rain_Ra[time])
            rain2 = np.ravel(rain_MSMs[time])
            RMSE = Calculation.calcRMSE(rain1, rain2)
            ALL1.append(RMSE)
            ALL2.append(FSS)
            ALL3.append(TS)
        return ALL1, ALL2, ALL3
