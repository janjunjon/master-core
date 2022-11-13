import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA
import pickle

from Abstract.Abstract import Abstract

class PrincipalComponentAnalysis:
    @classmethod
    def main(cls, n_components, X):
        pca = PCA(n_components=n_components)
        pca.fit(X)
        feature = pca.transform(X)
        df = pd.DataFrame(feature)
        return feature, pca, df

    @classmethod
    def shapeData(cls, *args, **kwargs):
        # dataArray = [[var1], [var2], ...]
        dataArray = []
        if args != None:
            for data in args:
                dataArray.append(data)
        if kwargs != None:
            for value in kwargs.values():
                dataArray.append(value)
        X = cls.getTransposedMatrix(dataArray)
        print(type(dataArray), len(dataArray), len(dataArray[0]))
        np.random.shuffle(X)
        sc = preprocessing.StandardScaler()
        sc.fit(X)
        X = sc.transform(X)
        return X
    
    @classmethod
    def getPrincipalComponentLoading(self, feature):
        df = pd.DataFrame(feature)
        return df
    
    @classmethod
    def getTransposedMatrix(cls, array):
        transposedMatrix = []
        for i in range(len(array[0])):
            X = []
            for j in range(len(array)):
                X.append(array[j][i])
            transposedMatrix.append(X)
        return transposedMatrix

    @classmethod
    def savePCA(cls, pca, path):
        pickle.dump(pca, open(path, 'wb'))
        print('save is completed.')

    @classmethod
    def saveArray(cls, array, path) -> None:
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        np.save(path, array)

class PCALoad(Abstract):
    def __init__(self, filename) -> None:
        super().__init__()
        self.label = filename.split('.')[0]
        self.path = '{}/var/PCA/{}'.format(self.root_path, filename)
        self.pca = pickle.load(open(self.path, 'rb'))
        self.feature = np.load(file='{}/var/PCA/{}.npy'.format(self.root_path, self.label))

    @property
    def components(self):
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.components_

    @property
    def mean(self):
        return self.pca.mean_

    @property
    def covariance(self):
        return self.pca.get_covariance()

    @property
    def explained_variance_ratio_(self):
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.explained_variance_ratio_
    
    def print_cumulative_contribution_rate(self):
        explained_variance_ratio_ = self.getNormalArray(self.pca.explained_variance_ratio_)
        cumulative_contribution_rate = 0
        text = ''
        for each_rate in explained_variance_ratio_:
            cumulative_contribution_rate += each_rate
            text += 'Until No.{}: {}\n'.format(explained_variance_ratio_.index(each_rate)+1, cumulative_contribution_rate)
        with open('{}/var/PCA/{}.txt'.format(self.root_path, self.label), 'w') as f:
            f.write(text)

    def getNdArray(self, array):
        if isinstance(array, np.ndarray):
            return array
        else:
            array = np.array(array)
            return array
    
    def getNormalArray(self, array):
        if isinstance(array, np.ndarray):
            array = array.tolist()
            return array
        else:
            return array