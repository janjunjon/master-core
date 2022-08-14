'q ctlinfo'
'sdfopen /home/jjthomson/fdrive/ra/ra202007_lonlat.nc'

'set grads off'
'set background 1'
'set mpdset hires'
'set gxout shaded'
'set lon 128 132'
'set lat 30 34'
'set t 1'

'color.gs 200 300 10 -kind white->rainbow'

'd rain'

'gxprint /home/jjthomson/master-core/img/confim_ra.png'

'reinit'
