from netCDF.v3.Setter import *
from ML.Regression.v3.Linear.SDGRegressor import SDGRegressor

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
        def pattern_1(self):
            varnames = ['rain_MSMs', 'temp', 'u', 'v', 'sp']
            return varnames

    class RegressionModel:
        """
        return ModelMachine Learning Regression Model to create MLCorrectModel
        """
        def SDGRegressor(self, save_path, text_path, X, Y):
            SDGRegressor.createModel(save_path, text_path, X, Y)

    class Data:
        """
        return indexes of input data if RadarAmedas Rain exists except for undef.
        """
        def Rain(self):
            # instance = IndexesRain()
            # indexes = instance.getIndexes(rain)
            indexes = np.load('/home/jjthomson/master-core/var/Data/Rain.npy')
            return indexes

        def HeavyRainCases(self):
            indexes = np.load('/home/jjthomson/master-core/var/Data/HeavyRainCases.npy')
            return indexes

    class Predict:
        pass