from netCDF.v3.MLCorrectModel import *

class Model1(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'temp', 'u', 'v', 'sp']
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern1.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern1.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern1.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern1.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern1.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern1.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern1'

        indexes = self.Data.HeavyRainCases(self)
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )

class Model2(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'rh950hPa','rh700hPa', 'rh500hPa', 'ept950hPa', 'ept700hPa', 'ept500hPa']
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern2.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern2.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern2.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern2.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern2.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern2.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern2'

        indexes = self.Data.HeavyRainCases(self)
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )

class Model3(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'div', 'td', 'lcl', 'uvs', 'vvs']
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern3.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern3.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern3.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern3.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern3.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern3.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern3'

        indexes = self.Data.HeavyRainCases(self)
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )

class Model4(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'ncld', 'pt950hPa', 'pt700hPa', 'pt500hPa', 'ssi', 'ki']
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern4.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern4.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern4.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern4.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern4.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern4.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern4'

        indexes = self.Data.HeavyRainCases(self)
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )

class Model5(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'u', 'ncld', 'ept700hPa', 'uvs'] ※ corrcoef highest order of each pattern
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern5.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern5.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern5.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern5.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern5.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern5.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern5'

        indexes = self.Data.HeavyRainCases(self)
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )

class Model6(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'u', 'ncld', 'ept700hPa', 'uvs'] ※ corrcoef highest order of each pattern
    Data: HeavyRainCases
    Model: SDGRegressor
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/HeavyRainCases/SDGRegressor/pattern6.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SDGRegressor/pattern6.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SDGRegressor/pattern6.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/HeavyRainCases/SDGRegressor/pattern6.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/HeavyRainCases/SDGRegressor/pattern6.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/HeavyRainCases/SDGRegressor/pattern6.gs'
        self.dirPath = 'HeavyRainCases/SDGRegressor/pattern6'

        indexes = self.Data.HeavyRainCases(self)
        self.varnames = self.Variables.pattern6(self)
        self.model = self.RegressionModel()
        self.setPCAComponents()
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
        self.createGradsFiles(self.ctl_path, self.gs_path, self.dirPath)
        X = self.shapeXForPredict(self.varnames)
        self.predictAll(
            ncSavePath=self.nc_path,
            X=X
        )