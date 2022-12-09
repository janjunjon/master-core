import os

from netCDF.v3.MLCorrectModel import *
from ML.DR.PCA import *

class PCA1(MLCorrectModel):
    """
    Variables: pattern1
    """
    def __init__(self) -> None:
        super().__init__()
        self.nc = NetCDF(self.fdrive_path + '/nc/combined/rains.nc')

        self.varnames = ['rain_MSMs', 'temp', 'u', 'v', 'sp']
        self.pca_save_path = '/home/jjthomson/master-core/var/PCA/v3/pattern1.sav'
        self.arr_save_path = '/home/jjthomson/fdrive/PCA/v3/pattern1'
        self.savePath = '/home/jjthomson/master-core/fdrive/nc/PCA/pattern1.nc'

    def pca(self):
        varnames = self.varnames
        self.setSpecificVars(varnames)
        self.shapeXForPCA(varnames)
        data = PrincipalComponentAnalysis.shapeData(
            rain_MSMs=self.rain_MSMs,
            temp=self.temp,
            u=self.u,
            v=self.v,
            sp=self.sp,
        )
        feature, pca, df = PrincipalComponentAnalysis.main(n_components=None, X=data)
        PrincipalComponentAnalysis.savePCA(pca, self.pca_save_path)
        # PrincipalComponentAnalysis.saveArray(feature, self.arr_save_path)
        self.createNC(feature.T)
    
    def createNC(self, score_):
        """
        pca.score_[8*253*241][number of variables]
        """
        for i, feature in enumerate(score_):
            score = np.reshape(feature, (248, 253, 241))
            locals()['component{}'.format(i+1)] =  score
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
        )

class PCA2(MLCorrectModel):
    """
    Variables: pattern2
    """
    def __init__(self) -> None:
        super().__init__()
        self.nc = NetCDF(self.fdrive_path + '/nc/combined/rains.nc')

        self.setVarnames = ['rain_MSMs', 'rh', 'ept']
        self.varnames = ['rain_MSMs', 'rh950hPa','rh700hPa', 'rh500hPa', 'ept950hPa', 'ept700hPa', 'ept500hPa']
        self.pca_save_path = '/home/jjthomson/master-core/var/PCA/v3/pattern2.sav'
        self.arr_save_path = '/home/jjthomson/fdrive/PCA/v3/pattern2'
        self.savePath = '/home/jjthomson/master-core/fdrive/nc/PCA/pattern2.nc'

    def pca(self):
        self.setSpecificVars(self.setVarnames)
        self.shapeXForPCA(self.varnames)
        data = PrincipalComponentAnalysis.shapeData(
            rain_MSMs=self.rain_MSMs,
            rh950hPa=self.rh950hPa,
            rh700hPa=self.rh700hPa,
            rh500hPa=self.rh500hPa,
            ept950hPa=self.ept950hPa,
            ept700hPa=self.ept700hPa,
            ept500hPa=self.ept500hPa
        )
        feature, pca, df = PrincipalComponentAnalysis.main(n_components=None, X=data)
        PrincipalComponentAnalysis.savePCA(pca, self.pca_save_path)
        # PrincipalComponentAnalysis.saveArray(feature, self.arr_save_path)
        self.createNC(feature.T)
    
    def createNC(self, score_):
        """
        pca.score_[8*253*241][number of variables]
        """
        for i, feature in enumerate(score_):
            score = np.reshape(feature, (248, 253, 241))
            locals()['component{}'.format(i+1)] =  score
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
        )

class PCA3(MLCorrectModel):
    """
    Variables: pattern3
    """
    def __init__(self) -> None:
        super().__init__()
        self.nc = NetCDF(self.fdrive_path + '/nc/combined/rains.nc')

        self.varnames = ['rain_MSMs', 'div', 'td', 'lcl', 'uvs', 'vvs']
        self.pca_save_path = '/home/jjthomson/master-core/var/PCA/v3/pattern3.sav'
        self.arr_save_path = '/home/jjthomson/fdrive/PCA/v3/pattern3'
        self.savePath = '/home/jjthomson/master-core/fdrive/nc/PCA/pattern3.nc'

    def pca(self):
        varnames = self.varnames
        self.setSpecificVars(varnames)
        self.shapeXForPCA(varnames)
        data = PrincipalComponentAnalysis.shapeData(
            rain_MSMs=self.rain_MSMs,
            div=self.div,
            td=self.td,
            lcl=self.lcl,
            uvs=self.uvs,
            vvs=self.vvs
        )
        feature, pca, df = PrincipalComponentAnalysis.main(n_components=None, X=data)
        PrincipalComponentAnalysis.savePCA(pca, self.pca_save_path)
        # PrincipalComponentAnalysis.saveArray(feature, self.arr_save_path)
        self.createNC(feature.T)
    
    def createNC(self, score_):
        """
        pca.score_[8*253*241][number of variables]
        """
        for i, feature in enumerate(score_):
            score = np.reshape(feature, (248, 253, 241))
            locals()['component{}'.format(i+1)] =  score
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
        )

class PCA4(MLCorrectModel):
    """
    Variables: pattern4
    """
    def __init__(self) -> None:
        super().__init__()
        self.nc = NetCDF(self.fdrive_path + '/nc/combined/rains.nc')

        
        self.setVarnames = ['rain_MSMs', 'ncld', 'pt', 'ssi', 'ki']
        self.varnames = ['rain_MSMs', 'ncld', 'pt950hPa', 'pt700hPa', 'pt500hPa', 'ssi', 'ki']
        self.pca_save_path = '/home/jjthomson/master-core/var/PCA/v3/pattern4.sav'
        self.arr_save_path = '/home/jjthomson/fdrive/PCA/v3/pattern4'
        self.savePath = '/home/jjthomson/master-core/fdrive/nc/PCA/pattern4.nc'

    def pca(self):
        self.setSpecificVars(self.setVarnames)
        self.shapeXForPCA(self.varnames)
        data = PrincipalComponentAnalysis.shapeData(
            rain_MSMs=self.rain_MSMs,
            ncld=self.ncld,
            pt950hPa=self.pt950hPa,
            pt700hPa=self.pt700hPa,
            pt500hPa=self.pt500hPa,
            ssi=self.ssi,
            ki=self.ki
        )
        feature, pca, df = PrincipalComponentAnalysis.main(n_components=None, X=data)
        PrincipalComponentAnalysis.savePCA(pca, self.pca_save_path)
        # PrincipalComponentAnalysis.saveArray(feature, self.arr_save_path)
        self.createNC(feature.T)
    
    def createNC(self, score_):
        """
        pca.score_[8*253*241][number of variables]
        """
        for i, feature in enumerate(score_):
            score = np.reshape(feature, (248, 253, 241))
            locals()['component{}'.format(i+1)] =  score
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
        )