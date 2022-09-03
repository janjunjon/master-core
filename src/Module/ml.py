from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# ライブラリーのインポート
from sklearn.linear_model import LinearRegression

# スコア計算のためのライブラリ
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

def _returnTestTrainData(x, y):
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=1
    )
    return x_train, x_test, y_train, y_test

def _normalizeData(x_train, x_test):
    sc = StandardScaler()
    sc.fit(x_train)
    x_train_std = sc.transform(x_train)
    x_test_std = sc.transform(x_test)
    return x_train_std, x_test_std

def _makeModel(x_train_std, x_test_std, y_train, y_test):
    # モデルの学習
    lr = LinearRegression()
    lr.fit(x_train_std, y_train)

    # 回帰　
    pred_lr = lr.predict(x_test_std)

    # 評価
    # 決定係数(R2)
    r2_lr = r2_score(y_test, pred_lr)

    # 平均絶対誤差(MAE)
    mae_lr = mean_absolute_error(y_test, pred_lr)

    print("R2 : %.3f" % r2_lr)
    print("MAE : %.3f" % mae_lr)

    # 回帰係数
    print("Coef = ", lr.coef_)
    # 切片
    print("Intercept =", lr.intercept_)