from array import array
import struct
import numpy as np

class RA():
    def convertIntToFloat(self, path):
        with open(path, 'rb') as f:
            data = f.read(2)
            # print(data)
            decoded_data = int.from_bytes(data, 'big')
            print(decoded_data)
        return

class RAtest():
    def __init__(self) -> None:
        self.lat = 3360
        self.lon = 2560
        self.rain = [0]*self.lat*self.lon

    def convertIntToFloat(self, path):
        i=0
        with open(path, 'rb') as f:
            while True:
                data = f.read(2)
                if data == None:
                    break
                try:
                    self.rain[i] = struct.unpack('h', data)[0]/10
                except:
                    continue
                i=i+1
            self.grid_rain = np.reshape(self.rain, (self.lat, self.lon))
        return self.grid_rain

    def write(self, path):
        arr = bytearray(self.rain)
        b_arr = bytes(arr)
        with open(path, 'wb') as f:
            f.write(b_arr)