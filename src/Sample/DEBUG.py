import numpy as np
import random
import struct
from sys import byteorder

from sklearn.decomposition import PCA

from netCDF.NetCDF import NetCDF

class Sample:
    def __init__(self) -> None:
        self.rain_Ra = 'ra'
        self.rain_MSMs = 'r1h'
        self.div = 'div'

    def getLocalVars(self):
        var = ['rain_Ra', 'rain_MSMs', 'div']
        for i in range(len(var)):
        #     var_name = var[i]
        #     # locals()['self.{}'.format(var_name)] = range(i)
        #     print('self.{}'.format(var_name))
        #     print(locals()['self.{}'.format(var_name)])
            setattr(self, var[i], range(i))
            if var[i] == 'rain_Ra': print(self.rain_Ra)
        print(locals())

    def debug(self):
        chrs = [chr(i) for i in range(ord('a'), ord('z')+1)]
        names = [''.join(random.sample(chrs, 10)) for i in range(10)]
        for i in range(10):
            locals()[names[i]] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            print(locals()[names[i]])

    def comfirmImage(self):
        ncMSMs = NetCDF('/home/jjthomson/fdrive/nc/reversed/MSMs.nc')
        ncRain = NetCDF('/home/jjthomson/fdrive/nc/rains.nc')

    def PCAdebug(self):
        x = np.linspace(0.2,1,100)
        y = 0.8*x + np.random.randn(100)*0.1
        print(x)
        print(y)
        X = np.vstack([x, y]).T
        print(len(X), len(X[0]), X)
        np.random.shuffle(X)
        pca = PCA(n_components=2)
        pca.fit(X)
        # PCA(copy=True, n_components=2, whiten=False)

    def arraydebug(self):
        locals()['arr'] = np.array([
            [
                [1,2,3,4,5],
                [1,2,3,4,5]
            ],
            [
                [1,2,3,4,5],
                [1,2,3,4,5]
            ]
        ])
        print(locals()['arr'], locals()['arr'].ndim)
        locals()['arr'] = np.append(
            locals()['arr'],
            np.array([
                [
                    [6,7,8,9,10],
                    [6,7,8,9,10]
                ],
                [
                    [6,7,8,9,10],
                    [6,7,8,9,10]
                ]
            ]),
            axis=0
        )
        print(locals()['arr'], locals()['arr'].ndim)

    def debugbinary(self, path):
        rain = []
        i = 0
        with open(path, "rb") as f:
            while True:
                data=f.read(2)
                if data=="":
                    break
                rain.append(data)
                if i < 10: print(data.decode())
                i=i+1
        print(rain[:10])
        return data

    def debugCreateImage(self):
        nc = NetCDF('/home/jjthomson/fdrive/nc/predict/v3/Rain/SDGRegressor/preparation.nc')
        print(nc.lat)
        rain = nc.variables['rain'][:,:,:]
        nc.drawMapByArray(rain, nc.lat, nc.lon, 24, '/home/jjthomson/fdrive/images/DEBUG/python/DEBUG_preparation_t=24.png')