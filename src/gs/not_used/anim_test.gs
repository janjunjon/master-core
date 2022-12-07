'open anl_column125/JRA_data/all_year.ctl'
'open anl_p125/JRA_data/all_year.ctl'

*'set t 1'
*'d w.2'
*'d pwat'
*say result

time=1
while(time<=212)

'set background 1'
'set lat 15 50'
'set lon 80 150'
'set grads off'
'set map 1 1 8'
'set gxout shaded'
'set xlopts 1 1 0.08'

*'color.gs -10 10 2 -kind brown->white->blue'
*'color.gs -50 50 10 -kind blue->white->red'

*'set t 1'

'color.gs 0 65 5 -kind rainbow'
'set parea 0.6 4.76 0 8.5'
'd pwat(t='time')'
say result
*'xanim -sec 2 pwat_gds0_eatm'

'color.gs 0 65 5 -kind rainbow'
'set parea 5.6 9.76 0 8.5'
'd w.2(t='time')'
say result
*'xanim -sec 2 w'

'set gxout vector'
'set ccolor 1'
'set arrlab on'
'set arrscl 1 2000'
'set parea 0.6 4.76 0 8.5'
'd skip(uwv(t='time'),2,2);vwv(t='time')'
say result

'set gxout vector'
'set ccolor 1'
'set arrlab on'
'set arrscl 1 2000'
'set parea 5.6 9.76 0 8.5'
'd skip(qu.2(t='time'),2,2);qv.2(t='time')'
say result

'xcbar 1.0 9.0 1.8 2.0 -edge triangle'

*'set strsiz 0.2'
'set strsiz 0.15 0.25'
'set string 1 c 6'

title='PWV(kg/m^2)_and_water_vapor_flux(kg/m/s)_2000_t='time
title1='anl_column125'
title2='anl_p125'
filename='PWV_and_water_vapor_flux_'
 
'draw string 5.0 6.75 'title
'draw string 2.75 5.75 'title1
'draw string 7.75 5.75 'title2
'gxprint 'filename't'time'.png'
'c'
*'enable print 'filename't='time'.gmf'
*'print'
*'disable print'

time=time+1
endwhile

*'!gxeps -c -i 'filename't='time'.gmf -o 'filename't='time'.ps'
*'!rm 'filename't='time'.gmf'