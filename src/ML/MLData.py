import numpy as np

class Data:
    def __init__(self, data):
        self.combinedData = [[],[],[],[],[],[],[]]
        self.rain_Ra = data[0]
        self.rain_MSMs = data[1]
        self.w = data[2]
        self.u = data[3]
        self.v = data[4]
        self.temp = data[5]
        self.rh = data[6]

    def main(self):
        MLData = self.combineExamples()
        return MLData

    def combineExamples(self):
        for i in range(7):
            self.combinedData[i].extend(self.example_1()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_2()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_3()[i])
        return self.combinedData

    def example_1(self):
        # t=23-27, lat=28-33, lon=128-133
        rain_Ra = np.ravel(self.rain_Ra[23:27][56:106][64:104])
        rain_MSMs = np.ravel(self.rain_MSMs[23:27][56:106][64:104])
        w = np.ravel(self.w[23:27][56:106][64:104])
        u = np.ravel(self.u[23:27][56:106][64:104])
        v = np.ravel(self.v[23:27][56:106][64:104])
        temp = np.ravel(self.temp[23:27][56:106][64:104])
        rh = np.ravel(self.rh[23:27][56:106][64:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_2(self):
        # t=39, lat=28-33, lon=125-133
        rain_Ra = np.ravel(self.rain_Ra[39][56:106][40:104])
        rain_MSMs = np.ravel(self.rain_MSMs[39][56:106][40:104])
        w = np.ravel(self.w[39][56:106][40:104])
        u = np.ravel(self.u[39][56:106][40:104])
        v = np.ravel(self.v[39][56:106][40:104])
        temp = np.ravel(self.temp[39][56:106][40:104])
        rh = np.ravel(self.rh[39][56:106][40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_3(self):
        # t=41, lat=28-33, lon=128-133
        rain_Ra = np.ravel(self.rain_Ra[23:27][56:106][64:104])
        rain_MSMs = np.ravel(self.rain_MSMs[23:27][56:106][64:104])
        w = np.ravel(self.w[23:27][56:106][64:104])
        u = np.ravel(self.u[23:27][56:106][64:104])
        v = np.ravel(self.v[23:27][56:106][64:104])
        temp = np.ravel(self.temp[23:27][56:106][64:104])
        rh = np.ravel(self.rh[23:27][56:106][64:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh