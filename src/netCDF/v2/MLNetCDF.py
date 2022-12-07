import numpy as np

from netCDF.NetCDF import NetCDF
from ML.Other.Abstract import SKLearn
from ML.Other.HeavyRainCases import Indexes
from Module.Draw import Draw
from Module.Array import Array
from Module.Calculation import Calculation as MathCalculation

class MLNetCDF(SKLearn):
    """
    Class to predict rain_Ra from rain_MSM and components from Principal Component Analysis, using netCDF.

    self.used_component: how much components you use
    self.predicted_time_step: t tstep you wanna predict. from 0 to 248
    """
    def __init__(self) -> None:
        super().__init__()
        self.model = self.loadModel(
            '{}/var/MLModels/v2/SDGRegressor_PCA_Rain.sav'.format(self.root_path)
        )
        self.save_path = '/home/jjthomson/fdrive/images/predict/PCA/predictedRain20200703_0300JST_Rain01.png'
        self.region = [22, 48, 120, 150]
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_pca = NetCDF('/home/jjthomson/fdrive/nc/PCA/pca.nc')
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs']
        self.rain_Ra = self.nc_rains.variables['rain_Ra']
        self.used_component = 10
        self.predicted_time_step = 24

    def predict(self):
        rain_MSMs = self.rain_MSMs[self.predicted_time_step]
        X = self.getX()
        # X = self.getAdditionalX(additionalX=rain_MSMs, X=X)
        X = Array.getTransposedMatrix(X)
        rain_MSMs = np.ravel(rain_MSMs)
        predicted = np.array(self.model.predict(X))
        # for i in range(len(predicted)):
        #     if rain_MSMs[i] < 10:
        #         predicted[i] = rain_MSMs[i]
        predicted = predicted.reshape([253, 241])
        self.predicted = predicted
        print(self.calcRMSE())
        self.makeFigure(self.predicted)
        indexes = Indexes.getIndexesLatLon(self, range(56,106), range(64,104))
        FSS = MathCalculation.FSS_(indexes, 0.5, np.ravel(self.rain_Ra[self.predicted_time_step]), np.ravel(predicted))
        print('FSS: {:.4f}'.format(FSS))
        # arr_fss = []
        # thresholds = np.linspace(0, 50, 21)
        # for threshold in thresholds:
        #     FSS = MathCalculation.FSS_(indexes, threshold, np.ravel(self.rain_Ra[self.predicted_time_step]), np.ravel(predicted))
        #     print(f'threshold: {threshold}, FSS: {FSS}')
        #     arr_fss.append(FSS)

    def makeFigure(self, var):
        d = Draw()
        d.drawMapByArrayNotMultidimensional(
            v_array=var,
            v_lat=self.nc_rains.lat,
            v_lon=self.nc_rains.lon,
            path=self.save_path,
            region=self.region
        )

    def calcRMSE(self):
        t = self.predicted_time_step
        X = np.ravel(self.rain_Ra[t])
        # Y = np.ravel(self.rain_MSMs[t])
        Y = np.ravel(self.predicted)
        deviation = np.array([(x - y) ** 2 for (x, y) in zip(X, Y)])
        RMSE = pow(np.mean(deviation), 0.5)
        return RMSE
        
    def getX(self) -> list:
        """
        <caution>
        X to return should be 2 dimensional array: X[number_of_data][number_of_variables]

        <memo>
        pca.feature: pca.feature[number_of_data][number_of_variables]
            so, if specific pca components, specify where you wanna use (example: [:10]) after transpose pca.feature
        """
        X = []
        for i in range(self.used_component):
            component = np.ravel(self.nc_pca.variables[f'component{i+1}'][self.predicted_time_step]).tolist()
            X.append(component)
        return X

    def getAdditionalX(self, additionalX, X) -> list:
        if not isinstance(X, list):
            X = X.tolist()
        additionalX = np.ravel(additionalX).tolist()
        X.append(additionalX)
        return X