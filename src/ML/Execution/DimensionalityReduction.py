import numpy as np

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF
from ML.DR.PCA import PrincipalComponentAnalysis

class Execution(Abstract):
    def __init__(self) -> None:
        super().__init__()
        path_to_combined = '{}/fdrive/nc/combined'.format(self.parent_path)
        self.ncRain = NetCDF('{}/fdrive/rains.nc'.format(self.parent_path))
        self.ncMSMs = NetCDF('{}/MSMs.nc'.format(path_to_combined))
        self.ncMSMp = NetCDF('{}/MSMp.nc'.format(path_to_combined))
        self.ncDiv = NetCDF('{}/div.nc'.format(path_to_combined))
        self.ncAtmos = NetCDF('{}/atmos.nc'.format(path_to_combined))
        self.getVars()

    def main(self):
        PrincipalComponentAnalysis.main(n_components=3)

    def getVars(self) -> None:
        self.rain_Ra = np.array(self.ncRain.variables['rain_Ra'][:].to_list())
        self.rain_MSMs = np.array(self.ncRain.variables['rain_MSMs'][:].to_list())

        self.psea = np.array(self.ncMSMs.variables['psea'][:].to_list())
        self.sp = np.array(self.ncMSMs.variables['sp'][:].to_list())
        self.ncld_upper = np.array(self.ncMSMs.variables['ncld_upper'][:].to_list())
        self.ncld_mid = np.array(self.ncMSMs.variables['ncld_mid'][:].to_list())
        self.ncld_low = np.array(self.ncMSMs.variables['ncld_low'][:].to_list())
        self.ncld = np.array(self.ncMSMs.variables['ncld'][:].to_list())
        self.dswrf = np.array(self.ncMSMs.variables['dswrf'][:].to_list())
        
        self.z = np.array(self.ncMSMp.variables['z'][:].to_list()) # 3 dimension
        self.vv = np.array(self.ncMSMp.variables['w'][:].to_list()) # 3 dimension
        self.u = np.array(self.ncMSMp.variables['u'][:].to_list()) # 3 dimension
        self.v = np.array(self.ncMSMp.variables['v'][:].to_list()) # 3 dimension
        self.temp = np.array(self.ncMSMp.variables['temp'][:].to_list()) # 3 dimension
        self.rh = np.array(self.ncMSMp.variables['rh'][:].to_list()) # 3 dimension
        
        self.w = np.array(self.ncDiv.variables['w'][:].to_list())
        self.qu = np.array(self.ncDiv.variables['qu'][:].to_list())
        self.qv = np.array(self.ncDiv.variables['qv'][:].to_list())
        self.div = np.array(self.ncDiv.variables['div'][:].to_list())
        
        self.pt = np.array(self.ncAtmos.variables['pt'][:].to_list()) # 3 dimension
        self.ept = np.array(self.ncAtmos.variables['ept'][:].to_list()) # 3 dimension
        self.td = np.array(self.ncAtmos.variables['td'][:].to_list())
        self.tl = np.array(self.ncAtmos.variables['tl'][:].to_list())
        self.lcl = np.array(self.ncAtmos.variables['lcl'][:].to_list())
        self.ssi = np.array(self.ncAtmos.variables['ssi'][:].to_list())
        self.ki = np.array(self.ncAtmos.variables['ki'][:].to_list())