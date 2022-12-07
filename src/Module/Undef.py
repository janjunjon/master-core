import numpy as np

from Exception.Exception import *
from Module.Array import Array

class Undef:
    @classmethod
    def setUndefRadarAmedas(cls, array):
        undef = np.load(file='/home/jjthomson/master-core/var/Data/undef.npy')
        if isinstance(array, np.ndarray):
            ndim = array.ndim
            array = array.tolist()
        elif isinstance(array, list):
            array = np.array(array)
            ndim = array.ndim
            array = array.tolist()
        else:
            raise TypeError('type is not list.')
        if ndim == 2:
            array = Array.convert(array)
            for i, each in enumerate(array):
                if i in undef:
                    array[i] = -999.0
                else:
                    continue
            array = Array.reshape(array)
            return array
        else:
            raise DimensionalError('dimension of array should be 2.')