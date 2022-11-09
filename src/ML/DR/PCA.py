import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn import preprocessing
from sklearn.decomposition import PCA

class PrincipalComponentAnalysis:
    @classmethod
    def main(cls, n_components, *args):
        pca = PCA(n_components=n_components)
        X = cls.shapeData(args)
        pca.fit(X)

    @classmethod
    def shapeData(cls, *args, **kwargs):
        # dataArray = [[var1], [var2], ...]
        dataArray = []
        for data in args:
            dataArray.append(data)
        for value in kwargs.values():
            dataArray.append(value)
        X = np.array(dataArray).T
        np.random.shuffle(X)
        sc = preprocessing.StandardScaler()
        sc.fit(X)
        X = sc.transform(X)
        return X