import numpy as np
import os

from Exception.Exception import *
from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF
from ML.DR.PCA import *
from ML.Other.HeavyRainCases import Indexes

class Execution(Abstract):
    """
    <DimensionalityReduction>
    Execution of Principal Component Analysis
    """
    def __init__(self, indexes=False) -> None:
        super().__init__()
        path_to_combined = '{}/fdrive/nc/reversed'.format(self.parent_path)
        self.ncRain = NetCDF('{}/fdrive/rains.nc'.format(self.parent_path))
        self.ncMSMs = NetCDF('{}/MSMs.nc'.format(path_to_combined))
        self.ncMSMp = NetCDF('{}/MSMp.nc'.format(path_to_combined))
        self.ncDiv = NetCDF('{}/div.nc'.format(path_to_combined))
        self.ncAtmos = NetCDF('{}/atmos.nc'.format(path_to_combined))
        self.varNcRain  = ['rain_Ra', 'rain_MSMs']
        self.varNcMSMs  = ['psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.varNcMSMp  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.varNcDiv   = ['pwv', 'qu', 'qv', 'div']
        self.varNcAtmos = ['pt', 'ept', 'td', 'tl', 'lcl', 'ssi', 'ki']
        self.twoDimVarNames = self.get2DimentionalVarNames()
        self.threeDimVarNames = self.get3DimentionalVarNames()
        self.getVars()
        if indexes:
            instance = Indexes()
            self.indexes = instance.indexes
        else:
            self.indexes = None

    def main(self, pca_save_path, arr_save_path, t=None, start=None, end=None):
        self.getSpecificTime(var_names=self.twoDimVarNames, t=t, start=start, end=end)
        self.convertVars(self.twoDimVarNames)
        # indexes = self.getIndexes()
        # self.getSpecificVars(self.twoDimVarNames, indexes)
        data = PrincipalComponentAnalysis.shapeData(
            rain_MSMs=self.rain_MSMs,
            psea=self.psea,
            sp=self.sp,
            u=self.u,
            v=self.v,
            temp=self.temp,
            rh=self.rh,
            ncld_upper=self.ncld_upper,
            ncld_mid=self.ncld_mid,
            ncld_low=self.ncld_low,
            ncld=self.ncld,
            dswrf=self.dswrf,
            pwv=self.pwv,
            qu=self.qu,
            qv=self.qv,
            div=self.div,
            td=self.td,
            tl=self.tl,
            lcl=self.lcl,
            ssi=self.ssi,
            ki=self.ki,
        )
        feature, pca, df = PrincipalComponentAnalysis.main(n_components=None, X=data)
        self.reshapeVars(self.twoDimVarNames)
        PrincipalComponentAnalysis.savePCA(pca, pca_save_path)
        PrincipalComponentAnalysis.saveArray(feature, arr_save_path)
        # PrincipalComponentAnalysis.saveArray(indexes, '{}/var/PCA/{}'.format(self.root_path, 'PCA_HeavyRainCases_indexes'))
        return feature, pca, df

    def getIndexes(self):
        if not self.indexes:
            indexes = self.getRainExistsIndex(0)
        else:
            indexes = self.indexes
        print(len(indexes))
        return indexes
        
    def getVars(self) -> None:
        for var in self.varNcRain:
            setattr(self, var, self.ncRain.variables[var])
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

    def getRainExistsIndex(self, mm):
        self.rain_Ra = np.array(self.rain_Ra)
        rains = self.rain_Ra.tolist()
        rains = self.convert(rains).tolist()
        Indexes = []
        for i, rain in enumerate(rains):
            if rain > mm:
                Indexes.append(i)
        self.rain_Ra = self.reshape(rains)
        return Indexes

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

class Execution202007(Execution):
    def __init__(self, indexes=False) -> None:
        super().__init__(indexes)

    def each202007(self):
        count = 0
        files = os.listdir('/home/jjthomson/fdrive/nc/div')
        for i, file in enumerate(files):
            filename = file.split('.')[0]
            pca_save_path = '{}/var/PCA/202007/PCA_{}.sav'.format(self.root_path, filename)
            arr_save_path = '{}/var/PCA/202007/PCA_{}'.format(self.root_path, filename)
            if i == 0:
                start = count
                count += 3
                end = count
            elif i == 32:
                start = count
                count += 5
                end = count
            else:
                start = count
                count += 8
                end = count
            self.main(
                pca_save_path=pca_save_path,
                arr_save_path=arr_save_path,
                start=start,
                end=end
            )
            print('DEBUG {}'.format(pca_save_path), start, end)
            
            self.getVars()