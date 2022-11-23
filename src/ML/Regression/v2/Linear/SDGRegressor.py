import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import sklearn.model_selection as cross_validation
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

from ML.Other.Abstract import SKLearnOnlyMethod as SKLearn

class SDGRegressor:
    @classmethod
    def createModel(cls, save_path, X, Y):
        X_train, X_test, Y_train, Y_test = cls.getDistributedData(X, Y)
        model = linear_model.SGDRegressor(max_iter=1000)
        model.fit(X_train, Y_train)
        
        pred_model=model.predict(X_test)
        r2_lr = r2_score(Y_test, pred_model)
        mae_lr = mean_absolute_error(Y_test, pred_model)
        scores = cross_validation.cross_val_score(model, X, Y, cv=5)
        RMSE = cls.calcRMSE(pred_model, Y_test)

        with open('{}.txt'.format(save_path), 'w') as f:
            f.write(
                f'''
                X length:, {len(X)}
                X components length: {len(X[0])}
                Y length: {len(Y)}
                Cross-Validation scores: {scores})
                Test set score: {model.score(X_test, Y_test)}
                R2: {r2_lr}
                MAE: {mae_lr}
                Coef: {model.coef_}
                Intercept: {model.intercept_}
                RMSE: {RMSE}
                '''
            )

        plt.scatter(Y_test, pred_model, c='r', marker='s',label="ALL")
        plt.legend()
        plt.hlines(y=0, xmin=0, xmax=50, colors='black')
        plt.show
        # plt.savefig('./test3.png')
        SKLearn.saveModel(model, '{}.sav'.format(save_path))

    @classmethod
    def getDistributedData(cls, X, Y):
        sc=preprocessing.StandardScaler()
        sc.fit(X)
        X=sc.transform(X)
        sc.fit(Y)
        Y=sc.transform(Y)
        X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)
        return X_train, X_test, Y_train, Y_test

    @classmethod
    def calcRMSE(cls, pred_model, Y_test):
        X = pred_model
        Y = Y_test
        deviation = [(x - y) ** 2 for (x, y) in zip(X, Y)]
        RMSE = pow(np.mean(deviation), 0.5)
        return RMSE