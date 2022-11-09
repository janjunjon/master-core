import numpy as np

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF
from ML.DR.PCA import PrincipalComponentAnalysis

class Execution(Abstract):
    def __init__(self) -> None:
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

    def main(self):
        PrincipalComponentAnalysis.main(
            n_components=None,
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
        if array.ndim == 1 and len(array) == 253*241:
            array = np.reshape(array, (253, 241))
        elif array.ndim == 1 and len(array) == 253*241*16:
            array = np.reshape(array, (16, 253, 241))
        return array

    def convert(self, array: np.ndarray) -> np.ndarray:
        if array.ndim > 1:
            array = np.ravel(array)
        return array

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
