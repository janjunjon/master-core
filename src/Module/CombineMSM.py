import os
import numpy as np

from netCDF.NetCDF import NetCDF

class Combine:
    @classmethod
    def combineMSM(cls, path, var, varDim):
        varList = []
        for file in os.listdir(path):
            if file == '20200630.nc':
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:][:][:][:].tolist())
                for i in [5,6,7]:
                    varList.append(VAR[i, :, :, :])
            elif file == '20200731.nc':
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:][:][:][:].tolist())
                for i in [0,1,2,3,4]:
                    varList.append(VAR)
            else:
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:][:][:][:].tolist())
                varList.append(VAR)
        return varList