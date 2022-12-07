from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF

class Coef(Abstract):
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