#! /bin/sh

wget https://support.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.10.5.tar.gz -P ~/
sudo tar zxvf ~/hdf5-1.10.5.tar.gz -C ~/

cd ~/hdf5-1.10.5
# sudo make clean
# sudo ./configure --prefix=/usr/local/hdf5-1.10.5 \
#             --enable-fortran \
#             --with-szlib=/usr  \
#             --enable-threadsafe \
#             --with-pthread=/usr/include/,/usr/lib \
#             --enable-hl --enable-shared --enable-unsupported
sudo ./configure --enable-fortran --enable-hl --enable-shared \
            --prefix=/usr/local/hdf5-1.10.5 \
            --enable-threadsafe --with-pthread=/usr/include/,/usr/lib/x86_64-linux-gnu --enable-unsupported
sudo make &> hdf5_logs.txt
# sudo make check
sudo make install