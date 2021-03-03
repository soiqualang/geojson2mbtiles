# geojson2mbtiles
Tool to convert GeoJson to Mbtiles

https://hub.docker.com/repository/docker/soiqualang/geojson2mbtiles

> Test với Google Colab

https://colab.research.google.com/drive/1TLIMNu9T2ZFUDy4hsB-S4ZsoXXKACgS1#scrollTo=MVrN7rSMFxuo

> Build docker

```bash
docker build -t geojson2mbtiles:1.0 .
```

> Run Docker

```bash
docker run -it -d --name geojson2mbtiles -v E:/tmp:/data geojson2mbtiles:1.0

docker run -it -d --name geojson2mbtiles -v E:/program_data/python/geojson2mbtiles:/data geojson2mbtiles:1.0

docker run -it -d --name geojson2mbtiles -v D:/tmp2:/data geojson2mbtiles:1.0
```

> test

```bash
docker exec -it geojson2mbtiles /bin/sh

python3.8 argu.py -input "input" -hallo "hallo" -xinchao "xinchao"
```

> Command

```bash
tippecanoe -z18 -o thamthucvat.mbtiles --drop-densest-as-needed thamthucvat.geojson
tippecanoe -zg -o thamthucvat.mbtiles --drop-densest-as-needed thamthucvat.geojson

docker exec -it geojson2mbtiles python3.8 json2mbtiles.py -geojson_folder_path "/data/geojson2mbtiles/geojson/" -mbtiles_folder_path "/data/geojson2mbtiles/mbtiles/" -maxzoom 18

docker exec -it geojson2mbtiles python3.8 "/data/geojson2mbtiles/json2mbtiles.py" -geojson_folder_path "/data/geojson2mbtiles/geojson/" -mbtiles_folder_path "/data/geojson2mbtiles/mbtiles/" -maxzoom 18


docker exec -it geojson2mbtiles tippecanoe -zg -f -o "/data/geojson2mbtiles/mbtiles/t_1vn_hientrang_sdd2015.mbtiles" --drop-densest-as-needed "/data/geojson2mbtiles/geojson/1vn_hientrang_sdd2015.geojson"
```

https://github.com/mapbox/tippecanoe