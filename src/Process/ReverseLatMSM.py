from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF

class Execution:
    def __init__(self, ncDirPath, saveFilename) -> None:
        self.path = ncDirPath
        self.saveDir = '/home/jjthomson/fdrive/nc/reversed'
        self.saveFilename = saveFilename
        self.nc = NetCDF(self.path)
        self.lat = self.nc.variables['lat'][:].tolist()
        self.lat.reverse()
        self.lon = self.nc.variables['lon'][:].tolist()
        self.p = [
            1000.,  975.,  950.,  925.,  900.,  850.,  800.,  700.,  600.,  500.,  400.,  300.,  250.,  200.,  150.,  100.
        ]
        self.time = self.nc.variables['time'][:].tolist()
        
        self.varNcMSMs  = ['rain', 'psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf']
        self.varNcMSMp  = ['z', 'w', 'u', 'v', 'temp', 'rh']
        self.varNcDiv   = ['pwv', 'qu', 'qv', 'div']
        self.varNcAtmos = ['pt', 'ept', 'td', 'tl', 'lcl', 'ssi', 'ki']

    def createReversedMSMs(self):
        arr = []
        for var_name in self.varNcMSMs:
            locals()[var_name] = self.nc.variables[var_name][:].tolist()
            for var in locals()[var_name]:
                var.reverse()
            arr.append(locals()[var_name])
        CreateNetCDF.createNcFileMSMs(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            rainList=arr[0],
            pseaList=arr[1],
            spList=arr[2],
            uList=arr[3],
            vList=arr[4],
            tempList=arr[5],
            rhList=arr[6],
            ncld_upperList=arr[7],
            ncld_midList=arr[8],
            ncld_lowList=arr[9],
            ncldList=arr[10],
            dswrfList=arr[11]
        )

    def createReversedMSMp(self):
        arr = []
        for var_name in self.varNcMSMp:
            locals()[var_name] = self.nc.variables[var_name][:].tolist()
            for var_p in locals()[var_name]:
                for var_lat in var_p:
                    var_lat.reverse()
            arr.append(locals()[var_name])
        CreateNetCDF.createNcFileMSMp(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            zList=arr[0],
            wList=arr[1],
            uList=arr[2],
            vList=arr[3],
            tempList=arr[4],
            rhList=arr[5]
        )
    
    def createReversedDiv(self):
        arr = []
        for var_name in self.varNcDiv:
            locals()[var_name] = self.nc.variables[var_name][:].tolist()
            for var in locals()[var_name]:
                var.reverse()
            arr.append(locals()[var_name])
        CreateNetCDF.createNcFileDivergence(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            timeList=self.time,
            pwvList=arr[0],
            quList=arr[1],
            qvList=arr[2],
            divList=arr[3]
        )

    def createReversedAtmos(self):
        arr = []
        for var_name in self.varNcMSMp:
            locals()[var_name] = self.nc.variables[var_name][:].tolist()
            if var_name == 'pt' or var_name == 'ept':
                for var_p in locals()[var_name]:
                    for var_lat in var_p:
                        var_lat.reverse()
            else:
                for var in locals()[var_name]:
                    var.reverse()
            arr.append(locals()[var_name])
        CreateNetCDF.createNcFileAtmosIndexes(
            filename=self.saveFilename,
            path='{}/{}'.format(self.saveDir, self.saveFilename),
            lonList=self.lon,
            latList=self.lat,
            pList=self.p,
            timeList=self.time,
            ptList=arr[0],
            eptList=arr[1],
            tdList=arr[2],
            tlList=arr[3],
            lclList=arr[4],
            ssiList=arr[5],
            kiList=arr[6]
        )