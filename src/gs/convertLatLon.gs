'open ../ctl/ra.ctl'
'q ctlinfo'

filename='/home/jjthomson/fdrive/ra/ra202007_lonlat.nc'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename

'set lon 128 132'
'set lat 30 34'
'set t 1 249'

'define rain = ra'
'set sdfwrite 'filename
'sdfwrite rain'

'reinit'
