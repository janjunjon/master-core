import os

from Abstract.Abstract import Abstract
from netCDF.NetCDF import NetCDF
from Module.CreateNetCDF import CreateNetCDF
from ML.DR.PCA import *

class Execution(Abstract):
    def __init__(self) -> None:
        super().__init__()
        self.filedir = self.fdrive_path + '/PCA/202007'
        self.savePath = self.fdrive_path + '/nc/PCA/pca.nc'
        self.nc = NetCDF(self.fdrive_path + '/nc/reversed/rains.nc')

    def main(self):
        """
        pca.score_[8*253*241][number of variables]
        """
        files = os.listdir(self.filedir)
        j = 0
        for file in files:
            if file.split('.')[-1] == 'npy':
                continue
            pca = PCALoad(filedir=self.filedir, filename=file, indexes=False)
            score_ = pca.score_.T
            if j == 0:
                time = 3
            elif j == 31:
                time = 5
            else:
                time = 8
            for i, feature in enumerate(score_):
                score = np.reshape(feature, (time, 253, 241))
                if j == 0:
                    locals()['component{}'.format(i+1)] =  score
                else:
                    locals()['component{}'.format(i+1)] = np.append(locals()['component{}'.format(i+1)], score, axis=0)
            j += 1
        print('ndim', locals()['component1'].ndim, len(locals()['component1']), len(locals()['component1'][0]), len(locals()['component1'][0][0]))
        CreateNetCDF.createNcFilePCAv2(
            path=self.savePath,
            lonList=self.nc.lon,
            latList=self.nc.lat,
            timeList=self.nc.time,
            component1=locals()['component1'],
            component2=locals()['component2'],
            component3=locals()['component3'],
            component4=locals()['component4'],
            component5=locals()['component5'],
            component6=locals()['component6'],
            component7=locals()['component7'],
            component8=locals()['component8'],
            component9=locals()['component9'],
            component10=locals()['component10'],
            component11=locals()['component11'],
            component12=locals()['component12'],
            component13=locals()['component13'],
            component14=locals()['component14'],
            component15=locals()['component15'],
            component16=locals()['component16'],
            component17=locals()['component17'],
            component18=locals()['component18'],
            component19=locals()['component19'],
            component20=locals()['component20'],
            component21=locals()['component21'],
        )