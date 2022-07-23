# core

## Docker

### docker image

* docker image build  
` docker image build -t "image_name" . `

* docker image pull  
` docker image pull jjthomson2166/scale-ubuntu `

* error stack  

```bash
sudo gpasswd -a $(whoami) docker
sudo chgrp docker /var/run/docker.sock
```

### docker container

* if you use F drive, execute this command and comment out mount in docker-compose.yml  
` sudo mount -t drvfs F: /mnt/f/ `

* before docker-compose up  
` docker cp scale-dev:/root/scale-5.4.4 ~/ `

* if you enter in command line in docker container  
` docker exec -it scale-dev bash `

* after you enter in docker container, execute this.  
` ./build/initial.sh `  

* if you exit container shell, execute this.  
` cp $HOME/scale-5.4.4 -R $HOME/fdrive `  

### others

* if error, which is `VS Code: NoPermissions (FileSystemError): Error: EACCES: permission denied`, happens, execute this command  
` sudo chown -R user {dir} `

## SCALE ([SCALE_user_guide](https://scale.riken.jp/archives/scale_users_guide.v5.4.4.pdf))

### tutorial

#### 理想大気実験

* 初期値作成  

```bash
export PATH=$PATH:$HOME/scale-5.4.4/scale-rm/test/tutorial
cd ~/scale-5.4.4/scale-rm/test/tutorial/ideal/
cp sample/init_R20kmDX500m.conf ./init_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./scale-rm_init init_R20kmDX500m.conf ※rootとして実行  
```

* シミュレーション実行  

```bash
cp sample/run_R20kmDX500m.conf ./run_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./scale-rm run_R20kmDX500m.conf
```

* 後処理と描画  

```bash
ln -s ../../../util/netcdf2grads_h/net2g ./
cp sample/net2g_R20kmDX500m.conf ./net2g_R20kmDX500m.conf
mpirun --allow-run-as-root -n 2 ./net2g net2g_R20kmDX500m.conf
grads -blc checkfig_ideal.gs
```

#### 現実大気実験

* `USER.sh`  
This is a file for configure and making `experiments/`  
`make`  

* 入力データ (境界値データ) の準備  

```bash
wget https://scale.riken.jp/archives/scale_database.tar.gz -P {dir_path} 
ln -s {dir_path}/scale_database ./
export SCALE_DB="{dir_path}/scale_database"
```

* pp : 地形データの作成の為の処理  

```bash
export Tutorial_DIR=$HOME/scale-5.4.4/scale-rm/test/tutorial
cd $Tutorial_DIR/real/tools
bash convert_FNL-grib2grads.sh 2007071418 2007071500 FNL_input FNL_output
```

* 実験セットの準備  

```bash
bash ~/core/initial
cd $Tutorial_DIR/real
make
```

* 地形データの作成：pp  

```bash
cd $Tutorial_DIR/real/experiment/pp/
mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm_pp pp.d01.conf
```

* 初期値/境界値データの作成：init  

```bash
cd ${Tutorial_DIR}/real/experiment/init
cp ../../data/gradsinput-link_FNL.sh ./
bash gradsinput-link_FNL.sh
ln -s ../../data/namelist.grads_boundary.FNL.2005053112-2016051106 ./
mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm_init init.d01.conf
```

* シミュレーションの実行：run  

```bash
cd ${Tutorial_DIR}/real/experiment/run
mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm run.d01.conf >& log &
```

* 結果のクイック描画：net2g  

```bash
cd ${Tutorial_DIR}/real/experiment/net2g
mpirun --allow-run-as-root --oversubscribe -n 4 ./net2g net2g.2D.d01.conf
mpirun --allow-run-as-root --oversubscribe -n 4 ./net2g net2g.3D.d01.conf
cp ../../data/checkfig_real.gs ./
grads -blc checkfig_real.gs
```

## Refference

* [SCALE_user_guide](https://scale.riken.jp/archives/scale_users_guide.v5.4.4.pdf)  
* [color.gs](http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/color.gs?lang=jp)  
* [xcbar.gs](http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/xcbar.gs?lang=en)  
