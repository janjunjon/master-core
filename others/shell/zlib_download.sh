#! /bin/sh

# zlib
wget http://www.zlib.net/zlib-1.2.11.tar.gz -P ~/
sudo tar zxvf ~/zlib-1.2.11.tar.gz -C ~/

cd ~/zlib-1.2.11
sudo ./configure --prefix=/usr/local
sudo make
sudo make install