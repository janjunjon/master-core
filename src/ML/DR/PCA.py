import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.decomposition import PCA

class PrincipalComponentAnalysis:
    @classmethod
    def main(cls, n_components, *args):
        pca = PCA(n_components=n_components)
        X = cls.shapeData(args)
        pca.fit(X)

    @classmethod
    def shapeData(cls, *args):
        # dataArray = [[var1], [var2], ...]
        dataArray = []
        for data in args:
            dataArray.append(data)
        X = np.array(dataArray).T
        np.random.shuffle(X)
        return X