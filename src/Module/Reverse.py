import numpy as np

class Reverse:
    @classmethod
    def reverseLat(cls, array):
        # array[time][p][lat][lon]
        if isinstance(array, np.ndarray):
            ndim = array.ndim
            array = array.tolist()
        elif isinstance(array, list):
            array = np.array(array)
            ndim = array.ndim
            array = array.tolist()
        else:
            raise TypeError('type is not list.')
        if ndim == 4:
            for t in range(len(array)):
                for p in range(len(array[0])):
                    if t == 0 and p == 0: formar = array[t][p][0]
                    array[t][p].reverse()
            if formar != array[0][0][-1]:
                raise ValueError('converted value is invalid.')
        elif ndim == 3:
            for t in range(len(array)):
                if t == 0: formar = array[t][0]
                array[t].reverse()
            if formar != array[0][-1]:
                raise ValueError('converted value is invalid.')
        elif ndim == 2:
            formar = array[0]
            array.reverse()
            if formar != array[-1]:
                raise ValueError('converted value is invalid.')
        return array
