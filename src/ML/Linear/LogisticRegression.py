import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import sklearn.model_selection as cross_validation
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
import sklearn
sklearn.__version__
import pickle

from ML.Abstract import SKLearn
from netCDF.NetCDF import NetCDF
from ML.MLData import Data as MLData

class Regression(SKLearn):
    def __init__(self):
        super().__init__()
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_MSMp = NetCDF('/home/jjthomson/fdrive/nc/LowLoadMSMp.nc')        
        self.save_path = '{}/var/MLModels/SDGRegressor_HeavyRain'.format(self.root_path)

        self.rain_Ra = self.nc_rains.variables['rain_Ra'][:][:][:].tolist()
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs'][:][:][:].tolist()
        self.w = self.nc_MSMp.variables['w'][:][:][:].tolist()
        self.u = self.nc_MSMp.variables['u'][:][:][:].tolist()
        self.v = self.nc_MSMp.variables['v'][:][:][:].tolist()
        self.temp = self.nc_MSMp.variables['temp'][:][:][:].tolist()
        self.rh = self.nc_MSMp.variables['rh'][:][:][:].tolist()        

    def main(self):
        X, Y = self.getData()
        X_train, X_test, Y_train, Y_test = self.getDistributedData(X, Y)
        model = linear_model.LogisticRegression(max_iter=1000)
        model.fit(X_train, Y_train)
        
        pred_model=model.predict(X_test)
        r2_lr = r2_score(Y_test, pred_model)
        mae_lr = mean_absolute_error(Y_test, pred_model)
        scores = cross_validation.cross_val_score(model, X, Y)

        print('Cross-Validation scores: {}'.format(scores))
        print('Test set score: {}'.format(model.score(X_test, Y_test)))
        print("R2 : %.3f" % r2_lr)
        print("MAE : %.3f" % mae_lr)
        print("Coef = ", model.coef_)
        print("Intercept =", model.intercept_)

        with open('{}.txt'.format(self.save_path), 'w') as f:
            f.write(
                f'''
                Cross-Validation scores: {scores})
                Test set score: {model.score(X_test, Y_test)}
                R2: {r2_lr}
                MAE: {mae_lr}
                Coef: {model.coef_}
                Intercept: {model.intercept_}
                '''
            )

        plt.scatter(Y_test, pred_model, c='r', marker='s',label="ALL")
        plt.legend()
        plt.hlines(y=0, xmin=0, xmax=50, colors='black')
        plt.show
        # plt.savefig('./test3.png')

        print("\n「RMだけの平均2乗誤差」と「全部を使用したときの平均二乗誤差」")
        RMS=np.mean((pred_model - Y_test) ** 2)
        print(RMS)

        self.saveModel(model, '{}.sav'.format(self.save_path))

    def getData(self):
        # self.rain_Ra = np.ravel(self.rain_Ra[0:56])
        # self.rain_MSMs = np.ravel(self.rain_MSMs[0:56])
        # self.w = np.ravel(self.w[0:56])
        # self.u = np.ravel(self.u[0:56])
        # self.v = np.ravel(self.v[0:56])
        # self.temp = np.ravel(self.temp[0:56])
        # self.rh = np.ravel(self.rh[0:56])
        d = MLData([
            self.rain_Ra,
            self.rain_MSMs,
            self.w,
            self.u,
            self.v,
            self.temp,
            self.rh
        ])
        Data = d.main()
        self.rain_Ra = Data[0]
        self.rain_MSMs = Data[1]
        self.w = Data[2]
        self.u = Data[3]
        self.v = Data[4]
        self.temp = Data[5]
        self.rh = Data[6]
        Y = []
        X = []
        print(len(self.rain_Ra))
        for i in range(len(self.rain_Ra)):
            if self.rain_Ra[i] > 0 and self.rain_MSMs[i] > 0:
                Y_arr = [
                    self.rain_Ra[i]
                ]
                X_arr = [
                    self.rain_MSMs[i],
                    self.w[i],
                    self.u[i],
                    self.v[i],
                    self.temp[i],
                    self.rh[i]
                ]
                Y.append(Y_arr)
                X.append(X_arr)
        print('X length:', len(X), 'X components length:', len(X[0]), 'Y length:', len(Y))
        sc=preprocessing.StandardScaler()
        sc.fit(X)
        X=sc.transform(X)
        sc.fit(Y)
        Y=sc.transform(Y)
        return X, Y

    def getDistributedData(self, X, Y):
        X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)
        return X_train, X_test, Y_train, Y_test

