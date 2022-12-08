import time as Time
import numpy as np
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

class SVRHyperParams:
    @classmethod
    def model(cls, X_train, X_test, Y_train, Y_test) -> svm.SVR:
        starttime = Time.time()
        gscv = GridSearchCV(svm.SVC(), cls.param(), cv=4, verbose=2, error_score='raise')
        gscv.fit(X_train, Y_train)

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

        return best, gscv

    @classmethod
    def param(cls):
        ret = {
            'C':[1, 10, 100],
            'kernel':['rbf'],
            'degree':np.arange(1, 6, 1),
            'gamma':np.linspace(0.01, 1.0, 50)
        }
        return ret