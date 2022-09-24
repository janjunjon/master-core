from ML.Abstract import SKLearn
from netCDF.NetCDF import NetCDF
import numpy as np

class MLNetCDF(SKLearn):
    def __init__(self) -> None:
        super().__init__()
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/rains.nc')
        self.nc_MSMp = NetCDF('/home/jjthomson/fdrive/nc/LowLoadMSMp.nc')

        self.rain_Ra = self.nc_rains.variables['rain_Ra'][:][:][:].tolist()
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs'][:][:][:].tolist()
        self.w = self.nc_MSMp.variables['w'][:][:][:].tolist()
        self.u = self.nc_MSMp.variables['u'][:][:][:].tolist()
        self.v = self.nc_MSMp.variables['v'][:][:][:].tolist()
        self.temp = self.nc_MSMp.variables['temp'][:][:][:].tolist()
        self.rh = self.nc_MSMp.variables['rh'][:][:][:].tolist()

    def predictWithModel(self):
        self.shapeData
        self.model.predict()

    def shapeData(self):
        self.rain_Ra = np.ravel(self.rain_Ra[0])
        self.rain_MSMs = np.ravel(self.rain_MSMs[0])
        self.w = np.ravel(self.w[0])
        self.u = np.ravel(self.u[0])
        self.v = np.ravel(self.v[0])
        self.temp = np.ravel(self.temp[0])
        self.rh = np.ravel(self.rh[0])
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