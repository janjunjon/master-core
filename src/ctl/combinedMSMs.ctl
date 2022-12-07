DSET ../combined/MSMs.nc
DTYPE netcdf
TITLE MSM surface
UNPACK scale_factor add_offset
OPTIONS yrev
UNDEF 9.96921e+36
XDEF 241 LINEAR 120 0.125
YDEF 253 LINEAR 22.4 0.1
ZDEF 1 LINEAR 0 1
TDEF 248 LINEAR 01Z01JUL2020 3hr
VARS 12
    psea=>psea  0  t,y,x  sea level pressure
    sp=>sp  0  t,y,x  surface air pressure
    u=>u  0  t,y,x  eastward component of wind
    v=>v  0  t,y,x  northward component of wind
    temp=>temp  0  t,y,x  temperature
    rh=>rh  0  t,y,x  relative humidity
    r1h=>r1h  0  t,y,x  rainfall in 1 hour
    ncld_upper=>ncld_upper  0  t,y,x  upper-level cloudiness
    ncld_mid=>ncld_mid  0  t,y,x  mid-level cloudiness
    ncld_low=>ncld_low  0  t,y,x  low-level cloudiness
    ncld=>ncld  0  t,y,x  cloud amount
    dswrf=>dswrf  0  t,y,x  Downward Short-Wave Radiation Flux
ENDVARS