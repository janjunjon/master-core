# core

## Docker

### docker image

* docker image build  
` docker image build -t "image_name" . `

* docker image pull  
` docker image pull jjthomson2166/scale-ubuntu `

### docker container

* if you use F drive, execute this command and comment out mount in docker-compose.yml  
` sudo mount -t drvfs F: /mnt/f/ `

* before docker-compose up  
` docker cp docker-app-1:/root/scale-5.4.4 ~/ `

* if you enter in command line in docker container  
` docker exec -it docker-app-1 bash `

### others

* if error, which is `VS Code: NoPermissions (FileSystemError): Error: EACCES: permission denied`, happens, execute this command  
` sudo chown -R user {dir} `

## SCALE [SCALE_user_guide](https://scale.riken.jp/archives/scale_users_guide.v5.4.4.pdf)

### tutorial

#### 理想大気実験

* 初期値作成  
`export PATH=$PATH:$HOME/scale-5.4.4/scale-rm/test/tutorial`
`cd ~/scale-5.4.4/scale-rm/test/tutorial/ideal/`  
`cp sample/init_R20kmDX500m.conf ./init_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./scale-rm_init init_R20kmDX500m.conf` ※rootとして実行  

* シミュレーション実行  
`cp sample/run_R20kmDX500m.conf ./run_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./scale-rm run_R20kmDX500m.conf`  

* 後処理と描画  
`ln -s ../../../util/netcdf2grads_h/net2g ./`  
`cp sample/net2g_R20kmDX500m.conf ./net2g_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./net2g net2g_R20kmDX500m.conf`  
`grads -blc checkfig_ideal.gs`  

#### 現実大気実験

* 入力データ (境界値データ) の準備  
`wget https://scale.riken.jp/archives/scale_database.tar.gz -P {dir_path}` in Drive  
`ln -s {dir_path}/scale_database ./`  
`export SCALE_DB="{dir_path}/scale_database"`  

* pp : 地形データの作成  
`export Tutorial_DIR=$HOME/scale-5.4.4/scale-rm/test/tutorial`  
`cd $Tutorial_DIR/real/tools`  
`bash convert_FNL-grib2grads.sh 2007071418 2007071500 FNL_input FNL_output`  

* 実験セットの準備  
`bash ~/core/initial`
`cd $Tutorial_DIR/real`  
`make`  

* 地形データの作成：pp  
`cd $Tutorial_DIR/real/experiment/pp/`  
`mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm_pp pp.d01.conf`  

* 初期値/境界値データの作成：init  
`cd ${Tutorial_DIR}/real/experiment/init`  
`cp ../../data/gradsinput-link_FNL.sh ./`  
`bash gradsinput-link_FNL.sh`  
`ln -s ../../data/namelist.grads_boundary.FNL.2005053112-2016051106 ./`  
`mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm_init init.d01.conf`

* シミュレーションの実行：run  
`cd ${Tutorial_DIR}/real/experiment/run`  
`mpirun --allow-run-as-root --oversubscribe -n 4 ./scale-rm run.d01.conf >& log &`  

* 結果のクイック描画：net2g  
`cd ${Tutorial_DIR}/real/experiment/net2g`  
`mpirun --allow-run-as-root --oversubscribe -n 4 ./net2g net2g.2D.d01.conf`  
`mpirun --allow-run-as-root --oversubscribe -n 4 ./net2g net2g.3D.d01.conf`  
`cp ../../data/checkfig_real.gs ./`  
`grads -blc checkfig_real.gs`  

## Refference

* [SCALE_user_guide](https://scale.riken.jp/archives/scale_users_guide.v5.4.4.pdf)  
* [color.gs](http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/color.gs?lang=jp)  
* [xcbar.gs](http://kodama.fubuki.info/wiki/wiki.cgi/GrADS/script/xcbar.gs?lang=en)  
