import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA
import pickle

from Abstract.Abstract import Abstract
from ML.Other.Abstract import SKLearn

class PrincipalComponentAnalysis:
    @classmethod
    def main(cls, X, n_components: int = None):
        """
        transform(X): np.dot(X-X.mean(axis=0), PCA.components_)
        """
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
    def __init__(self, filedir, filename, indexes=True) -> None:
        """
        filename: *.sav
        """
        super().__init__()
        self.filedir = filedir
        self.filename = filename
        self.label = filename.split('.')[0]
        self.pca = pickle.load(open('{}/{}'.format(self.filedir, self.filename), 'rb'))
        self.feature = np.load(file='{}/{}.npy'.format(self.filedir, self.label))
        if indexes:
            self.indexes = np.load(file='{}/{}.npy'.format(self.filedir, '{}_indexes'.format(self.label)))

    @property
    def score_(self):
        """
        score_: 主成分得点
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.feature

    @property
    def loading_(self):
        """
        loading_: 主成分負荷量
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.components_

    @property
    def mean_(self):
        return self.pca.mean_

    @property
    def covariance_(self):
        return self.pca.get_covariance()

    @property
    def explained_variance_ratio_(self):
        """
        explained_variance_ratio_: 各主成分の寄与率
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.explained_variance_ratio_
    
    @property
    def cumulative_contribution_rate(self):
        explained_variance_ratio_ = self.getNormalArray(self.pca.explained_variance_ratio_)
        array = []
        cumulative_contribution_rate = 0
        for each_rate in explained_variance_ratio_:
            cumulative_contribution_rate += each_rate
            array.append(cumulative_contribution_rate)
        return array

    def print_cumulative_contribution_rate(self):
        cumulative_contribution_rates = self.cumulative_contribution_rate
        text = ''
        for i in range(len(cumulative_contribution_rates)):
            text += 'Until No.{}: {}\n'.format(i+1, cumulative_contribution_rates[i])
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

class PCALoad2(Abstract):
    def __init__(self, label, path) -> None:
        """
        filename: *.sav
        """
        super().__init__()
        self.label = label
        self.pca = SKLearn.loadModel(self, path)

    @property
    def score_(self):
        """
        score_: 主成分得点
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.feature

    @property
    def loading_(self):
        """
        loading_: 主成分負荷量
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.components_

    @property
    def mean_(self):
        return self.pca.mean_

    @property
    def covariance_(self):
        return self.pca.get_covariance()

    @property
    def explained_variance_ratio_(self):
        """
        explained_variance_ratio_: 各主成分の寄与率
        """
        np.set_printoptions(precision=5, suppress=True)
        return self.pca.explained_variance_ratio_

    @property
    def explained_variance_(self):
        """
        explained_variance_: 固有値
        """
        return self.pca.explained_variance_
    
    @property
    def cumulative_contribution_rate(self):
        explained_variance_ratio_ = self.getNormalArray(self.pca.explained_variance_ratio_)
        array = []
        cumulative_contribution_rate = 0
        for each_rate in explained_variance_ratio_:
            cumulative_contribution_rate += each_rate
            array.append(cumulative_contribution_rate)
        return array

    def print_cumulative_contribution_rate(self):
        cumulative_contribution_rates = self.cumulative_contribution_rate
        text = ''
        for i in range(len(cumulative_contribution_rates)):
            text += 'Until No.{}: {}\n'.format(i+1, cumulative_contribution_rates[i])
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