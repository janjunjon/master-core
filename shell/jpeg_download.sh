#! /bin/sh

# jpeg
wget http://www.ijg.org/files/jpegsrc.v9d.tar.gz -P ~/
sudo tar zxvf ~/jpegsrc.v9d.tar.gz -C ~/

cd ~/jpeg-9d
sudo ./configure --prefix=/usr/local
sudo make
sudo make install