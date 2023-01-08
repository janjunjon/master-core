from netCDF.v3.MLCorrectModel import *

class Model1(MLCorrectModel):
    """
    Variables: ['rain_MSMs', 'temp', 'u', 'v', 'sp']
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern1.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern1.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern1.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern1.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern1.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern1.gs'
        self.dirPath = 'Rain/SVR/pattern1'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern1.json'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern2.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern2.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern2.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern2.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern2.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern2.gs'
        self.dirPath = 'Rain/SVR/pattern2'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern2.json'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern2(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern3.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern3.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern3.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern3.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern3.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern3.gs'
        self.dirPath = 'Rain/SVR/pattern3'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern3.json'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern3(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern4.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern4.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern4.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern4.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern4.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern4.gs'
        self.dirPath = 'Rain/SVR/pattern4'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern4.json'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern4(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern5.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern5.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern5.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern5.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern5.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern5.gs'
        self.dirPath = 'Rain/SVR/pattern5'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern5.json'

        indexes = self.Data.Rain(self)
        self.setVarnames, self.varnames = self.Variables.pattern5(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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
    Data: Rain
    Model: SVR
    """
    def __init__(self, correct=False) -> None:
        super().__init__()
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern6.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern6.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern6.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern6.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern6.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern6.gs'
        self.dirPath = 'Rain/SVR/pattern6'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern6.json'

        indexes = self.Data.Rain(self)
        self.varnames = self.Variables.pattern6(self)
        self.model = self.RegressionModel()
        self.setPCAComponents()
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

    def create(self):
        self.model.SVR(
            save_path=self.model_path,
            text_path=self.text_path,
            json_path=self.json_path,
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