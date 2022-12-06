import netCDF4

from netCDF.NetCDF import NetCDF
from Module.CombineMSM import Combine
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self, ncDirPath, saveFilename) -> None:
        self.path = ncDirPath
        self.saveDir = '/home/jjthomson/fdrive/nc/combined'
        self.saveFilename = saveFilename
        self.nc = netCDF4.Dataset('/home/jjthomson/fdrive/nc/recreated/rains.nc')
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.p = [
            1000.,  975.,  950.,  925.,  900.,  850.,  800.,  700.,  600.,  500.,  400.,  300.,  250.,  200.,  150.,  100.
        ]
        self.time = range(0, 248)

    def combineAllMSMs(self):
        RAIN = Combine.combineMSM(self.path, 'rain')
        PSEA = Combine.combineMSM(self.path, 'psea')
        SP = Combine.combineMSM(self.path, 'sp')
        U = Combine.combineMSM(self.path, 'u')
        V = Combine.combineMSM(self.path, 'v')
        TEMP = Combine.combineMSM(self.path, 'temp')
        RH = Combine.combineMSM(self.path, 'rh')
        NCLD_UPPER = Combine.combineMSM(self.path, 'ncld_upper')
        NCLD_MID = Combine.combineMSM(self.path, 'ncld_mid')
        NCLD_LOW = Combine.combineMSM(self.path, 'ncld_low')
        NCLD = Combine.combineMSM(self.path, 'ncld')
        DSWRF = Combine.combineMSM(self.path, 'dswrf')
        CreateNetCDF.createNcFileMSMs(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList=RAIN,
            pseaList=PSEA,
            spList=SP,
            uList=U,
            vList=V,
            tempList=TEMP,
            rhList=RH,
            ncld_upperList=NCLD_UPPER,
            ncld_midList=NCLD_MID,
            ncld_lowList=NCLD_LOW,
            ncldList=NCLD,
            dswrfList=DSWRF
        )

    def combineAllMSMp(self):
        Z = Combine.combineMSM(self.path, 'z', 4)
        W = Combine.combineMSM(self.path, 'w', 4)
        U = Combine.combineMSM(self.path, 'u', 4)
        V = Combine.combineMSM(self.path, 'v', 4)
        TEMP = Combine.combineMSM(self.path, 'temp', 4)
        RH = Combine.combineMSM(self.path, 'rh', 4)
        CreateNetCDF.createNcFileMSMp(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            zList=Z,
            wList=W,
            uList=U,
            vList=V,
            tempList=TEMP,
            rhList=RH
        )

    def combineAllDiv(self):
        PWV = Combine.combineMSM(self.path, 'pwv')
        QU = Combine.combineMSM(self.path, 'qu')
        QV = Combine.combineMSM(self.path, 'qv')
        DIV = Combine.combineMSM(self.path, 'div')
        CreateNetCDF.createNcFileDivergence(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            pwvList=PWV,
            quList=QU,
            qvList=QV,
            divList=DIV
        )

    def combineAllAtmos(self):
        PT = Combine.combineMSM(self.path, 'pt', 4)
        EPT = Combine.combineMSM(self.path, 'ept', 4)
        TD = Combine.combineMSM(self.path, 'td')
        TL = Combine.combineMSM(self.path, 'tl')
        LCL = Combine.combineMSM(self.path, 'lcl')
        SSI = Combine.combineMSM(self.path, 'ssi')
        KI = Combine.combineMSM(self.path, 'ki')
        UVS = Combine.combineMSM(self.path, 'uvs')
        VVS = Combine.combineMSM(self.path, 'vvs')
        CreateNetCDF.createNcFileAtmosIndexes(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            ptList=PT,
            eptList=EPT,
            tdList=TD,
            tlList=TL,
            lclList=LCL,
            ssiList=SSI,
            kiList=KI,
            uvsList=UVS,
            vvsList=VVS
        )