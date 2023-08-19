FROM soiqualang/geojson2mbtiles AS sys_base
WORKDIR /app
COPY merge-mbtiles ./merge-mbtiles
 
WORKDIR /app/merge-mbtiles

ENV TZ=Asia/Kolkata \
DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
	apt-get -y install npm && \
    npm install

RUN apt-get -y install python3-pip && \
	pip install --upgrade pip && \
	pip install -U tpkutils
    
WORKDIR /app
