'open ../ctl/ra.ctl'
'q ctlinfo'

filename='/home/jjthomson/fdrive/ra/ra202007_lonlat.nc'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename

'set lon 127 133'
'set lat 29 35'
'set t 1 249'

'define rain = ra'
'set sdfwrite 'filename
'sdfwrite rain'

'reinit'
