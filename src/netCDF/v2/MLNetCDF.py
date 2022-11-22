from os import pread
from ML.Other.Abstract import SKLearn
from Module.Draw import Draw

from netCDF.NetCDF import NetCDF
import numpy as np

class MLNetCDF(SKLearn):
    def __init__(self) -> None:
        super().__init__()
        self.model = self.loadModel(
            '{}/var/MLModels/v2/SDGRegressor_PCA_HeavyRainCases.sav'.format(self.root_path)
        )
        self.save_path = '/home/jjthomson/fdrive/images/predict/predictedRain20200703_0300JST_HeavyRainCases.png'
        self.region = [22, 48, 120, 150]
        self.predicted_time_step = 24
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_pca = NetCDF('/home/jjthomson/fdrive/nc/PCA/pca.nc')
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs']
        i = self.predicted_time_step

    def predict(self):
        rain_MSMs = np.ravel(self.rain_MSMs[self.predicted_time_step])
        X = [[rain_MSMs[i]] for i in range(253*241)]
        predicted = np.array(self.model.predict(X))
        for i in range(len(predicted)):
            if rain_MSMs[i] < 10:
                predicted[i] = rain_MSMs[i]
        predicted = predicted.reshape([253, 241])
        self.predicted = predicted
        print(self.calcRMSE())
        self.makeFigure(self.predicted)

    def makeFigure(self, var):
        d = Draw()
        d.drawMapByArrayNotMultidimensional(
            v_array=var,
            v_lat=self.lat,
            v_lon=self.lon,
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

    def getPCAComponents(self):
        for i in range(21):
            # setattr(self, f'component{i}', self.nc_pca.variables[f'component{i}'])
            if i == 0:
                components = np.array([np.ravel(self.nc_pca.variables[f'component{i+1}'][self.predicted_time_step])])
            else:
                components = np.append(components, [np.ravel(self.nc_pca.variables[f'component{i+1}'][self.predicted_time_step])], axis=0)
        return components