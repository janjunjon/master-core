from netCDF.v3.Setter import *

class MLCorrectModel(Setter):
    """
    MLCorrectModel
    self.predicted_time_step: t tstep you wanna predict. from 0 to 248
    """
    def __init__(self) -> None:
        super().__init__()

    class Variables:
        """"""
        def pattern_1(self):
            pass

    class RegressionModel:
        """
        return ModelMachine Learning Regression Model to create MLCorrectModel
        """
        def SDGRegressor(self):
            pass

    class Data:
        """
        return indexes of input data if RadarAmedas Rain exists except for undef.
        """
        def Rain(self, rain):
            instance = IndexesRain()
            indexes = instance.getIndexes(rain)
            return indexes

        def HeavyRainCases(self):
            indexes = np.load('/home/jjthomson/master-core/var/Data/HeavyRainCases.npy')
            return indexes

    class Predict:
        pass
        
    