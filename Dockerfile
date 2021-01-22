FROM ubuntu AS sys_base
WORKDIR /app
COPY tippecanoe ./tippecanoe
COPY json2mbtiles.py .

WORKDIR /app/tippecanoe
RUN apt-get update && \
    apt-get -y install libsqlite3-dev && \
    apt-get install make && \
    apt-get -y install build-essential && \
    apt-get -y install libz-dev && \
    apt-get -y install python3.8 && \
    make -j && \
    make install

WORKDIR /app
