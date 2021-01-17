FROM ubuntu AS sys_base
WORKDIR /app
COPY tippecanoe ./tippecanoe
RUN cd tippecanoe \
    apt-get update \
    apt-get install libsqlite3-dev \
    apt-get install make \
    apt-get install build-essential \
    apt-get install libz-dev \
    make -j \
    make install \
    cd ../

