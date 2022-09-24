import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
import sklearn.model_selection as cross_validation
import sklearn
sklearn.__version__
 
#解説 2：Housingのデータセットを読み込む--------------------------------
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data', header=None, sep='\s+')
df.columns=['CRIM','ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df)
X_rm=df[['RM']].values
X=df.iloc[:, 0:13]
#X=df[['AGE']].values
Y=df['MEDV'].values
 
 
#解説 3：データの整形-------------------------------------------------------
sc=preprocessing.StandardScaler()
sc.fit(X)
X=sc.transform(X)
sc.fit(X_rm)
X_rm=sc.transform(X_rm)

print(X.ndim, len(X), len(X[0]), X)
print(Y.ndim, len(Y), Y)
 
 
#解説 4：学習データとテストデータに分割する-------------------------------
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.2, random_state=0)
X_rm_train, X_rm_test, Y_train, Y_test = cross_validation.train_test_split(X_rm, Y, test_size=0.2, random_state=0)
 
#解説 5：SGD Regressorを適用する-------------------------------------------
clf = linear_model.SGDRegressor(max_iter=1000)
clf.fit(X_train, Y_train)
 
clf_rm = linear_model.SGDRegressor(max_iter=1000)
clf_rm.fit(X_rm_train, Y_train)
 
print("全部使用したときの回帰式の係数")
print(clf.intercept_) 
print(clf.coef_) 
 
#解説 6：結果をプロットする------------------------------------------------
 
line_X=np.arange(-4, 4, 0.1) #3から10まで1刻み
line_Y=clf_rm.predict(line_X[:, np.newaxis])
plt.figure(figsize=(10,10))
plt.subplot(2, 1, 1)
plt.scatter(X_rm_train, Y_train, c='b', marker='s')
plt.plot(line_X, line_Y, c='r')
plt.show
plt.savefig('./test1.png')
 
#解説 7：誤差をプロットする-------------------------------------------------
Y_rm_pred=clf_rm.predict(X_rm_test)
plt.subplot(2, 1, 2)
plt.scatter(Y_test, Y_rm_pred-Y_test, c='b', marker='s', label="RM_only")
 
Y_pred=clf.predict(X_test)
plt.scatter(Y_test, Y_pred-Y_test, c='r', marker='s',label="ALL")
plt.legend()
plt.hlines(y=0, xmin=0, xmax=50, colors='black')
plt.show
plt.savefig('./test2.png')

print("\n「RMだけの平均2乗誤差」と「全部を使用したときの平均二乗誤差」")
RMS=np.mean((Y_pred - Y_test) ** 2)
RMS_rm=np.mean((Y_rm_pred - Y_test) ** 2)
print(RMS_rm)
print(RMS)