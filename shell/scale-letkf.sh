#! /bin/sh

sudo yum install -y gcc gcc-c++ openssl-devel readline-devel zlib-devel
sudo yum install -y gcc-gfortran libgfortran
cd

# m4
# wget http://ftp.gnu.org/gnu/m4/m4-1.4.15.tar.gz
# sudo tar zxvf m4-1.4.15.tar.gz
# cd ~/m4-1.4.15
# cd lib
# sudo sed -i -e '/gets is a security/d' ./stdio.h
# cd ../
# sudo ./configure --prefix=/usr
# sudo make
# sudo make install

# zlib
wget http://www.zlib.net/zlib-1.2.11.tar.gz
sudo tar zxvf zlib-1.2.11.tar.gz
# szip
wget https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz
sudo tar zxvf szip-2.1.1.tar.gz
# jpegsrc
wget http://www.ijg.org/files/jpegsrc.v9d.tar.gz
sudo tar zxvf jpegsrc.v9d.tar.gz
# curl
wget http://curl.haxx.se/download/curl-7.37.0.tar.gz
sudo tar zxvf curl-7.37.0.tar.gz
# hdf5
wget https://support.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.10.5.tar.gz
sudo tar zxvf hdf5-1.10.5.tar.gz
# netCDF4
wget https://github.com/Unidata/netcdf-c/archive/refs/tags/v4.7.4.tar.gz
mv v4.7.4.tar.gz netcdf-c-4.7.4.tar.gz
sudo tar zxvf netcdf-c-4.7.4.tar.gz


# zlib
cd ~/zlib-1.2.11
sudo ./configure --prefix=/usr
sudo make
sudo make install
# szip
cd ~/szip-2.1.1
sudo ./configure --prefix=/usr
sudo make
sudo make install
# jpeg
cd ~/jpeg-9d
sudo ./configure --prefix=/usr
sudo make
sudo make install
# curl
cd ~/curl-7.37.0
sudo ./configure --prefix=/usr --enable-libcurl-option
sudo make
sudo make install
# hdf5
cd ~/hdf5-1.10.5
sudo ./configure --prefix=/usr/local/hdf5-1.10.5 \
            --enable-fortran \
            --with-szlib=/usr  \
            --enable-threadsafe \
            --with-pthread=/usr/include/,/usr/lib \
            --enable-hl --enable-shared --enable-unsupported
sudo make
sudo make check
sudo make install
cd /usr/local
sudo ln -s ~/hdf5-1.10.5 /usr/local/hdf5

#netCDF4
cd netcdf-c-4.7.4
sudo ./configure --prefix=${NCDIR} --enable-netcdf-4 --enable-shared --enable-dap --disable-dap-remote-tests \
            --with-curl=/usr/include/x86_64-linux-gnu/curl
sudo make
sudo make install

# vim .bashrc
# export LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/usr/local/hdf5/lib"
# export LIBRARY_PATH="${LIBRARY_PATH}:/usr/local/hdf5/lib"
# export PATH="${PATH}:/usr/local/hdf5/lib"
# export NCDIR=/usr/local/netcdf-c-4.7.4
# export CPPFLAGS="-I/usr/local/szip/include -I/usr/local/hdf5/include"
# export LDFLAGS="-L/usr/local/szip/lib -L/usr/local/hdf5/lib"



# export FC=gfortran
# export FFLAGS=" -assume byterecl -convert big_endian "

# export CC=gcc
# export F77=$FC

# hdf5
# HDF5_HOME=/usr/local/hdf5
# HDF5_LIB=$HDF5_HOME/lib
# HDF5_INC=$HDF5_HOME/include
# PATH="$HDF5_HOME/bin:$PATH"
# LD_LIBRARY_PATH=${HDF5_LIB}:$LD_LIBRARY_PATH

# export HDF5_HOME HDF5_INC HDF5_LIB

# export LD_LIBRARY_PATH
# # netCDF4
# export NCDIR=/usr/local/netcdf-c-4.7.4
# export CPPFLAGS="-I/usr/local/szip/include -I/usr/local/hdf5/include"
# export LDFLAGS="-L/usr/local/szip/lib -L/usr/local/hdf5/lib"

# export FC=gfortran
# export FFLAGS=" -assume byterecl -convert big_endian "

# export CC=gcc
# export F77=$FC