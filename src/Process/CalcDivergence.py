import os

class Execution:
    def __init__(self) -> None:
        self.path = '/home/jjthomson/fdrive/nc/data'
        self.saveDir = '/home/jjthomson/fdrive/nc/scripts/div'
        self.makeDir()

    def main(self):
        files = os.listdir(self.path)
        for file in files:
            startString = file[0]
            if startString == 's':
                filename = file[1:9]
                print(filename)
                self.makeScripts(filename)

    def makeScripts(self, filename):
        scripts = '''
        'sdfopen ../../data/p{}.nc'
        'open ../converted/{}.ctl'

        startint=1
        endint=8
        filename='../../div/{}.bin'

        'set gxout fwrite'
        'set undef dfile'
        'set fwrite 'filename

        'set x 1 241'
        'set y 1 253'

        t=startint
        while(t<=endint)
        'set t 't

        'set lev 1000'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/1000))/(1-0.378*(e/1000))'
        'x=const(maskout(sp.2(z=1)/100-987.5,sp.2(z=1)/100-987.5),0,-u)'
        'w1000=q*x*100'
        'qu1000=u*w1000'
        'qv1000=v*w1000'
        'a1000=hdivg(qu1000,qv1000)'

        'set lev 975'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/975))/(1-0.378*(e/975))'
        'x=const(maskout(sp.2(z=1)/100-962.5,987.5-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-962.5),0,-u)'
        'w975=q*x*100'
        'qu975=u*w975'
        'qv975=v*w975'
        'a975=hdivg(qu975,qv975)'

        'set lev 950'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/950))/(1-0.378*(e/950))'
        'x=const(maskout(sp.2(z=1)/100-937.5,962.5-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-937.5),0,-u)'
        'w950=q*x*100'
        'qu950=u*w950'
        'qv950=v*w950'
        'a950=hdivg(qu950,qv950)'

        'set lev 925'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/925))/(1-0.378*(e/925))'
        'x=const(maskout(sp.2(z=1)/100-912.5,937.5-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-912.5),0,-u)'
        'w925=q*x*100'
        'qu925=u*w925'
        'qv925=v*w925'
        'a925=hdivg(qu925,qv925)'

        'set lev 900'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/900))/(1-0.378*(e/900))'
        'x=const(maskout(sp.2(z=1)/100-875,912.5-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-875),0,-u)'
        'w900=q*x*100'
        'qu900=u*w900'
        'qv900=v*w900'
        'a900=hdivg(qu900,qv900)'

        'set lev 850'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/850))/(1-0.378*(e/850))'
        'x=const(maskout(sp.2(z=1)/100-825,875-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-825),0,-u)'
        'w850=q*x*100'
        'qu850=u*w850'
        'qv850=v*w850'
        'a850=hdivg(qu850,qv850)'

        'set lev 800'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/800))/(1-0.378*(e/800))'
        'x=const(maskout(sp.2(z=1)/100-750,825-sp.2(z=1)/100),25,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-750),0,-u)'
        'w800=q*x*100'
        'qu800=u*w800'
        'qv800=v*w800'
        'a800=hdivg(qu800,qv800)'

        'set lev 700'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/700))/(1-0.378*(e/700))'
        'x=const(maskout(sp.2(z=1)/100-650,750-sp.2(z=1)/100),50,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-650),0,-u)'
        'w700=q*x*100'
        'qu700=u*w700'
        'qv700=v*w700'
        'a700=hdivg(qu700,qv700)'

        'set lev 600'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/600))/(1-0.378*(e/600))'
        'x=const(maskout(sp.2(z=1)/100-550,650-sp.2(z=1)/100),50,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-550),0,-u)'
        'w600=q*x*100'
        'qu600=u*w600'
        'qv600=v*w600'
        'a600=hdivg(qu600,qv600)'

        'set lev 500'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/500))/(1-0.378*(e/500))'
        'x=const(maskout(sp.2(z=1)/100-450,550-sp.2(z=1)/100),50,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-450),0,-u)'
        'w500=q*x*100'
        'qu500=u*w500'
        'qv500=v*w500'
        'a500=hdivg(qu500,qv500)'

        'set lev 400'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/400))/(1-0.378*(e/400))'
        'x=const(maskout(sp.2(z=1)/100-350,450-sp.2(z=1)/100),50,-u)'
        'x=const(maskout(x,sp.2(z=1)/100-350),0,-u)'
        'w400=q*x*100'
        'qu400=u*w400'
        'qv400=v*w400'
        'a400=hdivg(qu400,qv400)'

        'set lev 300'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/300))/(1-0.378*(e/300))'
        'w300=q*50*100'
        'qu300=u*w300'
        'qv300=v*w300'
        'a300=hdivg(qu300,qv300)'

        'set lev 250'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/250))/(1-0.378*(e/250))'
        'w250=q*37.5*100'
        'qu250=u*w250'
        'qv250=v*w250'
        'a250=hdivg(qu250,qv250)'

        'set lev 200'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/200))/(1-0.378*(e/200))'
        'w200=q*25*100'
        'qu200=u*w200'
        'qv200=v*w200'
        'a200=hdivg(qu200,qv200)'

        'set lev 150'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/150))/(1-0.378*(e/150))'
        'w150=q*25*100'
        'qu150=u*w150'
        'qv150=v*w150'
        'a150=hdivg(qu150,qv150)'

        'set lev 100'
        'esat=6.1078*pow(10,7.5*(temp-273.15)/(237.3+(temp-273.15)))'
        'e=esat*rh/100'
        'q=(0.622*(e/100))/(1-0.378*(e/100))'
        'w100=q*12.5*100'
        'qu100=u*w100'
        'qv100=v*w100'
        'a100=hdivg(qu100,qv100)'

        'w=(w1000+w975+w950+w925+w900+w850+w800+w700+w600+w500+w400+w300+w250+w200+w150+w100)/9.81'

        'qu=(qu1000+qu975+qu950+qu925+qu900+qu850+qu800+qu700+qu600+qu500+qu400+qu300+qu250+qu200+qu150+qu100)/9.81'
        'qv=(qv1000+qv975+qv950+qv925+qv900+qv850+qv800+qv700+qv600+qv500+qv400+qv300+qv250+qv200+qv150+qv100)/9.81'

        'a=(a1000+a975+a950+a925+a900+a850+a800+a700+a600+a500+a400+a300+a250+a200+a150+a100)/9.81*60*60*3'

        t=t+1
        endwhile

        'define div = a'
        'set sdfwrite 'filename
        'sdfwrite div'

        'reinit'
        '''.format(filename, filename, filename)
        with open('{}/{}.gs'.format(self.saveDir, filename), 'w') as f:
            f.write(scripts)

    def makeDir(self):
        if not os.path.exists(self.saveDir):
            os.mkdir(self.saveDir)