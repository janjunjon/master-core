from netCDF.NetCDF import NetCDF

class RadarAmedas(NetCDF):
    def __init__(self, path) -> None:
        super().__init__(path)