import netCDF4
import numpy as np
from numpy import dtype

class CreateNetCDF:
    @classmethod
    def createNcFileMSMs(
        cls, filename, path, lonList, latList, timeList, rainList, pseaList, spList, uList, vList, tempList, rhList, ncld_upperList, ncld_midList, ncld_lowList, ncldList, dswrfList
    ):
        nc = netCDF4.Dataset(path, "w", format="NETCDF4")
        nc.createDimension("lon", len(lonList))
        nc.createDimension("lat", len(latList))
        nc.createDimension("time", len(timeList))

        lon = nc.createVariable("lon", dtype('float32'), "lon")
        lon.long_name = 'longitude'
        lon.units = 'degrees_east'
        lon.standard_name = 'longitude'

        lat = nc.createVariable("lat", dtype('float32'), "lat")
        lat.long_name = 'latitude'
        lat.units = 'degrees_north'
        lat.standard_name = 'latitude'

        time = nc.createVariable("time", dtype('int16'), "time")
        time.long_name = 'time'
        time.unit = 'hours since {}'.format(filename)
        time.standard_name = 'time'

        rain = nc.createVariable("rain", dtype('int16'), ("time", "lat", "lon"))
        rain.scale_factor = 0.006116208155
        rain.add_offset = 200.0
        rain.long_name = 'rainfall in 1 hour'
        rain.units = 'mm/h'
        rain.standard_name = 'rainfall_rate'

        psea = nc.createVariable("psea", dtype('int16'), ("time", "lat", "lon"))
        psea.scale_factor = 0.4587155879
        psea.add_offset = 95000.0
        psea.long_name = 'sea level pressure'
        psea.units = 'Pa'
        psea.standard_name = 'sea_level_pressure'

        sp = nc.createVariable("sp", dtype('int16'), ("time", "lat", "lon"))
        sp.scale_factor = 0.9174311758
        sp.add_offset = 80000.0
        sp.long_name = 'surface level pressure'
        sp.units = 'Pa'
        sp.standard_name = 'surface_level_pressure'

        u = nc.createVariable("u", dtype('int16'), ("time", "lat", "lon"))
        u.scale_factor = 0.006116208155
        u.add_offset = 0.0
        u.long_name = 'eastward component of wind'
        u.units = 'm/s'
        u.standard_name = 'eastward_wind'

        v = nc.createVariable("v", dtype('int16'), ("time", "lat", "lon"))
        v.scale_factor = 0.006116208155
        v.add_offset = 0.0
        v.long_name = 'northward component of wind'
        v.units = 'm/s'
        v.standard_name = 'northward_wind'

        temp = nc.createVariable("temp", dtype('int16'), ("time", "lat", "lon"))
        temp.scale_factor = 0.002613491379
        temp.add_offset = 255.4004974
        temp.long_name = 'temperature'
        temp.units = 'K'
        temp.standard_name = 'air_temperature'

        rh = nc.createVariable("rh", dtype('int16'), ("time", "lat", "lon"))
        rh.scale_factor = 0.002293577883
        rh.add_offset = 75.0
        rh.long_name = 'relative humidity'
        rh.units = '%'
        rh.standard_name = 'relative_humidity'

        ncld_upper = nc.createVariable("ncld_upper", dtype('int16'), ("time", "lat", "lon"))
        ncld_upper.scale_factor =0.001666666591
        ncld_upper.add_offset = 50.0
        ncld_upper.long_name = 'upper-level cloudiness'
        ncld_upper.units = '%'

        ncld_mid = nc.createVariable("ncld_mid", dtype('int16'), ("time", "lat", "lon"))
        ncld_mid.scale_factor = 0.001666666591
        ncld_mid.add_offset = 50.0
        ncld_mid.long_name = 'mid-level cloudiness'
        ncld_mid.units = '%'

        ncld_low = nc.createVariable("ncld_low", dtype('int16'), ("time", "lat", "lon"))
        ncld_low.scale_factor = 0.001666666591
        ncld_low.add_offset = 50.0
        ncld_low.long_name = 'low-level cloudiness'
        ncld_low.units = '%'

        ncld = nc.createVariable("ncld", dtype('int16'), ("time", "lat", "lon"))
        ncld.scale_factor = 0.001666666591
        ncld.add_offset = 50.0
        ncld.long_name = 'cloud amount'
        ncld.units = '%'
        ncld.standard_name = 'cloud_area_fraction'

        dswrf = nc.createVariable("dswrf", dtype('int16'), ("time", "lat", "lon"))
        dswrf.scale_factor = 0.0205
        dswrf.add_offset = 665.0
        dswrf.long_name = 'Downward Short-Wave Radiation Flux'
        dswrf.units = 'W/m^2'
        dswrf.standard_name = 'surface_net_downward_shortwave_flux'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        rain[:, :, :] = np.array(rainList)
        psea[:, :, :] = np.array(pseaList)
        sp[:, :, :] = np.array(spList)
        u[:, :, :] = np.array(uList)
        v[:, :, :] = np.array(vList)
        temp[:, :, :] = np.array(tempList)
        rh[:, :, :] = np.array(rhList)
        ncld_upper[:, :, :] = np.array(ncld_upperList)
        ncld_mid[:, :, :] = np.array(ncld_midList)
        ncld_low[:, :, :] = np.array(ncld_lowList)
        ncld[:, :, :] = np.array(ncldList)
        dswrf[:, :, :] = np.array(dswrfList)
        nc.close()

    @classmethod
    def createNcFileDivergence(cls, filename, path, lonList, latList, timeList, wList, quList, qvList, divList):
        nc = netCDF4.Dataset(path, "w", format="NETCDF4")
        nc.createDimension("lon", len(lonList))
        nc.createDimension("lat", len(latList))
        nc.createDimension("time", len(timeList))

        lon = nc.createVariable("lon", dtype('float32'), "lon")
        lon.long_name = 'longitude'
        lon.units = 'degrees_east'
        lon.standard_name = 'longitude'

        lat = nc.createVariable("lat", dtype('float32'), "lat")
        lat.long_name = 'latitude'
        lat.units = 'degrees_north'
        lat.standard_name = 'latitude'

        time = nc.createVariable("time", dtype('int16'), "time")
        time.long_name = 'time'
        time.unit = 'hours since {}'.format(filename)
        time.standard_name = 'time'

        w = nc.createVariable("w", dtype('int16'), ("time", "lat", "lon"))
        w.long_name = 'precipitable water vaper'
        w.units = 'mm/h'
        w.standard_name = 'precipitable_water_vaper'

        qu = nc.createVariable("qu", dtype('int16'), ("time", "lat", "lon"))
        qu.long_name = 'specific humidity on u wind'
        qu.units = 'm/s/g'
        qu.standard_name = 'specific_humidity_u'

        qv = nc.createVariable("qv", dtype('int16'), ("time", "lat", "lon"))
        qv.long_name = 'specific humidity on v wind'
        qv.units = 'm/s/g'
        qv.standard_name = 'specific_humidity_v'

        div = nc.createVariable("div", dtype('int16'), ("time", "lat", "lon"))
        div.long_name = 'water vapor divergence'
        div.units = 'mm/h'
        div.standard_name = 'water_vapor_divergence'

        lon[:], lat[:], time[:] = np.array(lonList), np.array(latList), np.array(timeList)
        w[:, :, :] = np.array(wList)
        qu[:, :, :] = np.array(quList)
        qv[:, :, :] = np.array(qvList)
        div[:, :, :] = np.array(divList)
        nc.close()

    @classmethod
    def createNcFileMSMsOnlyRain(cls, path, lonList, latList, timeList, rainList):
        nc = netCDF4.Dataset(path, "w", format="NETCDF4")
        nc.createDimension("lon", len(lonList))
        nc.createDimension("lat", len(latList))
        nc.createDimension("time", len(timeList))

        lon = nc.createVariable("lon", dtype('float32'), "lon")
        lon.long_name = 'longitude'
        lon.units = 'degrees_east'
        lon.standard_name = 'longitude'

        lat = nc.createVariable("lat", dtype('float32'), "lat")
        lat.long_name = 'latitude'
        lat.units = 'degrees_north'
        lat.standard_name = 'latitude'

        time = nc.createVariable("time", dtype('int16'), "time")
        time.long_name = 'time'
        time.unit = 'hours since 2020-07-03 00:00:00+00:00'
        time.standard_name = 'time'

        rain = nc.createVariable("rain", dtype('int16'), ("time", "lat", "lon"))
        rain.scale_factor = 0.006116208155
        rain.add_offset = 200.0
        rain.long_name = 'rainfall in 1 hour'
        rain.units = 'mm/h'
        rain.standard_name = 'rainfall_rate'

        lon[:], lat[:], time[:], rain[:, :, :] = np.array(lonList), np.array(latList), np.array(timeList), np.array(rainList)
        nc.close()