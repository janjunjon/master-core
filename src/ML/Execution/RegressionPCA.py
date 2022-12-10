import numpy as np

from netCDF.NetCDF import NetCDF
from Module.Array import Array
from ML.Other.Abstract import SKLearn
from ML.Other.HeavyRainCases import Indexes
from ML.DR.PCA import *
from ML.Regression.v2.Linear.SDGRegressor import SDGRegressor

class Execution(SKLearn):
    """
    Execution to create RegressionModel from PCA components
    """
    def __init__(self, save_path, i, indexes=True) -> None:
        super().__init__()
        self.save_path = save_path
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_pca = NetCDF('/home/jjthomson/fdrive/nc/PCA/pca.nc')
        self.components = self.getPCAComponents()
        self.Ra = self.nc_rains.variables['rain_Ra']
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs']
        if indexes:
            instance = Indexes()
            self.indexes = instance.indexes
        self.i = i

    def createModel(self):
        X, Y = self.getXY()
        SDGRegressor.createModel(
            save_path=self.save_path,
            X=X,
            Y=Y
        )

    def getXY(self):
        """
        <caution>
        X, Y to return should be 2 dimensional array: X[number_of_data][number_of_variables]

        <memo>
        pca.feature: pca.feature[number_of_data][number_of_variables]
            so, if specific pca components, specify where you wanna use (example: [:10]) after transpose pca.feature
        """
        rains_Ra = Array.convert(self.Ra[:].tolist())
        Y = [[rains_Ra[i]] for i in self.indexes]
        components = self.components[:self.i]
        X = []
        for component in components:
            each = []
            for index in self.indexes:
                each.append(component[index])
            X.append(each)
        X = self.additionalX(X)
        X = Array.getTransposedMatrix(X)
        print(type(X), len(X), len(X[0]))
        print(type(Y), len(Y), len(Y[0]))
        return X, Y

    def additionalX(self, X):
        """
        if additional explanatory variables exists, append it to `additional X`
        """
        if not isinstance(X, list):
            X = X.tolist()
        additionalX = []
        rains_MSMs = Array.convert(self.rain_MSMs[:].tolist())
        X_rain = [rains_MSMs[i] for i in self.indexes]
        additionalX.append(X_rain)
        X.extend(additionalX)
        return X

    def getPCAComponents(self):
        for i in range(21):
            # setattr(self, f'component{i}', self.nc_pca.variables[f'component{i}'])
            if i == 0:
                components = np.array([np.ravel(self.nc_pca.variables[f'component{i+1}'][:])])
            else:
                components = np.append(components, [np.ravel(self.nc_pca.variables[f'component{i+1}'][:])], axis=0)
        return components