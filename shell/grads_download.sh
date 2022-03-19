#! /bin/bash

# wget ftp://cola.gmu.edu/grads/2.0/grads-2.0.2-bin-i686-pc-linux-gnu.tar.gz -P ~/
wget ftp://cola.gmu.edu/grads/2.2/grads-2.2.1-bin-i686-pc-linux-gnu.tar.gz -P ~/
# tar xzvf ~/grads-2.0.2-bin-i686-pc-linux-gnu.tar.gz -C ~/
tar xzvf ~/grads-2.2.1-bin-i686-pc-linux-gnu.tar.gz -C /usr/local/
# wget https://sourceforge.net/projects/opengrads/files/grads2/2.2.1.oga.1/Linux%20%2864%20Bits%29/opengrads-2.2.1.oga.1-bundle-x86_64-pc-linux-gnu-glibc_2.17.tar.gz  -P ~/
# tar xzvf ~/opengrads-2.2.1.oga.1-bundle-x86_64-pc-linux-gnu-glibc_2.17.tar.gz -C ~/

# cd ~/grads-2.0.2

# export PATH=$PATH:/usr/local/grads-2.0.2/bin
# export GASCRP=/usr/local/grads-2.0.2/lib/
# export GADDIR=/usr/local/grads-2.0.2/data/
# export GASHP=/usr/local/grads-2.0.2/shape/

# sudo ./configure
# sudo make
# sudo make install