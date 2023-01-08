import subprocess

from netCDF.v3.HeavyRainCases.SVR import *
from External.Slack import *

class advModel1(Model1):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern1.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern1.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern1.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern1.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern1.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern1.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern1'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern1.json'

class advModel2(Model2):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern2.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern2.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern2.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern2.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern2.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern2.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern2'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern2.json'

class advModel3(Model3):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern3.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern3.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern3.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern3.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern3.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern3.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern3'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern3.json'

class advModel4(Model4):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern4.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern4.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern4.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern4.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern4.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern4.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern4'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern4.json'

class advModel5(Model5):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern5.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern5.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern5.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern5.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern5.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern5.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern5'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern5.json'

class advModel6(Model6):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/HeavyRainCases/SVR/pattern6.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern6.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/HeavyRainCases/SVR/pattern6.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR/pattern6.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/HeavyRainCases/SVR/pattern6.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/HeavyRainCases/SVR/pattern6.gs'
        self.dirPath = 'HeavyRainCases/SVR/pattern6'
        self.json_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/HeavyRainCases/SVR/pattern6.json'

try:
    # model1 = advModel1()
    # model1.create()
    # model1.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model1, ls: {}'.format(__file__, r.stdout))
    # model2 = advModel2()
    # model2.create()
    # model2.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model2, ls: {}'.format(__file__, r.stdout))
    # model3 = advModel3()
    # model3.create()
    # model3.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model3, ls: {}'.format(__file__, r.stdout))
    # model4 = advModel4()
    # model4.create()
    # model4.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model4, ls: {}'.format(__file__, r.stdout))
    # model5 = advModel5()
    # model5.create()
    # model5.correct()
    # r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    # Slack.notification('file: {}, finished: model5, ls: {}'.format(__file__, r.stdout))
    model6 = advModel6()
    model6.create()
    model6.correct()
    r = subprocess.run('ls /home/ishihara/fdrive/nc/predict/v3/HeavyRainCases/SVR', shell=True, capture_output=True)
    Slack.notification('file: {}, finished: model6, ls: {}'.format(__file__, r.stdout))
except ExecutionError as e:
    Slack.notification('file: {}, error: {}'.format(__file__, e))

Slack.notification('file: {}, finished.'.format(__file__))