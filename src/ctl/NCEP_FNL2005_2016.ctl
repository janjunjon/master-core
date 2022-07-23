dset ^fnl_20070714_18_00.grib1
title NCEP FNL Operational Model Global Tropospheric Analyses 2005 to 2016
options yrev template
undef 9.999e+20
xdef   360 linear   0.000000 1.000000
ydef   181 linear -90.000000 1.000000
zdef    26 levels
  1000 975 950 925 900 850 800 750 700 650
   600 550 500 450 400 350 300 250 200 150
   100  70  50  30  20  10
tdef 2 linear 00z04jul2020 3hr
vars 4
    pwv 0 99 precipitable water vapor
    qu 0 99 specific humidity u vector
    qv 0 99 specific humidity v vector
    a 0 99 water vapor divergence
ENDVARS
