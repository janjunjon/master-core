from netCDF.CalcEvaluationIndex import *

class Execution:
    def main(self):
        instance = Eval(
            dirPath='Rain/SDGRegressor',
            pattern='pattern1'
        )
        instance.main()
        instance = Eval(
            savePath='/home/jjthomson/fdrive/nc/predict/v3_eval/Rain/SDGRegressor/pattern2.txt',
            nc_correct_path='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern2.nc'
        )
        instance.main()
        instance = Eval(
            savePath='/home/jjthomson/fdrive/nc/predict/v3_eval/Rain/SDGRegressor/pattern3.txt',
            nc_correct_path='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern3.nc'
        )
        instance.main()
        instance = Eval(
            savePath='/home/jjthomson/fdrive/nc/predict/v3_eval/Rain/SDGRegressor/pattern4.txt',
            nc_correct_path='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern4.nc'
        )
        instance.main()
        instance = Eval(
            savePath='/home/jjthomson/fdrive/nc/predict/v3_eval/Rain/SDGRegressor/pattern5.txt',
            nc_correct_path='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern5.nc'
        )
        instance.main()
        instance = Eval(
            savePath='/home/jjthomson/fdrive/nc/predict/v3_eval/Rain/SDGRegressor/pattern6.txt',
            nc_correct_path='/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/pattern6.nc'
        )
        instance.main()