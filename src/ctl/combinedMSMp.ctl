DSET ../combined/MSMp.nc
DTYPE netcdf
TITLE MSM surface
UNPACK scale_factor add_offset
OPTIONS yrev
UNDEF 9.96921e+36
XDEF 241 LINEAR 120 0.125
YDEF 253 LINEAR 22.4 0.1
ZDEF 16 LEVELS 1000 975 950 925 900 850 800 700 600 500 400 300 250 200 150 100
TDEF 248 LINEAR 01Z01JUL2020 3hr
VARS 6
    z=>z 16 t,z,y,x Geopotential Height m
    w=>w 16 t,z,y,x Vertical Wind Pa/s
    u=>u 16 t,z,y,x Zonal wind m/s
    v=>v 16 t,z,y,x meridional wind m/s
    temp=>temp 16 t,z,y,x temperature K
    rh=>rh 16 t,z,y,x relative humidity %
ENDVARS