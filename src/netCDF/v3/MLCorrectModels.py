from netCDF.v3.MLNetCDF import *

class Pattern1(MLCorrectModel):
    def __init__(self) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern1.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern1.txt'

        indexes = self.Data.Rain(self)
        varnames = self.Variables.pattern_1(self)
        self.setSpecificVars(varnames)
        self.X, self.Y = self.shapeXY(indexes, varnames)

    def create(self):
        model = self.RegressionModel()
        model.SDGRegressor(
            save_path=self.model_path,
            text_path=self.text_path,
            X=self.X,
            Y=self.Y
        )
    
    def correct(self):
        self.predictAll(
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern1.nc'
        )