DSET ../combined/atmos.nc
DTYPE netcdf
TITLE Atmospheric Indexes From MSM
UNPACK scale_factor add_offset
OPTIONS yrev
UNDEF 9.96921e+36
XDEF 241 LINEAR 120 0.125
YDEF 253 LINEAR 22.4 0.1
ZDEF 16 LEVELS 1000 975 950 925 900 850 800 700 600 500 400 300 250 200 150 100
TDEF 248 LINEAR 01Z01JUL2020 3hr
VARS 9
    pt=>pt  16  t,z,y,x potential temperature
    ept=>ept  16  t,z,y,x equivalent potential temperature
    td=>td  0  t,y,x  dew point temperature
    tl=>tl  0  t,y,x  condensation temperature
    lcl=>lcl  0  t,y,x  lifted condensation level
    ssi=>ssi  0  t,y,x  Showalter Stability Index
    ki=>ki  0  t,y,x  K Index
    uvs=>uvs  0  t,y,x  eastward vertical sheer
    vvs=>vvs  0  t,y,x  northward vertical sheer
ENDVARS