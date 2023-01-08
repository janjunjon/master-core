import random
import subprocess

from netCDF.v3.Rain.SVR import *
from External.Slack import *

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern1.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern2.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern3.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern4.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern5.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

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
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern6.json'

        indexes = self.Data.Rain(self).tolist()
        indexes = random.sample(indexes, 80000)
        self.setVarnames, self.varnames = self.Variables.pattern1(self)
        self.model = self.RegressionModel()
        self.setSpecificVars(self.setVarnames)
        self.X, self.Y = self.shapeXY(indexes, self.varnames)

try:
    # model1 = advModel1(correct=True)
    # model1.create()
    # model1.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model1, ls: {}'.format(__file__, r.stdout))
    # model2 = advModel2(correct=True)
    # model2.create()
    # model2.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model2, ls: {}'.format(__file__, r.stdout))
    # model3 = advModel3(correct=True)
    # model3.create()
    # model3.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model3, ls: {}'.format(__file__, r.stdout))
    # model4 = advModel4(correct=True)
    # model4.create()
    # model4.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model4, ls: {}'.format(__file__, r.stdout))
    model5 = advModel5(correct=True)
    model5.create()
    model5.correct()
    r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    Slack.notification('file: {}, finished: model5, ls: {}'.format(__file__, r.stdout))
    model6 = advModel6(correct=True)
    model6.create()
    model6.correct()
    r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/Rain/SVR', shell=True, capture_output=True)
    Slack.notification('file: {}, finished: model6, ls: {}'.format(__file__, r.stdout))
except ExecutionError as e:
    Slack.notification('file: {}, error: {}'.format(__file__, e))

Slack.notification('file: {}, finished.'.format(__file__))