import numpy as np

from Exception.Exception import *
from netCDF.NetCDF import NetCDF
from ML.Other.Abstract import SKLearn
from ML.Other.HeavyRainCases import *
from Module.Draw import Draw
from Module.Array import Array
from Module.CreateNetCDF import CreateNetCDF
from Module.Calculation import Calculation as MathCalculation

class Setter(SKLearn):
    def __init__(self) -> None:
        super().__init__()

        self.region = [22, 48, 120, 150]
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/combined/rains.nc')
        self.Y = self.nc_rains.variables['rain_Ra'][:].tolist()
        self.ncMSMs = NetCDF('/home/jjthomson/fdrive/nc/combined/MSMs.nc')
        self.ncMSMp = NetCDF('/home/jjthomson/fdrive/nc/combined/MSMp.nc')
        self.ncDiv = NetCDF('/home/jjthomson/fdrive/nc/combined/div.nc')
        self.ncAtmos = NetCDF('/home/jjthomson/fdrive/nc/combined/atmos.nc')
        self.varNcMSMs  = ['psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.varNcMSMp  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.varNcDiv   = ['pwv', 'qu', 'qv', 'div']
        self.varNcAtmos = ['pt', 'ept', 'td', 'tl', 'lcl', 'ssi', 'ki', 'uvs', 'vvs']
        self.predicted_time_step = 24
        # self.getVars()

    @property
    def X(self):
        pass
    
    @X.getter
    def X(self):
        return self.__X

    @X.setter
    def X(self, X):
        self.__X = X

    def setSpecificVars(self, vars):
        for var in vars:
            if var == 'rain_MSMs':
                setattr(self, var, self.nc_rains.variables['rain_MSMs'][:].tolist())
            elif var in self.varNcMSMs:
                setattr(self, var, self.ncMSMs.variables[var][:].tolist())
            elif var in self.varNcMSMp:
                if var in ['rh']:
                    setattr(self, f'{var}950hPa', self.ncMSMp.variables[var][:,2,:,:].tolist())
                    setattr(self, f'{var}700hPa', self.ncMSMp.variables[var][:,7,:,:].tolist())
                    setattr(self, f'{var}500hPa', self.ncMSMp.variables[var][:,9,:,:].tolist())
                else:
                    continue
            elif var in self.varNcDiv:
                setattr(self, var, self.ncDiv.variables[var][:].tolist())
            elif var in self.varNcAtmos:
                if var in ['pt', 'ept']:
                    setattr(self, f'{var}950hPa', self.ncAtmos.variables[var][:,2,:,:].tolist())
                    setattr(self, f'{var}700hPa', self.ncAtmos.variables[var][:,7,:,:].tolist())
                    setattr(self, f'{var}500hPa', self.ncAtmos.variables[var][:,9,:,:].tolist())
                else:
                    setattr(self, var, self.ncAtmos.variables[var][:].tolist())


    def getVars(self) -> None:
        for var in self.varNcMSMs:
            setattr(self, var, self.ncMSMs.variables[var][:].tolist())
        for var in self.varNcMSMp:
            if var in ['rh']:
                setattr(self, f'{var}950hPa', self.ncMSMp.variables[var][:,2,:,:].tolist())
                setattr(self, f'{var}700hPa', self.ncMSMp.variables[var][:,7,:,:].tolist())
                setattr(self, f'{var}500hPa', self.ncMSMp.variables[var][:,9,:,:].tolist())
            else:
                continue
        for var in self.varNcDiv:
            setattr(self, var, self.ncDiv.variables[var][:].tolist())
        for var in self.varNcAtmos:
            if var in ['pt', 'ept']:
                setattr(self, f'{var}950hPa', self.ncAtmos.variables[var][:,2,:,:].tolist())
                setattr(self, f'{var}700hPa', self.ncAtmos.variables[var][:,7,:,:].tolist())
                setattr(self, f'{var}500hPa', self.ncAtmos.variables[var][:,9,:,:].tolist())
            else:
                setattr(self, var, self.ncAtmos.variables[var][:].tolist())

    def reshapeVars(self, var_names) -> None:
        for var_name in var_names:
            setattr(self, var_name, self.reshape(getattr(self, var_name)))

    def convertVars(self, var_names) -> None:
        for var_name in var_names:
            setattr(self, var_name, self.convert(getattr(self, var_name)))

    def reshape(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        if array.ndim == 1 and len(array) == 253*241:
            array = np.reshape(array, (253, 241))
        elif array.ndim == 1 and len(array) == 253*241*16:
            array = np.reshape(array, (16, 253, 241))
        return array

    def convert(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        if array.ndim > 1:
            array = np.ravel(array)
        return array

    def shapeXY(self, indexes, varnames):
        X = []
        for varname in varnames:
            d = np.ravel(getattr(self, varname)).tolist()
            addData = []
            for i in indexes:
                addData.append(d[i])
            X.append(addData)
        X = Array.getTransposedMatrix(X)
        Y = []
        d = np.ravel(self.Y)
        for i in indexes:
            Y.append([d[i]])
        print(f'X: {len(X)}, vars: {len(X[0])}')
        print(f'Y: {len(Y)}, vars: {len(Y[0])}')
        return X, Y

    def shapeXYForPredict(self, indexes, varnames):
        TIME_X = []
        TIME_Y = []
        for time in range(248):
            X = []
            for varname in varnames:
                d = np.ravel(getattr(self, varname)[time]).tolist()
                addData = []
                for i in indexes:
                    addData.append(d[i])
                X.append(addData)
            X = Array.getTransposedMatrix(X)
            TIME_X.append(X)
            Y = []
            d = np.ravel(self.Y)
            for i in indexes:
                Y.append([d[i]])
            TIME_Y.append(Y)
        print(f'TIME: {len(X)}, X: {len(X[0])}, vars: {len(X[0][0])}')
        print(f'TIME: {len(Y)}, Y: {len(Y[0])}, vars: {len(Y[0][0])}')
        return X, Y

    def predict(self):
        self.model = SKLearn.loadModel(self, self.model_path)
        predicted = np.array(self.model.predict(self.X))
        for lat in range(253):
            for lon in range(241):
                if self.rain_MSMs[lat][lon] <= 0:
                    predicted[lat][lon] = self.rain_MSMs[lat][lon]
        print(f'RMSE: {self.calcRMSE()}')
        self.makeFigure(predicted)

    def predictAll(self, ncSavePath):
        ALL = []
        for time in range(248):
            self.model = SKLearn.loadModel(self, self.model_path)
            predicted = np.array(self.model.predict(self.X[time]))
            for lat in range(253):
                for lon in range(241):
                    if self.rain_MSMs[lat][lon] <= 0:
                        predicted[lat][lon] = self.rain_MSMs[lat][lon]
            ALL.append(predicted)
        CreateNetCDF.createNcFilePredict(
            path=ncSavePath,
            filename='20200701',
            lonList=self.nc_rains.lon,
            latList=self.nc_rains.lat,
            timeList=self.nc_rains.time,
            predict=ALL
        )

    def makeFigure(self, var):
        d = Draw()
        d.drawMapByArrayNotMultidimensional(
            v_array=var,
            v_lat=self.nc_rains.lat,
            v_lon=self.nc_rains.lon,
            path=self.save_path,
            region=self.region
        )

    def calcRMSE(self):
        t = self.predicted_time_step
        X = np.ravel(self.rain_Ra[t])
        # Y = np.ravel(self.rain_MSMs[t])
        Y = np.ravel(self.predicted)
        deviation = np.array([(x - y) ** 2 for (x, y) in zip(X, Y)])
        RMSE = pow(np.mean(deviation), 0.5)
        return RMSE