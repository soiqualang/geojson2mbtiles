# geojson2mbtiles
Tool to convert GeoJson to Mbtiles

A tool to:
* Convert single geojson file to mbtile file
* Convert whole geojson folder file to mbtile files

https://github.com/soiqualang/geojson2mbtiles

# Pull and start container

* `<your_local_data_dir>`: Your local dir that you want to save your video, mp3,..
* `<docker_data_dir>`: Data dir in docker (default is `/data`)

Ex: `docker run -it -d --name geojson2mbtiles -v D:/tmp2/t1:/data soiqualang/geojson2mbtiles:1.0`

```bash
# Pull and start container
docker run -it -d --name geojson2mbtiles -v <your_local_data_dir>:/<docker_data_dir> soiqualang/geojson2mbtiles:1.0

# Stop container
docker stop geojson2mbtiles

# Start container
docker start geojson2mbtiles

# Remove container
docker rm geojson2mbtiles
```

# Run tool

## Convert all geojson in folder

```txt
D:\sync\websvr\docker\geojson2mbtiles>docker exec -it geojson2mbtiles python3.8 json2mbtiles.py -h
usage: json2mbtiles.py [-h] -geojson_folder_path GEOJSON_FOLDER_PATH -mbtiles_folder_path MBTILES_FOLDER_PATH -maxzoom MAXZOOM

ArgumentParser by soiqualang

optional arguments:
  -h, --help            show this help message and exit
  -geojson_folder_path GEOJSON_FOLDER_PATH
                        Input parammeter
  -mbtiles_folder_path MBTILES_FOLDER_PATH
                        Input parammeter
  -maxzoom MAXZOOM      Input parammeter
```

* `maxzoom`: What you want to download
  * `g`: tool will choose a maximum zoom level that should be high enough to reflect the precision of the original data. (If it turns out still not to be as detailed as you want, use -z manually with a higher number.)
  * `18`: Example is `18`, you can pick a zoom level (`number`) you want
* `geojson_folder_path`: Path to your local geojson folder
* `mbtiles_folder_path`: Path to your local mbtile folder

```bash
# Help
docker exec -it geojson2mbtiles python3.8 json2mbtiles.py -h

# Convert all geojson in folder
docker exec -it geojson2mbtiles python3.8 json2mbtiles.py -geojson_folder_path "/data/geojson2mbtiles/geojson/" -mbtiles_folder_path "/data/geojson2mbtiles/mbtiles/" -maxzoom g

```

## Convert a file

https://github.com/mapbox/tippecanoe

```bash
# Convert a file
docker exec -it geojson2mbtiles tippecanoe -zg -f -o "/data/geojson2mbtiles/mbtiles/t_1vn_hientrang_sdd2015.mbtiles" --drop-densest-as-needed "/data/geojson2mbtiles/geojson/1vn_hientrang_sdd2015.geojson"
```