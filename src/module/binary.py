class RA():
    def convertIntToFloat(self, path):
        with open(path, 'rb') as f:
            data = f.read()
            # print(data)
            decoded_data = int.from_bytes(data, 'big')
            print(decoded_data)
        return