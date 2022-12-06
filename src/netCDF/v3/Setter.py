import numpy as np

from Exception.Exception import *
from netCDF.NetCDF import NetCDF
from ML.Other.Abstract import SKLearn
from ML.Other.HeavyRainCases import *
from Module.Draw import Draw
from Module.Array import Array
from Module.Calculation import Calculation as MathCalculation

class Setter(SKLearn):
    def __init__(self) -> None:
        super().__init__()
        self.model = self.loadModel(
            '{}/var/MLModels/v2/SDGRegressor_PCA_Rain.sav'.format(self.root_path)
        )
        self.save_path = '/home/jjthomson/fdrive/images/predict/PCA/predictedRain20200703_0300JST_Rain01.png'
        self.region = [22, 48, 120, 150]
        self.nc_rains = NetCDF('/home/jjthomson/fdrive/nc/recreated/rains2.nc')
        self.rain_Ra = self.nc_rains.variables['rain_Ra'][:]
        self.rain_MSMs = self.nc_rains.variables['rain_MSMs'][:]
        self.ncMSMs = NetCDF('/home/jjthomson/fdrive/nc/reversed/MSMs.nc')
        self.ncMSMp = NetCDF('/home/jjthomson/fdrive/nc/reversed/MSMp.nc')
        self.ncDiv = NetCDF('/home/jjthomson/fdrive/nc/reversed/div.nc')
        self.ncAtmos = NetCDF('/home/jjthomson/fdrive/nc/reversed/atmos.nc')
        self.varNcMSMs  = ['psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.varNcMSMp  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.varNcDiv   = ['pwv', 'qu', 'qv', 'div']
        self.varNcAtmos = ['pt', 'ept', 'td', 'tl', 'lcl', 'ssi', 'ki', 'uvs', 'vvs']
        self.predicted_time_step = 24
        self.getVars()

    def getVars(self) -> None:
        for var in self.varNcMSMs:
            setattr(self, var, self.ncMSMs.variables[var])
        for var in self.varNcMSMp:
            setattr(self, var, self.ncMSMp.variables[var])
        for var in self.varNcDiv:
            setattr(self, var, self.ncDiv.variables[var])
        for var in self.varNcAtmos:
            setattr(self, var, self.ncAtmos.variables[var])

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

    def getSpecificVars(self, var_names, Indexes):
        for var_name in var_names:
            X = []
            for i in Indexes:
                specificVar = getattr(self, var_name)[i]
                X.append(specificVar)
            setattr(self, var_name, X)

    def getSpecificTime(self, var_names, t=None, start=None, end=None):
        for var_name in var_names:
            if t != None:
                specificVar = getattr(self, var_name)[t]
            elif start != None and end != None:
                specificVar = getattr(self, var_name)[start:end]
            else:
                raise SetError('time step is invalid.')
            setattr(self, var_name, specificVar)

    def getAllVarsName(self):
        var_names = []
        var_names.extend(self.varNcRain)
        var_names.extend(self.varNcMSMs)
        var_names.extend(self.varNcMSMp)
        var_names.extend(self.varNcDiv)
        var_names.extend(self.varNcAtmos)
        return var_names

    def get2DimentionalVarNames(self):
        var_names = []
        var_names.extend(self.varNcRain)
        var_names.extend(self.varNcMSMs)
        var_names.extend(self.varNcDiv)
        out = ['pt', 'ept']
        arr = [self.varNcAtmos[i] for i in np.arange(len(self.varNcAtmos)) if self.varNcAtmos[i] not in out]
        var_names.extend(arr)
        return var_names

    def get3DimentionalVarNames(self):
        var_names = []
        var_names.extend(self.varNcMSMp)
        out = ['td', 'tl', 'lcl', 'ssi', 'ki']
        arr = [self.varNcAtmos[i] for i in np.arange(len(self.varNcAtmos)) if self.varNcAtmos[i] not in out]
        var_names.extend(arr)
        return var_names