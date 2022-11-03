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
        for i in range(7):
            self.combinedData[i].extend(self.example_4()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_5()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_6()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_7()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_8()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_9()[i])
        for i in range(7):
            self.combinedData[i].extend(self.example_10()[i])
        return self.combinedData

    def example_1(self):
        # t=23-27, lat=28-33, lon=128-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[23:27, 56:106, 64:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[23:27, 56:106, 64:104])
        w = np.ravel(np.array(self.w)[23:27, 56:106, 64:104])
        u = np.ravel(np.array(self.u)[23:27, 56:106, 64:104])
        v = np.ravel(np.array(self.v)[23:27, 56:106, 64:104])
        temp = np.ravel(np.array(self.temp)[23:27, 56:106, 64:104])
        rh = np.ravel(np.array(self.rh)[23:27, 56:106, 64:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_2(self):
        # t=39, lat=28-33, lon=125-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[39, 56:106, 40:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[39, 56:106, 40:104])
        w = np.ravel(np.array(self.w)[39, 56:106, 40:104])
        u = np.ravel(np.array(self.u)[39, 56:106, 40:104])
        v = np.ravel(np.array(self.v)[39, 56:106, 40:104])
        temp = np.ravel(np.array(self.temp)[39, 56:106, 40:104])
        rh = np.ravel(np.array(self.rh)[39, 56:106, 40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_3(self):
        # t=41, lat=28-33, lon=128-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[41, 56:106, 64:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[41, 56:106, 64:104])
        w = np.ravel(np.array(self.w)[41, 56:106, 64:104])
        u = np.ravel(np.array(self.u)[41, 56:106, 64:104])
        v = np.ravel(np.array(self.v)[41, 56:106, 64:104])
        temp = np.ravel(np.array(self.temp)[41, 56:106, 64:104])
        rh = np.ravel(np.array(self.rh)[41, 56:106, 64:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_4(self):
        # t=45, lat=30.5-33, lon=125-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[45, 81:106, 40:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[45, 81:106, 40:104])
        w = np.ravel(np.array(self.w)[45, 81:106, 40:104])
        u = np.ravel(np.array(self.u)[45, 81:106, 40:104])
        v = np.ravel(np.array(self.v)[45, 81:106, 40:104])
        temp = np.ravel(np.array(self.temp)[45, 81:106, 40:104])
        rh = np.ravel(np.array(self.rh)[45, 81:106, 40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_5(self):
        # t=56, lat=32.5-35, lon=130-135
        rain_Ra = np.ravel(np.array(self.rain_Ra)[56, 101:126, 80:120])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[56, 101:126, 80:120])
        w = np.ravel(np.array(self.w)[56, 101:126, 80:120])
        u = np.ravel(np.array(self.u)[56, 101:126, 80:120])
        v = np.ravel(np.array(self.v)[56, 101:126, 80:120])
        temp = np.ravel(np.array(self.temp)[56, 101:126, 80:120])
        rh = np.ravel(np.array(self.rh)[56, 101:126, 80:120])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_6(self):
        # t=106, lat=30.5-33, lon=128-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[106, 81:106, 64:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[106, 81:106, 64:104])
        w = np.ravel(np.array(self.w)[106, 81:106, 64:104])
        u = np.ravel(np.array(self.u)[106, 81:106, 64:104])
        v = np.ravel(np.array(self.v)[106, 81:106, 64:104])
        temp = np.ravel(np.array(self.temp)[106, 81:106, 64:104])
        rh = np.ravel(np.array(self.rh)[106, 81:106, 64:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_7(self):
        # t=186, lat=28-33, lon=125-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[186, 56:106, 40:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[186, 56:106, 40:104])
        w = np.ravel(np.array(self.w)[186, 56:106, 40:104])
        u = np.ravel(np.array(self.u)[186, 56:106, 40:104])
        v = np.ravel(np.array(self.v)[186, 56:106, 40:104])
        temp = np.ravel(np.array(self.temp)[186, 56:106, 40:104])
        rh = np.ravel(np.array(self.rh)[186, 56:106, 40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_8(self):
        # t=191-195, lat=25-35, lon=125-135
        rain_Ra = np.ravel(np.array(self.rain_Ra)[191:195, 26:126, 40:120])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[191:195, 26:126, 40:120])
        w = np.ravel(np.array(self.w)[191:195, 26:126, 40:120])
        u = np.ravel(np.array(self.u)[191:195, 26:126, 40:120])
        v = np.ravel(np.array(self.v)[191:195, 26:126, 40:120])
        temp = np.ravel(np.array(self.temp)[191:195, 26:126, 40:120])
        rh = np.ravel(np.array(self.rh)[191:195, 26:126, 40:120])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_9(self):
        # t=200-201, lat=28-33, lon=125-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[200:201, 56:106, 40:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[200:201, 56:106, 40:104])
        w = np.ravel(np.array(self.w)[200:201, 56:106, 40:104])
        u = np.ravel(np.array(self.u)[200:201, 56:106, 40:104])
        v = np.ravel(np.array(self.v)[200:201, 56:106, 40:104])
        temp = np.ravel(np.array(self.temp)[200:201, 56:106, 40:104])
        rh = np.ravel(np.array(self.rh)[200:201, 56:106, 40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh

    def example_10(self):
        # t=207, lat=30.5-36, lon=125-133
        rain_Ra = np.ravel(np.array(self.rain_Ra)[207, 81:136, 40:104])
        rain_MSMs = np.ravel(np.array(self.rain_MSMs)[207, 81:136, 40:104])
        w = np.ravel(np.array(self.w)[207, 81:136, 40:104])
        u = np.ravel(np.array(self.u)[207, 81:136, 40:104])
        v = np.ravel(np.array(self.v)[207, 81:136, 40:104])
        temp = np.ravel(np.array(self.temp)[207, 81:136, 40:104])
        rh = np.ravel(np.array(self.rh)[207, 81:136, 40:104])
        return rain_Ra, rain_MSMs, w, u, v, temp, rh