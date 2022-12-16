import numpy as np

class Array:
    @classmethod
    def reshape(cls, array) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        if array.ndim == 1 and len(array) == 253*241:
            array = np.reshape(array, (253, 241))
        elif array.ndim == 1 and len(array) == 253*241*16:
            array = np.reshape(array, (16, 253, 241))
        return array

    @classmethod
    def convert(cls, array) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        if array.ndim > 1:
            array = np.ravel(array)
        return array

    @classmethod
    def listToNdArray(cls, array) -> np.ndarray:
        if isinstance(array, list):
            array = np.array(array)
        elif isinstance(array, np.ndarray):
            pass
        else:
            raise TypeError('array is not list.')
        return array

    @classmethod
    def ndarrayToList(cls, array) -> list:
        if isinstance(array, list):
            pass
        elif isinstance(array, np.ndarray):
            array = array.tolist()
        else:
            raise TypeError('array is not list.')
        return array

    @classmethod
    def getTransposedMatrix(cls, array):
        transposedMatrix = []
        for i in range(len(array[0])):
            X = []
            for j in range(len(array)):
                X.append(array[j][i])
            transposedMatrix.append(X)
        return transposedMatrix