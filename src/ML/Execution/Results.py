from Abstract.Abstract import Abstract
from Module.Figure import Figure
from ML.DR.PCA import *

class PCAResults(Abstract):
    """
    create figures of PCA Results
    """
    def __init__(self, casename) -> None:
        super().__init__()
        self.casename = casename # example: HeavyRainCases
        self.pca = PCALoad('{}/var/PCA'.format(self.root_path), 'PCA_{}.sav'.format(self.casename))

    def createComponentGraph(self):
        pca = self.pca
        labels = ['rain_MSMs', 'psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf', 'pwv', 'qu', 'qv', 'div', 'td', 'tl', 'lcl', 'ssi', 'ki']
        for i in range(len(labels)):
            Figure.createComponentBarGraph(
                path='{}/img/PCA/components/{}/loading_{}_{}.png'.format(self.root_path, self.casename, self.casename, i+1),
                labels=labels,
                array=pca.loading_[i],
                title='No.{} {}'.format(i+1, self.casename)
            )

    def createEVRGraph(self):
        pca = self.pca
        if isinstance(pca.cumulative_contribution_rate, np.ndarray):
            cumulative_contribution_rate = pca.cumulative_contribution_rate.tolist()
        else:
            cumulative_contribution_rate = pca.cumulative_contribution_rate
        labels = []
        for i in range(len(pca.loading_)):
            label = 'Until No.{}'.format(i+1)
            labels.append(label)
        labels.reverse()
        cumulative_contribution_rate.reverse()
        cumulative_contribution_rate = np.array(cumulative_contribution_rate)
        cumulative_contribution_rate = cumulative_contribution_rate*100
        Figure.createEVRBarGraph(
            path='{}/img/PCA/explained_variance_ratio/{}.png'.format(self.root_path, self.casename),
            labels=labels,
            array=cumulative_contribution_rate
        )