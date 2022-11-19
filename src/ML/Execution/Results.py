from Abstract.Abstract import Abstract
from Module.Figure import Figure
from ML.DR.PCA import *

class PCAResults(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def createComponentGraph(self):
        pca = PCALoad('PCA_Rain.sav')
        labels = ['rain_MSMs', 'psea', 'sp', 'u', 'v', 'temp', 'rh', 'ncld_upper', 'ncld_mid', 'ncld_low', 'ncld', 'dswrf', 'pwv', 'qu', 'qv', 'div', 'td', 'tl', 'lcl', 'ssi', 'ki']
        for i in range(len(labels)):
            Figure.createComponentBarGraph(
                path='{}/img/PCA/components/Rain/loading_Rain_{}.png'.format(self.root_path, i+1),
                labels=labels,
                array=pca.loading_[i],
                title='No.{} Rain'.format(i+1)
            )

    def createEVRGraph(self):
        pca = PCALoad('PCA_Rain.sav')
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
            path='{}/img/PCA/explained_variance_ratio/Rain.png'.format(self.root_path),
            labels=labels,
            array=cumulative_contribution_rate
        )