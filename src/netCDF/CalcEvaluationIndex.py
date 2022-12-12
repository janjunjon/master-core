import time as Time
import numpy as np
from netCDF.NetCDF import NetCDF
from Module.Calculation import *

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
        tRMSE: {:.4f}
        tTS: {:.4f}

        """.format(
            self.value1, self.value3
        )
        for i, value in enumerate(self.value2):
            text += """
            tFSS_{:.4f}: {:.4f}
            """.format(i, value)
        text += f"""
        <RA-MSMs>
        RMSE: {np.mean(self.RMSE1)}
        FSS: {np.mean(self.FSS1)}
        TS: {np.mean(self.TS1)}

        <RA-Correct>
        RMSE: {np.mean(self.RMSE2)}
        FSS: {np.mean(self.FSS2)}
        TS: {np.mean(self.TS2)}
        """
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
            for threshold in np.linspace(2, 20, 10):
                FSS = Calculation.FSS_(threshold=threshold, real=real[time], pred=correct[time])
                FSSEACH.append(FSS)
            TS = Calculation.ThreatScore(real=real[time], pred=correct[time])
            rain1 = np.ravel(real[time])
            rain2 = np.ravel(correct[time])
            RMSE = Calculation.calcRMSE(rain1, rain2)
            ALL1.append(RMSE)
            ALL2.append(FSSEACH)
            ALL3.append(TS)
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

        self.RMSE1, self.FSS1, self.TS1 = self.calcEvalIndex_RA_MSMs()
        self.save()
        text = f"""
        <RA-MSMs>
        RMSE: {np.mean(self.RMSE1)}
        FSS: {np.mean(self.FSS1)}
        TS: {np.mean(self.TS1)}
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
            rain1 = np.ravel(rain_Ra[time])
            rain2 = np.ravel(rain_MSMs[time])
            RMSE = Calculation.calcRMSE(rain1, rain2)
            ALL1.append(RMSE)
            ALL2.append(FSSEACH)
            ALL3.append(TS)
            print(f'time: {time}')
        return ALL1, ALL2, ALL3

    def save(self):
        np.save('/home/jjthomson/fdrive/npy/RMSE', self.RMSE1)
        np.save('/home/jjthomson/fdrive/npy/FSS', self.FSS1)
        np.save('/home/jjthomson/fdrive/npy/TS', self.TS1)