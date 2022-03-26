FROM ubuntu
SHELL ["/bin/bash", "-c"]
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt upgrade && apt update && \
    apt install -y build-essential && \
    apt install -y openmpi-bin && \
    apt install -y git && \
    apt install -y gcc gfortran g++ libcurl4-openssl-dev m4 mlocate make wget && \
    apt install -y python3 python3-pip && \
    apt install -y libhdf5-dev hdf5-helpers hdf5-tools && \
    apt install -y libnetcdf-dev libnetcdff-dev libnetcdf-c++4-dev && \
    apt install -y liblapack-dev libscalapack-openmpi-dev libatlas-base-dev && \
    apt install -y grads
RUN cd && \
    ompi_info | head >> ompi.txt && \
    nc-config --all >> nc-config.txt

# install SCALE
RUN cd && wget https://scale.riken.jp/archives/scale-5.4.4.tar.gz && \
    tar -zxvf scale-5.4.4.tar.gz
# export SCALE_SYS="Linux64-gnu-ompi"
ENV SCALE_SYS Linux64-gnu-ompi
RUN cd ~/scale-5.4.4/scale-rm/src && \
    make -j 4

# install net2g
RUN cd && cd scale-5.4.4/scale-rm/util/netcdf2grads_h && \
    make -j 2

# install SNO
RUN cd &&  cd scale-5.4.4/scale-rm/util/sno && \
    make

# mpiをrootとして実行することを許可
# ENV OMPI_ALLOW_RUN_AS_ROOT 1

# scale-5.4.4/bin にある実行バイナリへの静的リンクを張る
# 「scale-rm」はモデル本体、「scale-rm_init」は初期値/境界値作成ツール
RUN cd && cd scale-5.4.4/scale-rm/test/tutorial/ideal && \
    ln -s ../../../../bin/scale-rm ./ && \
    ln -s ../../../../bin/scale-rm_init ./

# install module
RUN pip install netCDF4 && \
    pip install matplotlib && \
    pip install pandas && \
    pip install sklearn && \
    pip install basemap