import time as Time
import numpy as np
import pandas as pd
from sklearn import svm, metrics
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

class SVRHyperParams:
    @classmethod
    def model(cls, X_train, X_test, Y_train, Y_test) -> svm.SVR:
        starttime = Time.time()
        gscv = GridSearchCV(svm.SVC(), cls.param(), cv=4, verbose=2, error_score='raise')
        gscv.fit(X_train, Y_train)
        best_params = gscv.best_params_
        print(best_params)

        # スコアの一覧を取得
        gs_result = pd.DataFrame.from_dict(gscv.cv_results_)
        gs_result.to_csv('gs_result.csv')

        # 最高性能のモデルを取得し、テストデータを分類
        best = gscv.best_estimator_
        print("学習モデル=", best)
        pred = best.predict(X_test)

        # 混同行列を出力
        print(confusion_matrix(Y_test, pred))

        gs_result = pd.DataFrame.from_dict(gscv.cv_results_)
        gs_result.to_csv('/home/jjthomson/fdrive/csv/gs_result.csv')

        elapsedtime = Time.time() - starttime
        print ("Elapsed time for grid search: {0} [sec]".format(elapsedtime))

        return best, best_params

    @classmethod
    def param(cls):
        ret = {
            'C':[1, 10, 100],
            'kernel':['rbf'],
            'degree':np.arange(1, 6, 1),
            'gamma':np.linspace(0.01, 1.0, 50)
        }
        return ret

class PolynomialRegression:
    @classmethod
    def model(cls, X_train, X_test, Y_train, Y_test):
        starttime = Time.time()
        params = {
            'polynomialfeatures__degree': np.arange(4)
        }
        gridsearch = GridSearchCV(
            PolynomialFeatures(),
            params, cv=10,
            scoring='neg_mean_squared_error'
        )
        gridsearch.fit(X_train, Y_train)

        elapsedtime = Time.time() - starttime
        print("Elapsed time for grid search: {0} [sec]".format(elapsedtime))
        
        print('The best parameter = ',gridsearch.best_params_)
        print('RMSE = ',-gridsearch.best_score_)
        
        Poly = PolynomialFeatures(gridsearch.best_params_['polynomialfeatures__degree'])
        return gridsearch, Poly

class Sample:
    @classmethod
    def template(cls, X_train, X_test, Y_train, Y_test, json_path):
        starttime = Time.time()
        from sklearn.metrics import mean_absolute_error #MAE
        from sklearn.metrics import mean_squared_error #MSE
        from sklearn.metrics import make_scorer

        from sklearn.model_selection import GridSearchCV
        from sklearn.model_selection import KFold
        from sklearn.svm import SVR

        kf = KFold(n_splits=5,shuffle=True,random_state=0)

        params_cnt = 10
        params = {
            "kernel": ['rbf'],
            "C": np.logspace(0,1,params_cnt),
            "epsilon": np.logspace(-1,1,params_cnt)
        }

        gridsearch = GridSearchCV(
            SVR(gamma='auto'),
            params, cv=kf
        )
        '''
        epsilon : Epsilon parameter in the epsilon-insensitive loss function.
                Note that the value of this parameter depends on the scale of the target variable y.
                If unsure, set epsilon=0.
        C : Regularization parameter.
            The strength of the regularization is inversely proportional to C.
            Must be strictly positive.
        https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
        '''

        gridsearch.fit(X_train, Y_train)

        elapsedtime = Time.time() - starttime
        print ("Elapsed time for grid search: {0} [sec]".format(elapsedtime))
        
        print('The best parameter = ',gridsearch.best_params_)
        print('RMSE = ',-gridsearch.best_score_)
        print()

        try:
            with open(json_path, 'w') as f:
                f.write(str(gridsearch.best_params_))
        except:
            pass

        KSVR = SVR(
            kernel=gridsearch.best_params_['kernel'],
            C=gridsearch.best_params_["C"],
            epsilon=gridsearch.best_params_["epsilon"]
        )
        return gridsearch, KSVR