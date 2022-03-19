#! /bin/sh

# netCDF4
# download
wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.7.4.tar.gz -P ~/
mv ~/v4.7.4.tar.gz ~/netcdf-c-4.7.4.tar.gz
sudo tar zxvf ~/netcdf-c-4.7.4.tar.gz -C ~/

# PATH(ubuntu)
# for netCDF4
# export FC=gfortran
# export CC=gcc

# hdf5 path
# export CPATH=$CPATH:/usr/local/hdf5/include
# export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/hdf5/lib

# netCDF4
# export NCDIR=/usr/local/netcdf-c-4.7.4
# export CPPFLAGS="-I/usr/local/szip/include -I/usr/local/hdf5-1.10.5/include"
# export LDFLAGS="-L/usr/local/szip/lib -L/usr/local/hdf5-1.10.5/lib"

sudo su
# .profile
# export NCDIR=/usr/local/netcdf-c-4.7.4
# export CPPFLAGS="-I/usr/local/szip/include -I/usr/local/hdf5-1.10.5/include"
# export LDFLAGS="-L/usr/local/szip/lib -L/usr/local/hdf5-1.10.5/lib"

cd /home/ubuntu/netcdf-c-4.7.4
sudo ./configure --prefix=${NCDIR} --enable-netcdf-4 --enable-shared --enable-dap --disable-dap-remote-tests \
            --with-curl=/usr/include/x86_64-linux-gnu/curl
sudo make
sudo make install