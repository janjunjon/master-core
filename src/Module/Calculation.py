import numpy as np
from scipy import stats
import itertools
from sklearn.metrics import mean_squared_error

from Exception.Exception import *
from Module.Array import Array

class Calculation:
    @classmethod
    def calcRMSE(cls, X, Y):
        deviation = [(x - y) ** 2 for (x, y) in zip(X, Y)]
        RMSE = pow(np.mean(deviation), 0.5)
        return RMSE

    @classmethod
    def corrcoef_(cls, array1, array2):
        if not isinstance(array1, np.ndarray):
            array1 = np.array(array1)
        if not isinstance(array2, np.ndarray):
            array2 = np.array(array2)
        corrcoef_ = np.corrcoef(array1, array2)
        return corrcoef_

    @classmethod
    def FSS_(cls, threshold, real, pred):
        real = Array.listToNdArray(real)
        pred = Array.listToNdArray(pred)
        if real.ndim != 2 and pred.ndim != 2:
            raise DimensionalError('real/pred dimension must be 2 dims.')
        real = np.ravel(real).tolist()
        pred = np.ravel(pred).tolist()
        Io = [1 if value >= threshold else 0 for value in real]
        If = [1 if value >= threshold else 0 for value in pred]
        Io = Array.reshape(Io)
        If = Array.reshape(If)
        for lat in range(253):
            for lon in range(241):
                if lat == 0 or lon == 0 or lat == 252 or lon == 240:
                    pass
                else:
                    patterns = list(itertools.product([lon-1, lon, lon+1], repeat=2))
                    value = 0
                    for i in range(len(patterns)):
                        value += Io[patterns[i][0]][patterns[i][1]]
                    Io[lat][lon] = value / len(patterns)
                    value = 0
                    for i in range(len(patterns)):
                        value += If[patterns[i][0]][patterns[i][1]]
                    If[lat][lon] = value / len(patterns)
        real = np.ravel(real).tolist()
        pred = np.ravel(pred).tolist()
        MSE = mean_squared_error(Io, If)
        MSEref = np.mean([(If[j]**2 + Io[j]**2) for j in range(len(Io))])
        if MSE > MSEref or MSEref == 0:
            return 0
        FSS = 1 - (MSE / MSEref)
        return FSS

    @classmethod
    def ThreatScore(self, real, pred, threshold=0):
        """
        FO: 適中, FX: 空振り, XO: 見逃し, XX: 適中
        """
        real = Array.convert(real)
        pred = Array.convert(pred)
        FO = 0
        FX = 0
        XO = 0
        XX = 0
        for i in range(len(real)):
            if real[i] > threshold and pred[i] > threshold:
                FO += 1
            elif real[i] <= threshold and pred[i] > threshold:
                FX += 1
            elif real[i] > threshold and pred[i] <= threshold:
                XO += 1
            elif real[i] <= threshold and pred[i] <= threshold:
                XX += 1
        # print(f'FO: {FO}, FX: {FX}, XO: {XO}, XX: {XX}, ')
        TS = FO / (FO + FX + XO)
        return TS

    @classmethod
    def welchT(cls, array1, array2):
        value = stats.ttest_ind(array1, array2, equal_var=False)
        return value