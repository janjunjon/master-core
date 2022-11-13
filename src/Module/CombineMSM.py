import os
import numpy as np

from netCDF.NetCDF import NetCDF

class Combine:
    @classmethod
    def combineMSM(cls, path, var, varDim=3):
        varList = []
        for file in os.listdir(path):
            if file == '20200630.nc':
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:].tolist())
                for t in [5,6,7]:
                    varList.append(VAR[t, :, :]) if varDim == 3 else varList.append(VAR[t, :, :, :])
            elif file == '20200731.nc':
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:].tolist())
                for t in [0,1,2,3,4]:
                    varList.append(VAR[t, :, :]) if varDim == 3 else varList.append(VAR[t, :, :, :])
            else:
                nc = NetCDF('{}/{}'.format(path, file))
                VAR = np.array(nc.variables[var][:].tolist())
                for t in range(8):
                    varList.append(VAR[t, :, :]) if varDim == 3 else varList.append(VAR[t, :, :, :])
        return varList