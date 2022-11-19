import numpy as np

from netCDF.NetCDF import NetCDF
from Module.Array import Array
from ML.Other.Abstract import SKLearn
from ML.DR.PCA import *
from ML.Regression.v2.Linear.SDGRegressor import SDGRegressor

class Execution(SKLearn):
    def __init__(self, save_path, pca_path, mlmodel_path=None) -> None:
        super().__init__()
        self.save_path = save_path
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.Ra = self.nc_rains.variables['rain_Ra']
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs']
        self.pca = PCALoad(pca_path)
        if mlmodel_path:
            self.model = self.loadModel('{}/var/MLModels/{}'.format(self.root_path, mlmodel_path))
        else:
            pass

    def createModel(self):
        rains_Ra = Array.convert(self.Ra)
        rains_MSMs = Array.convert(self.rain_MSMs)
        X = self.pca.feature.T[:10]
        X_rain = [[rains_MSMs[i]] for i in self.pca.indexes]
        X = X.tolist()
        X.append(X_rain)
        X = np.array(X, dtype=object)
        X = X.T
        X = X.tolist()
        Y = [[rains_Ra[i]] for i in self.pca.indexes]
        print(len(X_rain), len(X_rain[0]))
        print(self.pca.indexes[:20])
        print(type(X), len(X), len(X[0]))
        print(type(Y), len(Y), len(Y[0]))
        SDGRegressor.createModel(
            save_path=self.save_path,
            X=X,
            Y=Y
        )