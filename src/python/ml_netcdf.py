# -*- coding: utf-8 -*-
"""ML_netCDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I00FxREqrVlRPcsPvO7T59zichBZNFUd
"""

import netCDF4
# from google.colab import drive

# drive.mount('/content/drive')

# !ls drive/MyDrive/data/MSM
# !mv 'drive/MyDrive/data/MSM/0707.nc' 'drive/MyDrive/data/MSM/20210707.nc'

filename1 = 'drive/MyDrive/data/MSM/p20200704.nc'
filename2 = 'drive/MyDrive/data/MSM/s20200704.nc'
filename3 = 'drive/MyDrive/data/MSM/div20200704.nc'
filename4 = 'drive/MyDrive/data/MSM/ra20200704.nc'
nc_p = netCDF4.Dataset(filename1)
nc_s = netCDF4.Dataset(filename2)
nc_div = netCDF4.Dataset(filename3)
nc_ra = netCDF4.Dataset(filename4)

# nc_s.dimensions
# nc_p.variables.keys()
nc_s.variables.keys()
# nc_s.variables['r1h']
# nc_p['lat']
# nc_s['r1h']
# nc.history

nc_div

nc_ra
# nc_ra.dimensions
# nc_ra['p']

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# !pip3 install https://github.com/matplotlib/basemap/archive/master.zip
# !pip install pyproj==1.9.6
# !pip install git+https://github.com/matplotlib/basemap#subdirectory=packages/basemap
from mpl_toolkits.basemap import Basemap

# <time=0, p=0, lat=0, lon=0の時の>
# float(nc['temp'][0][:][0][0])
# len(temp)
# temp[0][0]

# <配列に>
# var = np.array(nc_div['div'][0][:][:])
# Lo = np.array(nc_div['lon'])
# La = np.array(nc_div['lat'])
var = np.array(nc_ra['p'][0][:][:])
Lo = np.array(nc_ra['lon'])
La = np.array(nc_ra['lat'])
Lon, Lat = np.meshgrid(Lo, La)

#plot with Matplotlib
fig=plt.figure(figsize=(10,10))
#set the color interval
interval=list(np.arange(200,300,10)) 
# interval=list(np.arange(0,100,5)) 
# interval.insert(0,0.1)
#set colormap
cmap=cm.jet
cmap.set_under('w', alpha=0)

#set map
m=Basemap(
    projection='cyl',
    resolution='i',
    llcrnrlat=30,
    urcrnrlat=35,
    llcrnrlon=128,
    urcrnrlon=133
    )
m.drawcoastlines(color='black')
m.drawmeridians(np.arange(128,133,0.5))
m.drawparallels(np.arange(30,35,0.5))
x,y=m(Lon, Lat) #compute map projection
im=plt.contourf(x, y, var, interval, cmap=cmap, latlon=True)
# set colorbar
cb=m.colorbar(im, "right", size="2.5%")

plt.show()
plt.close()

# time=24, lat=505, lon=481
# 引数はtime,lat,lonの順

# 散布図
a=[]
b=[]
# c=[]
# d=[]

for h in nc_ra['p'][:][:][:]:
  for i in h:
    for j in i:
      a.append(j/3)

for h in nc_div['div'][:][:][:]:
  for i in h:
    for j in i:
      b.append(j)

# for h in nc_s['rh'][:][:][:]:
#   for i in h:
#     for j in i:
#       c.append(j)

# for h in nc_s['temp'][:][:][:]:
#   for i in h:
#     for j in i:
#       d.append(j)

x=a
y=b

# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに散布図を設定する
ax.scatter(x, y, c='b')
 
# 表示する
plt.show()

import sklearn

# 目的変数：降水量、説明変数：水蒸気収束量
# train t=1,2,3,4,5,6,7
# validation t=8

# ライブラリーのインポート
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 学習データと評価データを作成
# y=f(x)
x=nc_ra['p'][0][:][:]
y=nc_div['div'][0][:][:]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

#データを標準化
sc = StandardScaler()
sc.fit(x_train) #学習用データで標準化
x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

# ライブラリーのインポート
from sklearn.linear_model import LinearRegression

# スコア計算のためのライブラリ
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

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