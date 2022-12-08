from netCDF.v3.MLNetCDF import *

class Pattern1(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'temp', 'u', 'v', 'sp']
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern1.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern1.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
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
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern1.nc',
            X=X
        )

class Pattern2(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'rh950hPa','rh700hPa', 'rh500hPa', 'ept950hPa', 'ept700hPa', 'ept500hPa']
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern2.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern2.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern2(self)
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
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern2.nc',
            X=X
        )

class Pattern3(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'div', 'td', 'lcl', 'uvs', 'vvs']
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern3.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern3.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern3(self)
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
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern3.nc',
            X=X
        )

class Pattern4(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'ncld', 'pt950hPa', 'pt700hPa', 'pt500hPa', 'ssi', 'ki']
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern4.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern4.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern4(self)
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
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern4.nc',
            X=X
        )

class Pattern5(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'u', 'ncld', 'ept700hPa', 'uvs'] ※ corrcoef highest order of each pattern
    Data: Rain
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SDGRegressor/pattern5.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SDGRegressor/pattern5.txt'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern5(self)
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
            ncSavePath='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern5.nc',
            X=X
        )