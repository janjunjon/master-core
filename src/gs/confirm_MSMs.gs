filename='/home/jjthomson/fdrive/nc/s20200701.nc'

'sdfopen 'filename
'q ctlinfo'

'set grads off'
'set background 1'
'set mpdset hires'
'set gxout shaded'
'set lon 128 132'
'set lat 30 34'
'set t 1'

'color.gs 200 300 10 -kind white->rainbow'

'd r1h'

'reinit'
