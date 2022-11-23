import numpy as np
import matplotlib.pyplot as plt

class Figure:
    @classmethod
    def createComponentBarGraph(cls, path: str, labels: list, array: list, title: str = None):
        """
        array: 1 dimensional array
        """
        fig, ax = plt.subplots()
        color = [('b' if i > 0 else 'r') for i in array]
        ax.set_xlim(-1, 1)
        ax.set_xlabel("PCA loading (-1 to 1)")
        ax.barh(labels, array, color=color)
        ax.set_title("PCA loading {}".format(title))
        fig.subplots_adjust(left=0.2)
        fig.show()
        fig.savefig(path)
        
    @classmethod
    def createEVRBarGraph(cls, path: str, labels: list, array: list):
        """
        array: 1 dimensional array
        """
        fig, ax = plt.subplots()
        color = [('b' if i > 0 else 'r') for i in array]
        ax.barh(labels, array, color=color)
        ax.set_xlabel("explained variance ratio (%)")
        ax.set_title("explained_variance_ratio_")
        fig.subplots_adjust(left=0.2)
        fig.show()
        fig.savefig(path)
        
    @classmethod
    def createMultiBarGraph(cls, path: str, labels: list, array: list):
        """
        array: 2 dimensional array
        """
        ncols = 3
        nrows = 7
        fig, axes = plt.subplots(
            ncols=ncols,
            nrows=nrows,
            squeeze=False,
            tight_layout=True
        )
        color = [('b' if i > 0 else 'r') for i in array[0]]
        axes[0,0].barh(labels, array[0], color=color)
        # k = 0
        # for i in range(ncols):
        #     for j in range(nrows):
        #         print(array[k])
        #         color = [('b' if i > 0 else 'r') for i in array[k]]
        #         print(i, j, k)
        #         axes[i,j].barh(labels, array[k], color=color)
        #         k += 1
        fig.show()
        fig.savefig(path)