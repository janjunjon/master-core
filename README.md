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
