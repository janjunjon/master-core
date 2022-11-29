'open /home/jjthomson/fdrive/ra/ra.ctl'
*'sdfopen /home/jjthomson/fdrive/ra/ra202007_lonlat.nc'
'q ctlinfo'

'set grads off'
'set background 1'
'set mpdset hires'
'set gxout shaded'
'set lon 128 132.5'
'set lat 30 34.5'
*'set t 1'

t=1
while(t<=249)

'set t 't
'color.gs 0 200 20 -kind white->rainbow'
'd ra'

'xcbar 1.8 8.8 2.0 2.15 -edge triangle -fh 0.1 -ft 4 -fw 0.07 -line on'

'gxprint ../test/confirm_ra(t='t').png'
'c'

t=t+1
endwhile

'reinit'
