function main(args)
filename=subwrd(args,1)

'sdfopen s'filename'.nc'
'q file'
say result

'set gxout fwrite'
'set undef dfile'
'set fwrite 'middle/ra'filename'.bin

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

** ------------------------------------------------------ **

filename_0000='ra/ra'filename'0000.bin'
filename_0300='ra/ra'filename'0300.bin'
filename_0600='ra/ra'filename'0600.bin'
filename_0900='ra/ra'filename'0900.bin'
filename_1200='ra/ra'filename'1200.bin'
filename_1500='ra/ra'filename'1500.bin'
filename_1800='ra/ra'filename'1800.bin'
filename_2100='ra/ra'filename'2100.bin'


** 3hours accumulate rainfall **
** 00:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_0000

'set x 1 241'
'set y 1 253'

'd r1h(t=23)+r1h(t=24)+r1h.2(t=1)'

'disable fwrite'
reinit





** 03:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_0300

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=2, t=4)'

'disable fwrite'
reinit





** 06:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_0600

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=5, t=7)'

'disable fwrite'
reinit





** 09:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_0900

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=8, t=10)'

'disable fwrite'
reinit





** 12:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_1200

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=11, t=13)'

'disable fwrite'
reinit





** 15:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_1500

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=14, t=16)'

'disable fwrite'
reinit





** 18:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_1800

'set x 1 241'
'set y 1 253'
'd sum(r1h.2, t=17, t=19)'

'disable fwrite'
reinit





** 21:00 (UTC) **
'open ra20200703.ctl'
'open ra20200704.ctl'

'set gxout fwrite'
'set undef dfile'
'set fwrite 'filename_2100

'set x 1 241'
'set y 1 253'

'd sum(r1h.2, t=20, t=22)'

'disable fwrite'
reinit


** -------------------------------------------------------------- **

'open ra.ctl'
'q file'
filename='ra20200704.nc'

'set x 1 241'
'set y 1 253'
'set t 1 8'
'p=ra'
'set sdfwrite 'filename
'sdfwrite p'
say result

'reinit'

