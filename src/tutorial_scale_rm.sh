#!/bin/bash

# ** 初期値作成 **
cd ~/scale-5.4.4/scale-rm/test/tutorial/ideal/
cp sample/init_R20kmDX500m.conf ./init_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./scale-rm_init init_R20kmDX500m.conf ※rootとして実行

# ** シミュレーション実行 **
cp sample/run_R20kmDX500m.conf ./run_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./scale-rm run_R20kmDX500m.conf

# ** 後処理と描画 **
ln -s ../../../util/netcdf2grads_h/net2g ./
cp sample/net2g_R20kmDX500m.conf ./net2g_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./net2g net2g_R20kmDX500m.conf
grads -blc checkfig_ideal.gs
