import os

class Execution:
    def __init__(self, savePath) -> None:
        self.savePath = savePath

    def main(self):
        filenames = self.filenames()
        filenumber = 1
        startTStep = 1
        for filename in filenames:
            endTStep = startTStep + 7
            scripts = self.scripts(filename, startTStep, endTStep)
            with open("{}/{}.gs".format(self.savePath, 'convertToNetCDF_{}'.format(filenumber)), 'w') as f:
                f.write(scripts)
            startTStep += 8
            filenumber += 1
    
    def filenames(self):
        days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        filenames = []
        for day in days:
            filename = '202007{}'.format(day)
            filenames.append(filename)
        return filenames

    def scripts(self, filename, startTStep, endTStep):
        scripts = '''
            'open ../ra.ctl'
            'q ctlinfo'

            filename='../conbinedNetCDF/ra{}.nc'

            'set gxout fwrite'
            'set undef dfile'
            'set fwrite 'filename

            'set t {} {}'
            'set x 1 2560'
            'set y 1 3360'

            'define rain = ra'
            'set sdfwrite 'filename
            'sdfwrite rain'

            'reinit'

        '''.format(filename, startTStep, endTStep)
        return scripts