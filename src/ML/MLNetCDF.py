from ML.Abstract import SKLearn
from Module.Draw import Draw

from netCDF.NetCDF import NetCDF
import numpy as np

class MLNetCDF(SKLearn):
    def __init__(self) -> None:
        super().__init__()
        self.model = self.loadModel('{}/var/MLModels/SDGRegressor_all.sav'.format(self.root_path))
        self.save_path = '/home/jjthomson/fdrive/images/predict/predictedRain20200703_0300JST_HeavyRain02.png'
        self.region = [22, 48, 120, 150]
        self.predicted_time_step = 24

        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_MSMp = NetCDF('/home/jjthomson/fdrive/nc/LowLoadMSMp.nc')
        self.lat = self.nc_rains.variables['lat'][:].tolist()
        self.lon = self.nc_rains.variables['lon'][:].tolist()
        self.rain_Ra = self.nc_rains.variables['rain_Ra'][:][:][:].tolist()
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs'][:][:][:].tolist()
        self.w = self.nc_MSMp.variables['w'][:][:][:].tolist()
        self.u = self.nc_MSMp.variables['u'][:][:][:].tolist()
        self.v = self.nc_MSMp.variables['v'][:][:][:].tolist()
        self.temp = self.nc_MSMp.variables['temp'][:][:][:].tolist()
        self.rh = self.nc_MSMp.variables['rh'][:][:][:].tolist()

    def predict(self):
        X, Y = self.shapeData()
        predicted = self.model.predict(X)
        predicted = np.array(predicted)
        for i in range(len(predicted)):
            if self.rain_MSMs[i] < 5:
                predicted[i] = 0
            if self.rain_MSMs[i] < 10:
                predicted[i] = self.rain_MSMs[i]
        predicted = predicted.reshape([253, 241])
        self.predicted = predicted
        print(self.calcRMSE())
        # self.makeFigure(self.predicted)

    def shapeData(self):
        i = self.predicted_time_step
        self.rain_Ra = np.ravel(self.rain_Ra[i])
        self.rain_MSMs = np.ravel(self.rain_MSMs[i])
        self.w = np.ravel(self.w[i])
        self.u = np.ravel(self.u[i])
        self.v = np.ravel(self.v[i])
        self.temp = np.ravel(self.temp[i])
        self.rh = np.ravel(self.rh[i])
        Y = []
        X = []
        for i in range(len(self.rain_Ra)):
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
        return X, Y

    def makeFigure(self, var):
        d = Draw()
        d.drawMapByArrayNotMultidimensional(
            v_array=var,
            v_lat=self.lat,
            v_lon=self.lon,
            path=self.save_path,
            region=self.region
        )

    def calcRMSE(self):
        t = self.predicted_time_step
        X = np.ravel(self.rain_Ra[t])
        # Y = np.ravel(self.rain_MSMs[t])
        Y = np.ravel(self.predicted)
        deviation = [(x - y) ** 2 for (x, y) in zip(X, Y)]
        RMSE = np.mean(deviation)
        return RMSE