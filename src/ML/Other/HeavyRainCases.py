import numpy as np

class Indexes:
    """
    get array index of specific heavy rain cases
    """
    def __init__(self) -> None:
        self.indexes = self.getAllIndexes()

    def getAllIndexes(self):
        indexes_case_1 = self.case_1()
        indexes_case_2 = self.case_2()
        indexes_case_3 = self.case_3()
        indexes_case_4 = self.case_4()
        indexes_case_5 = self.case_5()
        indexes_case_6 = self.case_6()
        indexes_case_7 = self.case_7()
        indexes_case_8 = self.case_8()
        indexes_case_9 = self.case_9()
        indexes_case_10 = self.case_10()
        varnames = ['indexes_case_{}'.format(i) for i in range(1,10+1)]
        all = []
        for varname in varnames:
            all.extend(locals()[varname])
        return all

    def getIndexes(self, T, LAT, LON):
        count = 0
        indexes = []
        for t in range(248):
            for lat in range(253):
                for lon in range(241):
                    if t in T and lat in LAT and lon in LON:
                        indexes.append(count)
                    count += 1
        return indexes
        
    def case_1(self):
        # t=23-27, lat=28-33, lon=128-133
        T = range(23,27)
        LAT = range(56,106)
        LON = range(64,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_2(self):
        # t=39, lat=28-33, lon=125-133
        T = [39]
        LAT = range(56,106)
        LON = range(40,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_3(self):
        # t=41, lat=28-33, lon=128-133
        T = [41]
        LAT = range(56,106)
        LON = range(64,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_4(self):
        # t=45, lat=30.5-33, lon=125-133
        T = [45]
        LAT = range(81,106)
        LON = range(40,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_5(self):
        # t=56, lat=32.5-35, lon=130-135
        T = [56]
        LAT = range(101,126)
        LON = range(80,120)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_6(self):
        # t=106, lat=30.5-33, lon=128-133
        T = [106]
        LAT = range(81,106)
        LON = range(64,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_7(self):
        # t=186, lat=28-33, lon=125-133
        T = [186]
        LAT = range(56,106)
        LON = range(40,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_8(self):
        # t=191-195, lat=25-35, lon=125-135
        T = range(191,195)
        LAT = range(26,126)
        LON = range(40,120)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_9(self):
        # t=200-201, lat=28-33, lon=125-133
        T = range(200,201)
        LAT = range(56,106)
        LON = range(40,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes

    def case_10(self):
        # t=207, lat=30.5-36, lon=125-133
        T = [207]
        LAT = range(81,136)
        LON = range(40,104)
        indexes = self.getIndexes(T, LAT, LON)
        return indexes