from netCDF.v3.Rain.NonLinearSDGRegressor import *

class advModel1(Model1):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern1.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern1.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern1.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern1.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern1.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern1.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern1'
model1 = advModel1()
model1.create()
model1.correct()

class advModel2(Model2):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern2.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern2.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern2.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern2.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern2.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern2.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern2'
model2 = advModel2()
model2.create()
model2.correct()

class advModel3(Model3):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern3.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern3.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern3.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern3.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern3.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern3.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern3'
model3 = advModel3()
model3.create()
model3.correct()

class advModel4(Model4):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern4.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern4.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern4.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern4.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern4.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern4.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern4'
model4 = advModel4()
model4.create()
model4.correct()

class advModel5(Model5):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern5.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern5.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern5.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern5.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern5.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern5.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern5'
model5 = advModel5()
model5.create()
model5.correct()

class advModel6(Model6):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/ishihara/fdrive/MLCorrectModels/v3/Rain/NonLinearSDGRegressor/pattern6.sav'
        self.text_path = '/home/ishihara/fdrive/MLCorrectModels/v3_result/Rain/NonLinearSDGRegressor/pattern6.txt'
        # self.img_path = '/home/ishihara/fdrive/MLCorrectModels/v3_img/Rain/NonLinearSDGRegressor/pattern6.png'
        self.nc_path = '/home/ishihara/fdrive/nc/predict/v3/Rain/NonLinearSDGRegressor/pattern6.nc'
        self.ctl_path = '/home/ishihara/fdrive/nc/predict/v3_ctl/Rain/NonLinearSDGRegressor/pattern6.ctl'
        self.gs_path = '/home/ishihara/fdrive/nc/predict/v3_gs/Rain/NonLinearSDGRegressor/pattern6.gs'
        self.dirPath = 'Rain/NonLinearSDGRegressor/pattern6'
model6 = advModel6()
model6.create()
model6.correct()