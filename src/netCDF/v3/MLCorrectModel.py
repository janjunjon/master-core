from netCDF.v3.Setter import *
from ML.Regression.v3.Linear.LinearRegression import LinearRegression
from ML.Regression.v3.Linear.SDGRegressor import SDGRegressor
from ML.Regression.v3.NonLinear.PolynomialRegression import NonLinearSDGRegressor
from ML.Regression.v3.NonLinear.SVR import SVR

class MLCorrectModel(Setter):
    """
    MLCorrectModel
    self.predicted_time_step: t tstep you wanna predict. from 0 to 248
    """
    def __init__(self) -> None:
        super().__init__()

    class Variables:
        """
        return pattern of explanatory variables
        """
        def preparation(self):
            setVarnames = ['rain_MSMs']
            varnames = ['rain_MSMs']
            return setVarnames, varnames

        def pattern1(self):
            setVarnames = ['rain_MSMs', 'temp', 'u', 'v', 'sp']
            varnames = ['rain_MSMs', 'temp', 'u', 'v', 'sp']
            return setVarnames, varnames

        def pattern2(self):
            setVarnames = ['rain_MSMs', 'rh', 'ept']
            varnames = ['rain_MSMs', 'rh950hPa','rh700hPa', 'rh500hPa', 'ept950hPa', 'ept700hPa', 'ept500hPa']
            return setVarnames, varnames

        def pattern3(self):
            setVarnames = ['rain_MSMs', 'div', 'td', 'lcl', 'uvs', 'vvs']
            varnames = ['rain_MSMs', 'div', 'td', 'lcl', 'uvs', 'vvs']
            return setVarnames, varnames

        def pattern4(self):
            setVarnames = ['rain_MSMs', 'ncld', 'pt', 'ssi', 'ki']
            varnames = ['rain_MSMs', 'ncld', 'pt950hPa', 'pt700hPa', 'pt500hPa', 'ssi', 'ki']
            return setVarnames, varnames

        def pattern5(self):
            setVarnames = ['rain_MSMs', 'u', 'ncld', 'ept', 'uvs']
            varnames = ['rain_MSMs', 'u', 'ncld', 'ept700hPa', 'uvs']
            return setVarnames, varnames

        def pattern6(self):
            varnames = [
                'rain_MSMs',
                'pca1_component1', 'pca1_component2', 'pca2_component1', 'pca2_component2',
                'pca3_component1', 'pca3_component2', 'pca4_component1', 'pca4_component2',
            ]
            return varnames

    class RegressionModel:
        """
        return ModelMachine Learning Regression Model to create MLCorrectModel
        """
        def LinearRegression(self, save_path, text_path, X, Y):
            LinearRegression.createModel(save_path, text_path, X, Y)

        def SDGRegressor(self, save_path, text_path, X, Y):
            SDGRegressor.createModel(save_path, text_path, X, Y)

        def NonLinearSDGRegressor(self, save_path, text_path, X, Y):
            NonLinearSDGRegressor.createModel(save_path, text_path, X, Y)

        def SVR(self, save_path, text_path, json_path, X, Y):
            SVR.createModel(save_path, text_path, json_path, X, Y)
            # gridsearch, KSVR = SVR.debug(X, Y)
            # return gridsearch, KSVR

    class Data:
        """
        return indexes of input data if RadarAmedas Rain exists except for undef.
        """
        def Rain(self):
            # instance = IndexesRain()
            # indexes = instance.getIndexes(rain)
            indexes = np.load('/home/ishihara/master-core/var/Data/Rain.npy')
            return indexes

        def HeavyRainCases(self):
            indexes = np.load('/home/ishihara/master-core/var/Data/HeavyRainCases.npy')
            return indexes

    class Predict:
        pass