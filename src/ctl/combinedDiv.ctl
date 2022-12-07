DSET ../combined/div.nc
DTYPE netcdf
TITLE PWV, QU, QV, DIV From MSM
UNPACK scale_factor add_offset
OPTIONS yrev
UNDEF 9.96921e+36
XDEF 241 LINEAR 120 0.125
YDEF 253 LINEAR 22.4 0.1
ZDEF 1 LINEAR 0 1
TDEF 248 LINEAR 01Z01JUL2020 3hr
VARS 4
    pwv=>pwv  0  t,y,x  precipitable water vaper
    qu=>qu  0  t,y,x  specific humidity on u wind
    qv=>qv  0  t,y,x  specific humidity on v wind
    div=>div  0  t,y,x  water vapor divergence
ENDVARS