import subprocess

def main():
    for conbinations in filenames():
        command = "/home/jjthomson/master-core/src/c/short2f4ra1km {} {}".format(conbinations[0], conbinations[1])
        print(command)
        subprocess.run(command, shell=True)

def filenames():
    combinations = []
    days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
    hours = ["0300", "0600", "0900", "1200", "1500", "1800", "2100", "2400"]
    for day in days:
        for hour in hours:
            input = "/home/jjthomson/fdrive/ra/202007/{}/202007{}{}.bin".format(day, day, hour)
            output = "/home/jjthomson/fdrive/ra/converted/202007{}{}_converted.bin".format(day, hour)
            arr = [input, output]
            combinations.append(arr)
    return combinations

if __name__ == "__main__":
    main()