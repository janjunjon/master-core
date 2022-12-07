'open ./combinedAtmos.ctl'

'q ctlinfo'
say result

'set background 1'
'set lat 22 48'
'set lon 120 150'
'set grads off'
'set map 1 1 6'
*'set gxout shaded'
'set xlopts 1 1 0.1'
'set ylopts 1 1 0.1'
'set z 1'

t=1
*while(t<=248)

'set t 't
*'color.gs -10 10 1 -kind blue->white->red'
'd pt'
*'xcbar 1.0 9.0 1.2 1.4 -edge triangle'

title=var'(t='t''
'set strsiz 0.2 0.25'
'set string 1 c 6'
'draw string 5.0 7.75 'title

'gxprint ../../images/DEBUG/grads/DEBUG_combinedAtmos_pt_t='t'.png'

*t=t+1
*endwhile