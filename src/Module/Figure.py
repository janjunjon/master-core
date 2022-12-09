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

    @classmethod
    def createModelResult(cls, model, X_train, X_test, Y_train, Y_test, path):
        # 予測値の計算
        score = model.score(X_test, Y_test)

        # グラフ化
        # plt.scatter(X_test, Y_test,label="test data")

        plt.clf()
        print(f'X_train: {len(X_train)}, X_test: {len(X_test)}, Y_train: {len(Y_train)}, Y_test: {len(Y_test)}')
        plt.scatter(X_test, Y_test, label="test data", edgecolor='k',facecolor='w')
        plt.scatter(X_train, Y_train, label="training data", facecolor="r", marker='x')
        plt.scatter(X_train[model.support_], Y_train[model.support_], label="Support vectors", color='c')

        plt.title("predicted results")
        plt.xlabel("$x$")
        plt.ylabel("$y$")

        x = np.reshape(np.arange(-3,3,0.01), (-1, 1))
        plt.plot(x, model.predict(x), label="model ($R^2=%1.3f$)" % (score), color='b')

        plt.legend()
        
        plt.savefig(path)
        plt.close()