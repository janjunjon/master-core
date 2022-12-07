*'sdfopen s20200704.nc'
*'open ra20200703.ctl'
*'open ra20200704.ctl'

filename_0000='ra/ra202007040000.bin'
filename_0300='ra/ra202007040300.bin'
filename_0600='ra/ra202007040600.bin'
filename_0900='ra/ra202007040900.bin'
filename_1200='ra/ra202007041200.bin'
filename_1500='ra/ra202007041500.bin'
filename_1800='ra/ra202007041800.bin'
filename_2100='ra/ra202007042100.bin'



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
