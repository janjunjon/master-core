import time as Time
import numpy as np
from netCDF.NetCDF import NetCDF
from Module.Calculation import *
from Module.Reverse import *
from ML.Other.HeavyRainCases import *

class Eval:
    def __init__(self, dirPath, pattern) -> None:
        self.pattern = pattern
        self.dirPath = f'/home/jjthomson/fdrive/npy/{dirPath}'
        self.savePath = f'/home/jjthomson/fdrive/nc/predict/v3_eval/{dirPath}/{pattern}.txt'
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')
        self.nc_correct = NetCDF(f'/home/jjthomson/fdrive/nc/predict/v3/{dirPath}/{pattern}.nc')

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
            np.mean(self.RMSE1), [np.mean(self.FSS1[:,i]) for i in range(13)], np.mean(self.TS1),
            np.mean(self.RMSE2), [np.mean(self.FSS2[:,i]) for i in range(13)], np.mean(self.TS2),
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
            thresholds = np.append(np.linspace(2, 20, 10), [30,40,50])
            for threshold in thresholds:
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
        RMSE = np.load('/home/jjthomson/fdrive/npy/RMSE.npy')
        FSS = np.load('/home/jjthomson/fdrive/npy/FSS.npy')
        TS  = np.load('/home/jjthomson/fdrive/npy/TS.npy')
        return RMSE, FSS, TS

    def save(self):
        np.save(f'{self.dirPath}/RMSE_{self.pattern}', self.RMSE2)
        np.save(f'{self.dirPath}/FSS_{self.pattern}', self.FSS2)
        np.save(f'{self.dirPath}/TS_{self.pattern}', self.TS2)

class EvalRAMSMs:
    def __init__(self) -> None:
        self.savePath = f'/home/jjthomson/fdrive/npy/RA_MSMs.txt'
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')

    def main(self):
        starttime = Time.time()

        self.RMSE, self.FSS, self.TS = self.calcEvalIndex_RA_MSMs()
        self.save()
        text = f"""
        <RA-MSMs>
        RMSE: {'{:.6f}'.format(self.RMSE[0])}
        FSS: {[float('{:.6f}'.format(self.FSS[0][i])) for i in range(13)]}
        TS: {'{:.6f}'.format(self.TS[0])}
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
            thresholds = np.append(np.linspace(2, 20, 10), [30,40,50])
            for threshold in thresholds:
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
        np.save('/home/jjthomson/fdrive/npy/RMSE', self.RMSE)
        np.save('/home/jjthomson/fdrive/npy/FSS', self.FSS)
        np.save('/home/jjthomson/fdrive/npy/TS', self.TS)

class EvalSpecificRegions(Eval):
    """
    regions: [56, 106, 64, 104]
    """
    def __init__(self, dirPath, pattern, regions=None) -> None:
        super().__init__(dirPath, pattern)
        self.time = 23
        self.regions = [76, 116, 64, 104]
        self.indexes = case202007040100()
        self.dirPath = f'/home/jjthomson/fdrive/npy2/{dirPath}'
        self.savePath = f'/home/jjthomson/fdrive/nc/predict/v3_eval2/{dirPath}/{pattern}.txt'
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')
        self.nc_correct = NetCDF(f'/home/jjthomson/fdrive/nc/predict/v3/{dirPath}/{pattern}.nc')

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
            '{:.6f}'.format(self.RMSE1[0]), [float('{:.6f}'.format(self.FSS1[0][i])) for i in range(13)], '{:.6f}'.format(self.TS1[0]),
            '{:.6f}'.format(self.RMSE2[0]), [float('{:.6f}'.format(self.FSS2[0][i])) for i in range(13)], '{:.6f}'.format(self.TS2[0]),
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
        time = self.time
        real = self.nc_rains.variables['rain_Ra'][time]
        correct = self.nc_correct.variables['rain'][time]
        FSSEACH = []
        rain = Reverse.reverseLat(correct)
        thresholds = np.append(np.linspace(2, 20, 10), [30,40,50])
        for threshold in thresholds:
            FSS = Calculation.FSS_(
                threshold=threshold, real=real, pred=rain,
                LATs=self.regions[0], LATf=self.regions[1],
                LONs=self.regions[2], LONf=self.regions[3]
            )
            FSSEACH.append(FSS)
        TS = Calculation.ThreatScore(
            real=real, pred=rain, indexes=self.indexes
        )
        RMSE = Calculation.RMSE(
            real=real, pred=rain, indexes=self.indexes
        )
        ALL1.append(RMSE)
        ALL2.append(FSSEACH)
        ALL3.append(TS)
        print(f'time: {time}')
        return ALL1, ALL2, ALL3

    def calcEvalIndex_RA_MSMs(self):
        RMSE = np.load('/home/jjthomson/fdrive/npy2/RMSE.npy')
        FSS = np.load('/home/jjthomson/fdrive/npy2/FSS.npy')
        TS  = np.load('/home/jjthomson/fdrive/npy2/TS.npy')
        return RMSE, FSS, TS

    def save(self):
        np.save(f'{self.dirPath}/RMSE_{self.pattern}', self.RMSE2)
        np.save(f'{self.dirPath}/FSS_{self.pattern}', self.FSS2)
        np.save(f'{self.dirPath}/TS_{self.pattern}', self.TS2)

class EvalRAMSMsSpecificRegions(EvalRAMSMs):
    def __init__(self) -> None:
        self.savePath = f'/home/jjthomson/fdrive/npy2/RA_MSMs.txt'
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains_nomask.nc')
        self.time = 23
        self.regions = [56, 106, 64, 104]
        self.indexes = case202007040100()

    def main(self):
        starttime = Time.time()

        self.RMSE, self.FSS, self.TS = self.calcEvalIndex_RA_MSMs()
        self.save()
        text = f"""
        <RA-MSMs>
        RMSE: {'{:.6f}'.format(self.RMSE[0])}
        FSS: {[float('{:.6f}'.format(self.FSS[0][i])) for i in range(13)]}
        TS: {'{:.6f}'.format(self.TS[0])}
        """
        with open(self.savePath, 'w') as f:
            f.write(text)

        elapsedtime = Time.time() - starttime
        print ("Elapsed time to calculate Evaluation Indexes: {0} [sec]".format(elapsedtime))

    def calcEvalIndex_RA_MSMs(self):
        ALL1 = []
        ALL2 = []
        ALL3 = []
        time = self.time
        real = self.nc_rains.variables['rain_Ra'][time]
        correct = self.nc_rains.variables['rain_MSMs'][time]
        FSSEACH = []
        thresholds = np.append(np.linspace(2, 20, 10), [30,40,50])
        for threshold in thresholds:
            FSS = Calculation.FSS_(
                threshold=threshold, real=real, pred=correct,
                LATs=self.regions[0], LATf=self.regions[1],
                LONs=self.regions[2], LONf=self.regions[3]
            )
            FSSEACH.append(FSS)
        TS = Calculation.ThreatScore(
            real=real, pred=correct, indexes=self.indexes
        )
        RMSE = Calculation.RMSE(
            real=real, pred=correct, indexes=self.indexes
        )
        ALL1.append(RMSE)
        ALL2.append(FSSEACH)
        ALL3.append(TS)
        print(f'time: {time}')
        return ALL1, ALL2, ALL3

    def save(self):
        np.save('/home/jjthomson/fdrive/npy2/RMSE', self.RMSE)
        np.save('/home/jjthomson/fdrive/npy2/FSS', self.FSS)
        np.save('/home/jjthomson/fdrive/npy2/TS', self.TS)