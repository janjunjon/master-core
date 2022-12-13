import time as Time
import numpy as np
from netCDF.NetCDF import NetCDF
from Module.Calculation import *
from Module.Reverse import *
from ML.Other.HeavyRainCases import *

class Eval:
    def __init__(self, dirPath, pattern) -> None:
        self.pattern = pattern
        self.dirPath = f'/home/ishihara/fdrive/npy/{dirPath}'
        self.savePath = f'/home/ishihara/fdrive/nc/predict/v3_eval/{dirPath}/{pattern}.txt'
        self.nc_rains = NetCDF('/home/ishihara/fdrive/nc/combined/rains_nomask.nc')
        self.nc_correct = NetCDF(f'/home/ishihara/fdrive/nc/predict/v3/{dirPath}/{pattern}.nc')

    def main(self):
        starttime = Time.time()

        self.RMSE1, self.FSS1, self.TS1 = self.calcEvalIndex_RA_MSMs()
        self.RMSE2, self.FSS2, self.TS2 = self.calcEvalIndex_Real_Correct()
        self.save()
        self.value1 = Calculation.welchT(self.RMSE1, self.RMSE2)
        self.FSS1, self.FSS2 = np.array(self.FSS1), np.array(self.FSS2)
        self.value2 = [Calculation.welchT(self.FSS1[:,i], self.FSS2[:,i]) for i in range(10)]
        self.value3 = Calculation.welchT(self.TS1, self.TS2)
        text = """
        <tkentei>
        tRMSE: {}
        tTS: {}

        """.format(self.value1, self.value3)
        for i, value in enumerate(self.value2):
            text += """
            tFSS_{}: {}
            """.format(i, value)
        text += """
        <RA-MSMs>
        RMSE: {}
        FSS: {}
        TS: {}

        <RA-Correct>
        RMSE: {}
        FSS: {}
        TS: {}
        """.format(
            np.mean(self.RMSE1), ['{:.4f}'.format(np.mean(self.FSS1[:,i])) for i in range(10)], np.mean(self.TS1),
            np.mean(self.RMSE2), ['{:.4f}'.format(np.mean(self.FSS2[:,i])) for i in range(10)], np.mean(self.TS2),
        )
        with open(self.savePath, 'w') as f:
            f.write(text)

        elapsedtime = Time.time() - starttime
        print ("Elapsed time to calculate Evaluation Indexes: {0} [sec]".format(elapsedtime))

    def calcEvalIndex_Real_Correct(self):
        """
        FSS[248][10]
        """
        ALL1 = []
        ALL2 = []
        ALL3 = []
        real = self.nc_rains.variables['rain_Ra'][:]
        correct = self.nc_correct.variables['rain'][:]
        for time in range(248):
            FSSEACH = []
            rain = Reverse.reverseLat(correct[time])
            for threshold in np.linspace(2, 20, 10):
                FSS = Calculation.FSS_(threshold=threshold, real=real[time], pred=rain)
                FSSEACH.append(FSS)
            TS = Calculation.ThreatScore(real=real[time], pred=rain)
            RMSE = Calculation.RMSE(real=real[time], pred=rain)
            ALL1.append(RMSE)
            ALL2.append(FSSEACH)
            ALL3.append(TS)
            print(f'time: {time}')
        return ALL1, ALL2, ALL3

    def calcEvalIndex_RA_MSMs(self):
        RMSE = np.load('/home/ishihara/fdrive/npy/RMSE.npy')
        FSS = np.load('/home/ishihara/fdrive/npy/FSS.npy')
        TS  = np.load('/home/ishihara/fdrive/npy/TS.npy')
        return RMSE, FSS, TS

    def save(self):
        np.save(f'{self.dirPath}/RMSE_{self.pattern}', self.RMSE2)
        np.save(f'{self.dirPath}/FSS_{self.pattern}', self.FSS2)
        np.save(f'{self.dirPath}/TS_{self.pattern}', self.TS2)

class EvalRAMSMs:
    def __init__(self) -> None:
        self.savePath = f'/home/ishihara/fdrive/npy/RA_MSMs.txt'
        self.nc_rains = NetCDF('/home/ishihara/fdrive/nc/combined/rains_nomask.nc')

    def main(self):
        starttime = Time.time()

        self.RMSE, self.FSS, self.TS = self.calcEvalIndex_RA_MSMs()
        self.save()
        text = f"""
        <RA-MSMs>
        RMSE: {np.mean(self.RMSE)}
        FSS: {np.mean(self.FSS)}
        TS: {np.mean(self.TS)}
        """
        with open(self.savePath, 'w') as f:
            f.write(text)

        elapsedtime = Time.time() - starttime
        print ("Elapsed time to calculate Evaluation Indexes: {0} [sec]".format(elapsedtime))

    def calcEvalIndex_RA_MSMs(self):
        ALL1 = []
        ALL2 = []
        ALL3 = []
        rain_Ra = self.nc_rains.variables['rain_Ra'][:]
        rain_MSMs = self.nc_rains.variables['rain_MSMs'][:]
        for time in range(248):
            FSSEACH = []
            for threshold in np.linspace(2, 20, 10):
                FSS = Calculation.FSS_(threshold=threshold, real=rain_Ra[time], pred=rain_MSMs[time])
                FSSEACH.append(FSS)
            TS = Calculation.ThreatScore(real=rain_Ra[time], pred=rain_MSMs[time])
            RMSE = Calculation.RMSE(real=rain_Ra[time], pred=rain_MSMs[time])
            ALL1.append(RMSE)
            ALL2.append(FSSEACH)
            ALL3.append(TS)
            print(f'time: {time}')
        return ALL1, ALL2, ALL3

    def save(self):
        np.save('/home/ishihara/fdrive/npy/RMSE', self.RMSE)
        np.save('/home/ishihara/fdrive/npy/FSS', self.FSS)
        np.save('/home/ishihara/fdrive/npy/TS', self.TS)