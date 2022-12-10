from netCDF.v3.Rain.SVR import *

class advModel1(Model1):
    def __init__(self, correct=False) -> None:
        super().__init__(correct)
        self.model_path = '/home/jjthomson/fdrive/MLCorrectModels/v3/Rain/SVR/pattern1.sav'
        self.text_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_result/Rain/SVR/pattern1.txt'
        # self.img_path = '/home/jjthomson/fdrive/MLCorrectModels/v3_img/Rain/SVR/pattern1.png'
        self.nc_path = '/home/jjthomson/fdrive/nc/predict/v3/Rain/SVR/pattern1.nc'
        self.ctl_path = '/home/jjthomson/fdrive/nc/predict/v3_ctl/Rain/SVR/pattern1.ctl'
        self.gs_path = '/home/jjthomson/fdrive/nc/predict/v3_gs/Rain/SVR/pattern1.gs'
        self.dirPath = 'Rain/SVR/pattern1'
        self.json_path = '/home/jjthomson/master-core/var/v3_result/HeavyRainCases/SVR/pattern1.json'
model1 = advModel1()
model1.create()
model1.correct()