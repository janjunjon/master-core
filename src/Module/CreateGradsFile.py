class Grads:
    @classmethod
    def createCtlFileV3Results(cls, save_path, dirPath):
        # {}=dirPath: Rain/SDGRegressor/pattern1
        scripts = '''
            DSET ../../../v3/{}.nc
            DTYPE netcdf
            TITLE Rainfall corrected by MLCorrectModel
            OPTIONS yrev
            UNDEF 9.96921e+36
            XDEF 241 LINEAR 120 0.125
            YDEF 253 LINEAR 22.4 0.1
            ZDEF 1 LINEAR 0 1
            TDEF 248 LINEAR 01Z01JUL2020 3hr
            VARS 3
                rain_Ra=>rain_Ra  0  t,y,x  RadarAmedas rain_fall in 1 hour
                rain=>rain  0  t,y,x  corrected rain
                devi=>devi  0  t,y,x  square deviation for RMSE
            ENDVARS
        '''.format(dirPath)
        with open(save_path, 'w') as f:
            f.write(scripts)
    
    @classmethod
    def createGsFileV3Results(cls, save_path, dirPath):
        # {}=dirPath: Rain/SDGRegressor/pattern1
        scripts = '''
            'open ../../../v3_ctl/{}.ctl'

            'q ctlinfo 1'
            say result

            'set background 1'
            'set lat 22 48'
            'set lon 120 150'
            'set grads off'
            'set map 1 1 6'
            'set gxout shaded'
            'set xlopts 1 1 0.1'
            'set ylopts 1 1 0.1'

            t=1
            while(t<=248)

            'set t 't

            * rain_Ra
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
            'set parea 0.6 4.76 0 8.5'
            'd rain_Ra'

            * predicted
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
            'set parea 5.6 9.76 0 8.5'
            'd rain'

            *'../../../../scripts/xcbar 1.0 9.0 1.2 1.4 -edge triangle'
            'cbarn'

            'set strsiz 0.25 0.25'
            'set string 1 c 6'

            title='rainfall_202007_t='t
            title1='rain_RA'
            title2='corrected rain'

            'draw string 5.0 7.75 'title
            'draw string 2.75 6.75 'title1
            'draw string 7.75 6.75 'title2

            'gxprint ../../../v3_images/{}/corrected_rain_t='t'.png'


            t=t+1
            endwhile

            'reinit'

        '''.format(dirPath, dirPath)
        with open(save_path, 'w') as f:
            f.write(scripts)