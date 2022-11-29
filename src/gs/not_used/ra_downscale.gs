'sdfopen s20200703.nc'

filename='middle/ra20200703.bin'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename

'set x 1 481'
'set y 1 505'

t=1
while(t<=24)
'set t 't
*say result

y=1
while(y<=505)
'set y 'y
*say result

x=1
while(x<=481)
'set x 'x
*say result

'd r1h'
say result

x=x+2
endwhile

y=y+2
endwhile

t=t+1
endwhile

'disable fwrite'
'reinit'
