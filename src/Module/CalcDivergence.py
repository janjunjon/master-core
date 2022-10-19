import numpy as np
from windspharm.standard import *
import xarray

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF

# 一旦保留
class Calculation(Abstract):
    def __init__(self) -> None:
        super().__init__()
        self.MSMp = NetCDF('/home/jjthomson/fdrive/nc/data/p20200701.nc')
        self.ConvertedMSMs = NetCDF('/home/jjthomson/fdrive/nc/converted/20200701.nc')
        self.sp = np.array(self.ConvertedMSMs.variables['sp'][:][:][:].tolist())
        lat = self.MSMp.variables['lat'][:].tolist()
        self.lat = np.array(lat)
        self.lon = np.array(self.MSMp.variables['lon'][:].tolist())
        self.p = np.array(self.MSMp.variables['p'][:].tolist())
        self.temp = np.array(self.MSMp.variables['temp'][:][:][:][:].tolist())
        self.z = np.array(self.MSMp.variables['z'][:][:][:][:].tolist())
        self.u = np.array(self.MSMp.variables['u'][:][:][:][:].tolist())
        self.v = np.array(self.MSMp.variables['v'][:][:][:][:].tolist())
        self.rh = np.array(self.MSMp.variables['rh'][:][:][:][:].tolist())

    def main(self):
        pass

    def divergence(self, qu, qv):
        qu = xarray.DataArray(
            data=qu,
            dims=['latitude', 'longitude'],
            coords=[('latitude', self.lat), ('longitude', self.lon)]
        )
        qv = xarray.DataArray(
            data=qv,
            dims=['latitude', 'longitude'],
            coords=[('latitude', self.lat), ('longitude', self.lon)]
        )
        w = VectorWind(qu, qv, gridtype='regular')
        DIV = w.divergence(truncation=13)
        # U = np.ravel(qu)
        # V = np.ravel(qv)
        # DIV = []
        # for u in U:
        #     for v in V:
        #         w = VectorWind(u, v)
        #         div = w.divergence()
        #         DIV.append(div)
        # DIV = np.array(DIV)
        return DIV
    
    def calc1000hPa(self, time):
        p = 0
        sp = np.ravel(self.sp[time, :, :] / 100)
        pres = np.array([987.5]*253*241)
        temp = self.temp[time, p, :, :]
        u = self.u[time, p, :, :]
        v = self.v[time, p, :, :]
        rh = self.rh[time, p, :, :]
        esat = 6.1078 * pow(10, 7.5 * (temp - 273.15)/(237.3 + (temp - 273.15)))
        e = esat * rh / 100
        q = (0.622 * (e / 1000)) / (1 - 0.378 * (e / 1000))
        X = []
        for i in range(len(pres)):
            if sp[i] >= pres[i]:
                x = sp[i] - pres[i]
            else:
                x = 0
            X.append(x)
        X = np.array(X).reshape(253, 241)
        w = q * X * 100
        qu = u * w
        qv = v * w
        qu = np.ma.MaskedArray(qu)
        qv = np.ma.MaskedArray(qv)
        div = self.divergence(qu, qv)
        return w, qu, qv, div
    
    def calc975hPa(self, time):
        p = 0
        sp = self.sp[time, :, :] / 100
        temp = self.temp[time, p, :, :]
        u = self.u[time, p, :, :]
        v = self.v[time, p, :, :]
        rh = self.rh[time, p, :, :]
        esat = 6.1078 * pow(10, 7.5 * (temp - 273.15)/(237.3 + (temp - 273.15)))
        e = esat * rh / 100
        q = (0.622 * (e / 1000)) / (1 - 0.378 * (e / 1000))
        if 987.5 >= sp > 975:
            x1 = sp - 975
            x2 = 975 - 962.5
            x = x1 + x2
        elif 975 >= sp >= 962.5:
            x = sp - 962.5
        else:
            x = 0
        w = q * x * 100
        qu = u * w
        qv = v * w
        a = pow((pow(qu, 2) + pow(qv, 2)), 0.5)
        return w, qu, qv, a

# --------------------------------------------------------------------------------

    # not used
    # def calcDivergence(self, qu, qv):
    #     # [lat, lon]
    #     for i in range(253):
    #         for j in range(241):
    #             if not i-1 < 0 and not j-1 < 0 and not i+1 > 252 and not j+1 > 240:
    #                 nextNS = qv[i+1, j]
    #                 prevNS = qv[i-1, j]
    #                 nextEW = qu[i, j+1]
    #                 prevEW = qu[i, j-1]
    #                 NS = nextNS - prevNS
    #                 EW = nextEW - prevEW
    #                 a = NS/ + EW
    #     return a