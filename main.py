import src.module.netcdf as netcdf

def main():
    path = "/mnt/f/ishihara_juntaro/ishihara_master/0703.nc"
    nc = netcdf.read_netCDF(path)
    # config = netcdf.config_netCDF(nc)
    # print(config)
    netcdf.draw_pic(nc, "r1h")

if __name__ == "__main__":
    main()