'sdfopen s20200704.nc'

'set x 1 481'
'set y 1 505'

t=1
while(t<=8)

'set grads off'
'set background 1'
'set mpdset hires'
'set gxout shaded'
'set t 't

'color.gs 0 50 5 -kind white->rainbow'

* maskout(expr, mask)
* exprは描画したい変数、maskはマスクの判定を行うための変数です。
* ある地点におけるmaskの値が0以上の場合、exprをそのまま返します。
* maskの値が0未満の場合は、未定義値として扱われます。

*'rainfall=const(maskout(r1h, r1h),0,-u)'
'd r1h'

'cbarn'

'gxprint test_r1h(t='t').png'
'c'

t=t+1
endwhile
