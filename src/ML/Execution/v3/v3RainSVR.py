from netCDF.v3.Rain.SVR import *
import random

class advModel1(Model1):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern1.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern1.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern1.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern1.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern1.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern1.gs'
        self.dirPath = 'Rain/SVR/pattern1'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern1.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model1 = advModel1()
model1.create()
model1.correct()

class advModel2(Model2):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern2.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern2.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern2.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern2.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern2.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern2.gs'
        self.dirPath = 'Rain/SVR/pattern2'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern2.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model2 = advModel2()
model2.create()
model2.correct()

class advModel3(Model3):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern3.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern3.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern3.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern3.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern3.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern3.gs'
        self.dirPath = 'Rain/SVR/pattern3'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern3.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model3 = advModel3()
model3.create()
model3.correct()

class advModel4(Model4):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern4.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern4.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern4.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern4.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern4.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern4.gs'
        self.dirPath = 'Rain/SVR/pattern4'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern4.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model4 = advModel4()
model4.create()
model4.correct()

class advModel5(Model5):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern5.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern5.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern5.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern5.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern5.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern5.gs'
        self.dirPath = 'Rain/SVR/pattern5'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern5.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model5 = advModel5()
model5.create()
model5.correct()

class advModel6(Model6):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/SVR/pattern6.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern6.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern6.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/SVR/pattern6.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern6.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/SVR/pattern6.gs'
        self.dirPath = 'Rain/SVR/pattern6'
        self.json_path = '/home/ishihara/master-core/var/v3_result/HeavyRainCases/SVR/pattern6.json'

        indexes = self.Data.Rain(self)
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        if not correct:
            self.X, self.Y = self.shapeXY(indexes, self.varnames)

model6 = advModel6()
model6.create()
model6.correct()