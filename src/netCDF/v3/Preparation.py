from netCDF.v3.MLNetCDF import *

class Preparation1(MLCorrectModel):
    """
    Variables: rain_MSMs
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/preparation.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/preparation.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.preparation(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SDGRegressor(
            save_path=self.model_path,
            text_path=self.text_path,
            X=self.X,
            Y=self.Y
        )
    
    def correct(self):
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/preparation.nc',
            X=X
        )

class Preparation2(MLCorrectModel):
    """
    Variables: rain_MSMs
    Data: Rain
    Model: NonLinearSDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/Nonlinear-SDGRegressor/preparation.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/Nonlinear-SDGRegressor/preparation.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.preparation(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.NonLinearSDGRegressor(
            save_path=self.model_path,
            text_path=self.text_path,
            X=self.X,
            Y=self.Y
        )
    
    def correct(self):
        X = self.shapeXForPredict(self.varnames)
        self.predictAllNonLinear(
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/Nonlinear-SDGRegressor/preparation.nc',
            X=X
        )

class Preparation3(MLCorrectModel):
    """
    Variables: rain_MSMs
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SVR/preparation.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SVR/preparation.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.preparation(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            X=self.X,
            Y=self.Y
        )
    
    def correct(self):
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SVR/preparation.nc',
            X=X
        )