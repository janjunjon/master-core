import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import sklearn.model_selection as cross_validation
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import PolynomialFeatures

from ML.Other.Abstract import SKLearnOnlyMethod as SKLearn

class NonLinearSDGRegressor:
    @classmethod
    def createModel(cls, save_path, text_path, X, Y):
        length = len(X[0])
        X_train, X_test, Y_train, Y_test = cls.getDistributedData(X, Y)
        poly = PolynomialFeatures(length)
        X_poly = poly.fit_transform(X_train)
        X_test = poly.fit_transform(X_test)
        model = linear_model.SGDRegressor(max_iter=1000)
        model.fit(X_poly, Y_train)
        
        pred_model=model.predict(X_test)
        r2_lr = r2_score(Y_test, pred_model)
        mae_lr = mean_absolute_error(Y_test, pred_model)
        scores = cross_validation.cross_val_score(model, X, Y, cv=5)
        RMSE = cls.calcRMSE(pred_model, Y_test)

        with open(text_path, 'w') as f:
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
        SKLearn.saveModel(model, save_path)

    @classmethod
    def getDistributedData(cls, X, Y):
        sc=preprocessing.StandardScaler()
        sc.fit(X)
        X=sc.transform(X)
        X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)
        return X_train, X_test, Y_train, Y_test

    @classmethod
    def calcRMSE(cls, pred_model, Y_test):
        X = pred_model
        Y = Y_test
        deviation = [(x - y) ** 2 for (x, y) in zip(X, Y)]
        RMSE = pow(np.mean(deviation), 0.5)
        return RMSE