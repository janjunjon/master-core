import os

class Execution:
    def __init__(self, path, savePath) -> None:
        self.path = path
        self.savePath = savePath

    def main(self):
        filenames = self.filenames()
        for filename in filenames:
            scripts = self.scripts(filename)
            with open("{}/{}.ctl".format(self.savePath, filename), 'w') as f:
                f.write(scripts)
    
    def filenames(self):
        filenames = []
        files = os.listdir(self.path)
        for filename in files:
            filenames.append(filename.split('.')[0])
        return filenames

    def scripts(self, filename):
        scripts = '''
            dset ^../../converted/{}.nc
            title MSMs rain {}
            undef 9.96921e+36
            dtype netcdf
            xdef 241 linear 120 0.125
            ydef 253 linear 22.4 0.1
            zdef 1 linear 0 1
            tdef 8 linear 01Z01JUL2020 180mn
            vars 1
                rain=>rain  0  t,y,x  rainfall in 1 hour
            endvars
        '''.format(filename, filename)
        return scripts