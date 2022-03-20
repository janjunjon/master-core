#! /bin/sh

wget https://support.hdfgroup.org/ftp/lib-external/szip/2.1.1/src/szip-2.1.1.tar.gz -P ~/
sudo tar zxvf ~/szip-2.1.1.tar.gz -C ~/

cd ~/szip-2.1.1
sudo ./configure --prefix=/usr/local
sudo make
sudo make install