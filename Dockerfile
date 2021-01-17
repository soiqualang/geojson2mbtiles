FROM ubuntu AS sys_base
WORKDIR /app
COPY tippecanoe ./tippecanoe

WORKDIR /app/tippecanoe
RUN apt-get update
RUN apt-get install libsqlite3-dev
RUN apt-get install make
RUN apt-get install build-essential
RUN apt-get install libz-dev
RUN make -j
RUN make install

WORKDIR /app