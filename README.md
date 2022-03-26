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

* if error, which is permission denied, happens, execute this command  
` sudo chmod -R 777 ./ `

## SCALE

### tutorial

**初期値作成**  
`cd ~/scale-5.4.4/scale-rm/test/tutorial/ideal/`  
`cp sample/init_R20kmDX500m.conf ./init_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./scale-rm_init init_R20kmDX500m.conf` ※rootとして実行  

**シミュレーション実行**  
`cp sample/run_R20kmDX500m.conf ./run_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./scale-rm run_R20kmDX500m.conf`  

**後処理と描画**  
`ln -s ../../../util/netcdf2grads_h/net2g ./`  
`cp sample/net2g_R20kmDX500m.conf ./net2g_R20kmDX500m.conf`  
`mpirun --allow-run-as-root -n 2 ./net2g net2g_R20kmDX500m.conf`  
`grads -blc checkfig_ideal.gs`  
