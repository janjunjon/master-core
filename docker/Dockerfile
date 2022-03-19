FROM ubuntu
SHELL ["/bin/bash", "-c"]
RUN apt upgrade && apt update && \
    apt install -y build-essential && \
    apt install -y gcc gfortran g++ libcurl4-openssl-dev m4 mlocate make wget openmpi-bin && \
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
RUN cd scale-5.4.4/scale-rm/src && \
    make -j 4

RUN apt install -y python3 python3-pip