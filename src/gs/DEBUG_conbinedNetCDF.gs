'sdfopen ../conbinedNetCDF/ra20200701.nc'
'q ctlinfo'
say result

'set background 1'
'set lat 22 48'
'set lon 120 150'
'set grads off'
'set map 1 1 6'
'set gxout shaded'
'set xlopts 1 1 0.1'
'set ylopts 1 1 0.1'

'set gxout grfill'
'set rgb 21 70 70 70'
'set rgb 22 255 255 255'
'set rgb 23 127 0 255'
'set rgb 24 0 0 255'
'set rgb 25 0 128 255'
'set rgb 26 0 255 255'
'set rgb 27 0 255 0'
'set rgb 28 255 255 0'
'set rgb 29 255 128 0'
'set rgb 30 255 0 0'
'set rgb 31 255 0 127'
'set clevs -999 0 1 5 10 20 30 40 60 80'
'set ccols 21 22 23 24 25 26 27 28 29 30 31'

t=1
'set t 't
'd rain'
'xcbar 1.0 9.0 1.2 1.4 -edge triangle'

'set strsiz 0.2 0.25'
'set string 1 c 6'

title='rainfall_202007_t='t

'draw string 5.0 7.75 'title

'gxprint DEBUG_conbinedNetCDF.png'
'reinit'
