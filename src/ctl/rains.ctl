DSET ../grads/rains.nc
DTYPE netcdf
TITLE RainFall by MSMs and Radar Amedas
UNPACK scale_factor add_offset
OPTIONS yrev
UNDEF 9.96921e+36
XDEF 241 LINEAR 120 0.125
YDEF 253 LINEAR 22.4 0.1
ZDEF 1 LINEAR 0 1
TDEF 248 LINEAR 01Z01JUL2020 3hr
VARS 2
    rain_Ra=>rain_Ra  0  t,y,x  RadarAmedas rain_fall in 1 hour
    rain_MSMs=>rain_MSMs  0  t,y,x  MSMs rain_fall in 1 hour
ENDVARS