import time as Time
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import preprocessing

from Exception.Exception import *
from netCDF.NetCDF import NetCDF
from ML.Other.Abstract import SKLearn
from ML.Other.HeavyRainCases import *
from Module.Draw import Draw
from Module.Array import Array
from Module.CreateNetCDF import CreateNetCDF
from Module.Reverse import Reverse
from Module.Calculation import Calculation as MathCalculation
from Module.CreateGradsFile import Grads

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
        self.varNcMSMs  = ['psea', 'sp', 'u', 'v', 'temp', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.varNcMSMp  = ['z', 'w', 'rh']
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
        sc = preprocessing.StandardScaler()
        sc.fit(X)
        X = sc.transform(X)
        return X, Y

    def shapeXForPredict(self, varnames):
        TIME_X = []
        sc = preprocessing.StandardScaler()
        for time in range(248):
            X = []
            for varname in varnames:
                d = np.ravel(getattr(self, varname)[time]).tolist()
                X.append(d)
            X = Array.getTransposedMatrix(X)
            sc.fit(X)
            X = sc.transform(X)
            TIME_X.append(X)
        print(f'TIME: {len(TIME_X)}, X: {len(TIME_X[0])}, vars: {len(TIME_X[0][0])}')
        return TIME_X

    def shapeXForPCA(self, varnames):
        for varname in varnames:
            d = np.ravel(getattr(self, varname))
            setattr(self, varname, d)

    def predict(self):
        starttime = Time.time()
        self.model = SKLearn.loadModel(self, self.model_path)
        predicted = np.array(self.model.predict(self.X))
        for lat in range(253):
            for lon in range(241):
                if self.rain_MSMs[lat][lon] <= 0:
                    predicted[lat][lon] = self.rain_MSMs[lat][lon]
        print(f'RMSE: {self.calcRMSE()}')
        self.makeFigure(predicted)
        elapsedtime = Time.time() - starttime
        print ("Elapsed time to create: {0} [sec]".format(elapsedtime))

    def predictAll(self, ncSavePath, X):
        starttime = Time.time()
        self.model = SKLearn.loadModel(self, self.model_path)
        lat = self.nc_rains.lat
        lat.reverse()
        RAIN = []
        ALL = []
        DEVIATION = []
        for time in range(248):
            real = np.ravel(self.nc_rains.variables['rain_Ra'][time,:,:])
            data = X[time].tolist()
            indexes = [data.index(vector) for vector in data if vector[0] > 0]
            print(f'TIME: {time}, X: {len(data)}, vars: {len(data[0])}')
            print(f'vector: {data[indexes[0]]}')
            predicted = np.array(self.model.predict(data))
            print(f'predicted: {predicted[indexes[0]]}')
            rain_MSMs = np.ravel(self.rain_MSMs[time])
            # exists = [i for i in predicted if i > 0]
            # print(exists[:10])
            for i in range(253*241):
                if rain_MSMs[i] <= 0:
                    predicted[i] = rain_MSMs[i]
            deviation = self.getSquareDeviation(real, predicted)
            real = np.reshape(real, (253,241))
            real = Reverse.reverseLat(real)
            predicted = np.reshape(predicted, (253,241))
            predicted = Reverse.reverseLat(predicted)
            deviation = np.reshape(deviation, (253,241))
            deviation = Reverse.reverseLat(deviation)
            RAIN.append(real)
            ALL.append(predicted)
            DEVIATION.append(deviation)
        print(f'deviation: TIME: {len(DEVIATION)}, LAT: {len(DEVIATION[0])}, LON: {len(DEVIATION[0][0])}')
        CreateNetCDF.createNcFilePredict(
            path=ncSavePath,
            filename='20200701',
            lonList=self.nc_rains.lon,
            latList=lat,
            timeList=self.nc_rains.time,
            real=RAIN,
            predict=ALL,
            deviation=DEVIATION
        )
        elapsedtime = Time.time() - starttime
        print ("Elapsed time to correct: {0} [sec]".format(elapsedtime))
    
    def predictAllNonLinear(self, ncSavePath, X):
        starttime = Time.time()
        self.model = SKLearn.loadModel(self, self.model_path)
        lat = self.nc_rains.lat
        lat.reverse()
        RAIN = []
        ALL = []
        DEVIATION = []
        for time in range(248):
            real = np.ravel(self.nc_rains.variables['rain_Ra'][time,:,:])
            data = X[time].tolist()
            indexes = [data.index(vector) for vector in data if vector[0] > 0]
            print(f'TIME: {time}, X: {len(data)}, vars: {len(data[0])}')
            print(f'vector: {data[indexes[0]]}')
            length = len(data[0])
            poly = PolynomialFeatures(length)
            data = poly.fit_transform(data)
            predicted = np.array(self.model.predict(data))
            print(f'predicted: {predicted[indexes[0]]}')
            rain_MSMs = np.ravel(self.rain_MSMs[time])
            # exists = [i for i in predicted if i > 0]
            # print(exists[:10])
            for i in range(253*241):
                if rain_MSMs[i] <= 0:
                    predicted[i] = rain_MSMs[i]
            deviation = self.getSquareDeviation(real, predicted)
            real = np.reshape(real, (253,241))
            real = Reverse.reverseLat(real)
            predicted = np.reshape(predicted, (253,241))
            predicted = Reverse.reverseLat(predicted)
            deviation = np.reshape(deviation, (253,241))
            deviation = Reverse.reverseLat(deviation)
            RAIN.append(real)
            ALL.append(predicted)
            DEVIATION.append(deviation)
        print(f'deviation: TIME: {len(DEVIATION)}, LAT: {len(DEVIATION[0])}, LON: {len(DEVIATION[0][0])}')
        CreateNetCDF.createNcFilePredict(
            path=ncSavePath,
            filename='20200701',
            lonList=self.nc_rains.lon,
            latList=lat,
            timeList=self.nc_rains.time,
            real=RAIN,
            predict=ALL,
            deviation=DEVIATION
        )
        elapsedtime = Time.time() - starttime
        print ("Elapsed time to correct: {0} [sec]".format(elapsedtime))

    def makeFigure(self, var):
        d = Draw()
        d.drawMapByArrayNotMultidimensional(
            v_array=var,
            v_lat=self.nc_rains.lat,
            v_lon=self.nc_rains.lon,
            path=self.save_path,
            region=self.region
        )

    def getSquareDeviation(self, X, Y):
        deviation = np.array([(x - y) ** 2 for (x, y) in zip(X, Y)])
        return deviation

    def calcCorrelationCoefficient(self, B):
        indexes = np.load(file='/home/jjthomson/master-core/var/Data/undef.npy')
        A = np.ravel(self.nc_rains.variables['rain_Ra'])
        B = np.ravel(B)
        print(f'A: {len(A)}')
        X = []
        Y = []
        for index in indexes:
            X.append(A[index])
            Y.append(B[index])
        print(f'X: {len(X)}')
        corrcoef_ = MathCalculation.corrcoef_(X, Y)
        print(corrcoef_)

    def createGradsFiles(self, ctl_path, gs_path, dirPath):
        Grads.createCtlFileV3Results(ctl_path, dirPath)
        Grads.createGsFileV3Results(gs_path, dirPath)

    def setPCAComponents(self):
        setattr(self, 'rain_MSMs', self.nc_rains.variables['rain_MSMs'][:].tolist())
        nc_pca1 = NetCDF('/home/jjthomson/fdrive/nc/PCA/pattern1.nc')
        nc_pca2 = NetCDF('/home/jjthomson/fdrive/nc/PCA/pattern2.nc')
        nc_pca3 = NetCDF('/home/jjthomson/fdrive/nc/PCA/pattern3.nc')
        nc_pca4 = NetCDF('/home/jjthomson/fdrive/nc/PCA/pattern4.nc')
        # varnames1 = ['component1', 'component2']
        # varnames2 = ['component1', 'component2']
        # varnames3 = ['component1', 'component2', 'component3']
        # varnames4 = ['component1', 'component2', 'component3', 'component4']
        varnames = ['component1', 'component2']
        for varname in varnames:
            for i in range(1,5):
                setattr(self, f'pca{i}_{varname}', locals()[f'nc_pca{i}'].variables[varname][:])