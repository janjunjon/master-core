import netCDF4
from numpy import ma
from netCDF.NetCDF import NetCDF

class ConvertedRa(NetCDF):
    def __init__(self, file) -> None:
        super().__init__(file)
        self.nc = netCDF4.Dataset(file)
        # 0,3,6,9,12,15,18,21時は欠損
        # self.time = [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]
        self.filename = file.split('/')[-1].split('.')[0]

    @property
    def rain(self):
        r1h = self._convertRaRain()
        return r1h

    @property
    def lat(self):
        lat = self.nc.variables['lat'][:].tolist()
        convertedLat = []
        for i in range(287, 3312, 12):
            convertedLat.append(lat[i])
        return convertedLat
    
    @property
    def lon(self):
        lon = self.nc.variables['lon'][:].tolist()
        convertedLon = []
        for j in range(159, 2560, 10):
            convertedLon.append(lon[j])
        return convertedLon

    @property
    def time(self):
        return [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0, 22.0]

    def _returnConvertedLatLon(self):
        lat = self.nc.variables['lat'][:].tolist()
        lon = self.nc.variables['lon'][:].tolist()
        convertedLat = []
        convertedLon = []
        for i in range(287, 3312, 12):
            convertedLat.append(lat[i])
        for j in range(159, 2560, 10):
            convertedLon.append(lon[j])
        return [convertedLat, convertedLon]

    def _convertResolution(self, v_array):
        normal_array_with_time = []
        for time_a in v_array:
            lat_a = []
            for i in range(287, 3312, 12):
                lon_a = []
                for j in range(159, 2560, 10):
                    lon_a.append(time_a[i][j])
                lat_a.append(lon_a)
            normal_array_with_time.append(lat_a)
        return normal_array_with_time

    def _convertRaRain(self):
        rain = ma.masked_values(self.nc.variables['rain'], value=-999)
        rain.mask = ma.nomask
        if rain.ndim == 3:
            convertedRain = []
            for i in range(0, 8):
                lat_a = []
                for j in range(287, 3312, 12):
                    lon_a = []
                    for k in range(159, 2560, 10):
                        lon_a.append(
                            rain[i][j][k]
                        )
                    lat_a.append(lon_a)
                convertedRain.append(lat_a)
        elif rain.ndim == 2:
            convertedRain = []
            for j in range(287, 3312, 12):
                lon_a = []
                for k in range(159, 2560, 10):
                    lon_a.append(
                        rain[j][k]
                    )
                convertedRain.append(lon_a)
        return convertedRain