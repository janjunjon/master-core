import numpy as np
from windspharm.standard import *
import xarray

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF

class Calculation(Abstract):
    def __init__(self, path_MSMp, path_ConvertedMSMs) -> None:
        super().__init__()
        # self.MSMp = NetCDF('/home/jjthomson/fdrive/nc/data/p20200701.nc')
        # self.ConvertedMSMs = NetCDF('/home/jjthomson/fdrive/nc/converted/20200701.nc')        
        self.MSMp = NetCDF(path_MSMp)
        self.ConvertedMSMs = NetCDF(path_ConvertedMSMs)
        self.sp = np.array(self.ConvertedMSMs.variables['sp'][:][:][:].tolist())
        lat = self.MSMp.variables['lat'][:].tolist()
        self.lat = np.array(lat)
        self.lon = np.array(self.MSMp.variables['lon'][:].tolist())
        self.time = np.array(self.MSMp.variables['time'][:].tolist())
        self.p = np.array(self.MSMp.variables['p'][:].tolist())
        self.temp = np.array(self.MSMp.variables['temp'][:][:][:][:].tolist())
        self.z = np.array(self.MSMp.variables['z'][:][:][:][:].tolist())
        self.u = np.array(self.MSMp.variables['u'][:][:][:][:].tolist())
        self.v = np.array(self.MSMp.variables['v'][:][:][:][:].tolist())
        self.rh = np.array(self.MSMp.variables['rh'][:][:][:][:].tolist())
        # self.main()

    def main(self):
        W, QU, QV, DIV = [], [], [], []
        for i in range(8):
            w, qu, qv, div = self.sumEachPres(i)
            W.append(w)
            QU.append(qu)
            QV.append(qv)
            DIV.append(div)
        self.w = W
        self.qu = QU
        self.qv = QV
        self.div = DIV

    def divergence(self, qu, qv):
        # qu = np.ma.MaskedArray(qu)
        # qv = np.ma.MaskedArray(qv)

        # xarray.VectorWind: xarray, standard.VectorWind: ndarray or numpy.ma.MaskedArray
        # qu = xarray.DataArray(
        #     data=qu,
        #     dims=['latitude', 'longitude'],
        #     coords=[('latitude', self.lat), ('longitude', self.lon)]
        # )
        # qv = xarray.DataArray(
        #     data=qv,
        #     dims=['latitude', 'longitude'],
        #     coords=[('latitude', self.lat), ('longitude', self.lon)]
        # )

        w = VectorWind(qu, qv, gridtype='regular')
        DIV = w.divergence()
        return DIV

    def sumEachPres(self, time):
        w1000, qu1000, qv1000, div1000 = self.calc1000hPa(time)
        w975, qu975, qv975, div975 = self.calc975hPa(time)
        w950, qu950, qv950, div950 = self.calc950hPa(time)
        w925, qu925, qv925, div925 = self.calc925hPa(time)
        w900, qu900, qv900, div900 = self.calc900hPa(time)
        w850, qu850, qv850, div850 = self.calc850hPa(time)
        w800, qu800, qv800, div800 = self.calc800hPa(time)
        w700, qu700, qv700, div700 = self.calc700hPa(time)
        w600, qu600, qv600, div600 = self.calc600hPa(time)
        w500, qu500, qv500, div500 = self.calc500hPa(time)
        w400, qu400, qv400, div400 = self.calc400hPa(time)
        w300, qu300, qv300, div300 = self.calc300hPa(time)
        w250, qu250, qv250, div250 = self.calc250hPa(time)
        w200, qu200, qv200, div200 = self.calc200hPa(time)
        w150, qu150, qv150, div150 = self.calc150hPa(time)
        w100, qu100, qv100, div100 = self.calc100hPa(time)
        W = (w1000 + w975 + w950 + w925 + w900 + w850 + w800 + w700 + w600 + w500 + w400 + w300 + w250 + w200 + w150 + w100) / 9.81
        QU = (qu1000 + qu975 + qu950 + qu925 + qu900 + qu850 + qu800 + qu700 + qu600 + qu500 + qu400 + qu300 + qu250 + qu200 + qu150 + qu100) / 9.81
        QV = (qv1000 + qv975 + qv950 + qv925 + qv900 + qv850 + qv800 + qv700 + qv600 + qv500 + qv400 + qv300 + qv250 + qv200 + qv150 + qv100) / 9.81
        DIV = (div1000 + div975 + div950 + div925 + div900 + div850 + div800 + div700 + div600 + div500 + div400 + div300 + div250 + div200 + div150 + div100) / 9.81 * 60 * 60 * 3
        return W, QU, QV, DIV

    def calcVars(self, i, time, lower, upper):
        sp = np.ravel(self.sp[time, :, :] / 100)
        lower_pres = np.array([lower]*253*241) if lower != None else 'None'
        p = np.array([self.p[i]]*253*241) 
        upper_pres = np.array([upper]*253*241) if upper != None else 'None'
        temp = np.ravel(self.temp[time, i, :, :])
        u = np.ravel(self.u[time, i, :, :])
        v = np.ravel(self.v[time, i, :, :])
        rh = np.ravel(self.rh[time, i, :, :])
        X = self.getHeight(p, sp, lower_pres, upper_pres)
        W, QU, QV = [], [], []
        for i in range(253*241):
            esat = 6.1078 * pow(10, 7.5 * (temp[i] - 273.15)/(237.3 + (temp[i] - 273.15)))
            e = esat * rh[i] / 100
            q = (0.622 * (e / p[0])) / (1 - 0.378 * (e / p[0]))
            w = q * X[i] * 100
            qu = u[i] * w
            qv = v[i] * w
            W.append(w)
            QU.append(qu)
            QV.append(qv)
        W = self.shape(W)
        QU = self.shape(QU)
        QV = self.shape(QV)
        DIV = self.divergence(QU, QV)
        return W, QU, QV, DIV

    def getHeight(self, p, sp, lower_pres, upper_pres):
        X = []
        # sp > 987.5, 987.5 >= sp > 975, 975 >= sp > 962.5, 962.5 > sp
        if type(lower_pres) is str:
            for i in range(len(upper_pres)):
                if sp[i] > upper_pres[i]:
                    x = sp[i] - upper_pres[i]
                else:
                    x = 0
                X.append(x)
        elif type(upper_pres) is str:
            for i in range(len(lower_pres)):
                if sp[i] > lower_pres[i]:
                    x = p[i] - lower_pres[i]
                else:
                    x = 0
                X.append(x)
        else:
            for i in range(len(lower_pres)):
                if sp[i] > lower_pres[i]:
                    x = lower_pres[i] - upper_pres[i]
                elif lower_pres[i] >= sp[i] and sp[i] > p[i]:
                    x1 = sp[i] - p[i]
                    x2 = p[i] - upper_pres[i]
                    x = x1 + x2
                elif p[i] >= sp[i] and sp[i] >= upper_pres[i]:
                    x = sp[i] - upper_pres[i]
                else:
                    x = 0
                X.append(x)
        return X

    def shape(self, array):
        array = np.array(array).reshape(253, 241)
        return array
    
    def calc1000hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=0,
            time=time,
            lower=None,
            upper=987.5
        )
        return W, QU, QV, DIV
    
    def calc975hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=1,
            time=time,
            lower=987.5,
            upper=962.5
        )
        return W, QU, QV, DIV

    def calc950hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=2,
            time=time,
            lower=962.5,
            upper=937.5
        )
        return W, QU, QV, DIV
    
    def calc925hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=3,
            time=time,
            lower=937.5,
            upper=912.5
        )
        return W, QU, QV, DIV
    
    def calc900hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=4,
            time=time,
            lower=912.5,
            upper=875
        )
        return W, QU, QV, DIV
    
    def calc850hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=5,
            time=time,
            lower=875,
            upper=825
        )
        return W, QU, QV, DIV
    
    def calc800hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=6,
            time=time,
            lower=825,
            upper=750
        )
        return W, QU, QV, DIV
    
    def calc700hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=7,
            time=time,
            lower=750,
            upper=650
        )
        return W, QU, QV, DIV
    
    def calc600hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=8,
            time=time,
            lower=650,
            upper=550
        )
        return W, QU, QV, DIV
    
    def calc500hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=9,
            time=time,
            lower=550,
            upper=450
        )
        return W, QU, QV, DIV
    
    def calc400hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=10,
            time=time,
            lower=450,
            upper=350
        )
        return W, QU, QV, DIV
    
    def calc300hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=11,
            time=time,
            lower=350,
            upper=275
        )
        return W, QU, QV, DIV
    
    def calc250hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=12,
            time=time,
            lower=275,
            upper=225
        )
        return W, QU, QV, DIV
    
    def calc200hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=13,
            time=time,
            lower=225,
            upper=175
        )
        return W, QU, QV, DIV
    
    def calc150hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=14,
            time=time,
            lower=175,
            upper=125
        )
        return W, QU, QV, DIV
    
    def calc100hPa(self, time):
        W, QU, QV, DIV = self.calcVars(
            i=15,
            time=time,
            lower=125,
            upper=None
        )
        return W, QU, QV, DIV