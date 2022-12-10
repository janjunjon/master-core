import numpy as np
from sklearn.metrics import mean_squared_error

class Calculation:
    @classmethod
    def corrcoef_(cls, array1, array2):
        if not isinstance(array1, np.ndarray):
            array1 = np.array(array1)
        if not isinstance(array2, np.ndarray):
            array2 = np.array(array2)
        corrcoef_ = np.corrcoef(array1, array2)
        return corrcoef_

    @classmethod
    def FSS_(cls, indexes, threshold, arr_real, arr_pred):
        print(np.sum(arr_real))
        print(np.sum(arr_pred))
        arr_Io = []
        arr_If = []
        for i in indexes:
            real = arr_real[i]
            pred = arr_pred[i]
            Io = 1 if real >= threshold else 0
            If = 1 if pred >= threshold else 0
            arr_Io.append(Io)
            arr_If.append(If)
        print(np.sum(arr_Io))
        print(np.sum(arr_If))
        ave_Io = []
        for j in range(len(arr_Io)):
            if j >= len(arr_Io) - 3:
                ave_Io.append(np.mean([arr_Io[j], arr_Io[j-1], arr_Io[j-2]]))
            else:
                ave_Io.append(np.mean([arr_Io[j], arr_Io[j+1], arr_Io[j+2]]))
        ave_If = []
        for j in range(len(arr_If)):
            if j >= len(arr_If) - 3:
                ave_If.append(np.mean([arr_If[j], arr_If[j-1], arr_If[j-2]]))
            else:
                ave_If.append(np.mean([arr_If[j], arr_If[j+1], arr_If[j+2]]))
        print(np.sum(ave_Io))
        print(np.sum(ave_If))
        MSE = np.mean([(ave_If[j] - ave_Io[j])**2 for j in range(len(ave_Io))])
        MSEref = np.mean([(ave_If[j]**2 + ave_Io[j]**2) for j in range(len(ave_Io))])
        a = np.array([(ave_If[j] - ave_Io[j])**2 for j in range(len(ave_Io))])
        b = np.array([(ave_If[j]**2 + ave_Io[j]**2) for j in range(len(ave_Io))])
        # print([b for b in a if b != 0])
        print('MSE: {:.4f}'.format(MSE))
        print('MSEref: {:.4f}'.format(MSEref))
        print('MSE / MSEref: {:.4f}'.format(MSE / MSEref))
        FSS = 1 - (MSE / MSEref)
        return FSS
