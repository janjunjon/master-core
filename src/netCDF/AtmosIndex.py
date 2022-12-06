import numpy as np

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF
from Module.CalcAtmosIndex import Calculation as AtmosCalculation
from Module.CreateNetCDF import CreateNetCDF
from Module.Reverse import Reverse

class NetCDFAtmosIndex(Abstract):
    def __init__(self, path_MSMp, savePath, filename) -> None:
        super().__init__()
        self.MSMp = NetCDF(path=path_MSMp)
        self.savePath = savePath
        self.filename = filename

        lat = self.MSMp.variables['lat'][:].tolist()
        lat.reverse()
        self.lat = np.array(lat)
        self.lon = np.array(self.MSMp.variables['lon'][:].tolist())
        self.time = np.array(self.MSMp.variables['time'][:].tolist())
        # [1000.,  975.,  950.,  925.,  900.,  850.,  800.,  700.,  600.,  500.,  400.,  300.,  250.,  200.,  150.,  100.]
        self.p = np.array(self.MSMp.variables['p'][:].tolist())
        self.temp = np.array(self.MSMp.variables['temp'][:][:][:][:].tolist())
        self.temp1000hPa = self.temp[:, 0, :, :]
        self.temp850hPa = self.temp[:, 5, :, :]
        self.temp700hPa = self.temp[:, 7, :, :]
        self.temp500hPa = self.temp[:, 9, :, :]
        self.rh = np.array(self.MSMp.variables['rh'][:][:][:][:].tolist())
        self.rh1000hPa = self.rh[:, 0, :, :]
        self.rh850hPa = self.rh[:, 5, :, :]
        self.rh700hPa = self.rh[:, 7, :, :]
        self.rh500hPa = self.rh[:, 9, :, :]
        self.u = np.array(self.MSMp.variables['u'][:][:][:][:].tolist())
        self.u900hPa = self.u[:, 4, :, :]
        self.u700hPa = self.u[:, 7, :, :]
        self.v = np.array(self.MSMp.variables['v'][:][:][:][:].tolist())
        self.v900hPa = self.v[:, 4, :, :]
        self.v700hPa = self.v[:, 7, :, :]

        self.varNcAtmos = ['pt', 'ept', 'td', 'tl', 'lcl', 'ssi', 'ki', 'uvs', 'vvs']

    def main(self):
        self.pt, self.ept = self.calcFourDimensionalVars()
        self.td, self.tl, self.lcl, self.ssi, self.ki, self.uvs, self.vvs = self.calcThreeDimensionalVars()
        for var_name in self.varNcAtmos:
            setattr(self, var_name, Reverse.reverseLat(getattr(self, var_name)))
        CreateNetCDF.createNcFileAtmosIndexes(
            filename=self.filename,
            path=self.savePath,
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            ptList=self.pt,
            eptList=self.ept,
            tdList=self.td,
            tlList=self.tl,
            lclList=self.lcl,
            ssiList=self.ssi,
            kiList=self.ki,
            uvsList=self.uvs,
            vvsList=self.vvs
        )

    def calcFourDimensionalVars(self):
        PTList = []
        EPTList = []
        for t in range(8):
            for p in range(16):
                for y in range(253):
                    for x in range(241):
                        PT = AtmosCalculation.getPotentialTemperature(
                            temp=self.temp[t, p, y, x],
                            P=self.p[p]
                        )
                        EPT = AtmosCalculation.getEquivalentPotentialTemperature(
                            temp=self.temp[t, p, y, x],
                            rh=self.rh[t, p, y, x],
                            P=self.p[p]
                        )
                        PTList.append(PT)
                        EPTList.append(EPT)
        PTList = self.restoreMultidimensionalArray(np.array(PTList), 4)
        EPTList = self.restoreMultidimensionalArray(np.array(EPTList), 4)
        return PTList, EPTList

    def calcThreeDimensionalVars(self):
        TdList = []
        TlList = []
        LCLList = []
        SSIList = []
        KIList = []
        UVSList = []
        VVSList = []
        for t in range(8):
            for y in range(253):
                for x in range(241):
                    Td = AtmosCalculation.getDewPointTemperature(
                        temp=self.temp1000hPa[t, y, x],
                        rh=self.temp1000hPa[t, y, x]
                    )
                    Tl = AtmosCalculation.getCondensationTemperature(
                        temp=self.temp1000hPa[t, y, x],
                        rh=self.temp1000hPa[t, y, x]
                    )
                    LCL = AtmosCalculation.getLCL(
                        temp=self.temp1000hPa[t, y, x],
                        rh=self.rh1000hPa[t, y, x]
                    )
                    SSI = AtmosCalculation.getSSI(
                        temp500hPa=self.temp500hPa[t, y, x],
                        temp850hPa=self.temp850hPa[t, y, x],
                        rh850hPa=self.rh850hPa[t, y, x]
                    )
                    KI = AtmosCalculation.getKI(
                        temp850hPa=self.temp850hPa[t, y, x],
                        temp700hPa=self.temp700hPa[t, y, x],
                        temp500hPa=self.temp500hPa[t, y, x],
                        rh850hPa=self.rh850hPa[t, y, x],
                        rh700hPa=self.rh700hPa[t, y, x]
                    )
                    UVS, VVS = AtmosCalculation.getVerticalSheer(
                        upperU=self.u700hPa[t, y, x],
                        upperV=self.v700hPa[t, y, x],
                        lowerU=self.u900hPa[t, y, x],
                        lowerV=self.v900hPa[t, y, x],
                    )
                    TdList.append(Td)
                    TlList.append(Tl)
                    LCLList.append(LCL)
                    SSIList.append(SSI)
                    KIList.append(KI)
                    UVSList.append(UVS)
                    VVSList.append(VVS)
        TdList = self.restoreMultidimensionalArray(np.array(TdList), 3)
        TlList = self.restoreMultidimensionalArray(np.array(TlList), 3)
        LCLList = self.restoreMultidimensionalArray(np.array(LCLList), 3)
        SSIList = self.restoreMultidimensionalArray(np.array(SSIList), 3)
        KIList = self.restoreMultidimensionalArray(np.array(KIList), 3)
        UVSList = self.restoreMultidimensionalArray(np.array(UVSList), 3)
        VVSList = self.restoreMultidimensionalArray(np.array(VVSList), 3)
        return TdList, TlList, LCLList, SSIList, KIList, UVSList, VVSList

    def convertOneDimArray(self, array):
        if not isinstance(array, np.ndarray):
            raise TypeError('It is not an instance of numpy.ndarray')
        array = np.ravel(array)
        return array
    
    def restoreMultidimensionalArray(self, array, ndim):
        if not isinstance(array, np.ndarray):
            raise TypeError('It is not an instance of numpy.ndarray')
        if ndim == 4:
            array = np.reshape(array, (8, 16, 253, 241))
        elif ndim == 3:
            array = np.reshape(array, (8, 253, 241))
        elif ndim == 2:
            array = np.array(array).reshape(253, 241)
        return array