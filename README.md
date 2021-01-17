# geojson2mbtiles
Tool to convert GeoJson to Mbtiles

> Test với Google Colab

https://colab.research.google.com/drive/1TLIMNu9T2ZFUDy4hsB-S4ZsoXXKACgS1#scrollTo=MVrN7rSMFxuo

> Build docker

```bash
docker build -t geojson2mbtiles:1.0 .
```

> Run Docker

```bash
docker run -it -d --name geojson2mbtiles -v E:/tmp:/data geojson2mbtiles:1.0
```

> test

```bash
docker exec -it geojson2mbtiles /bin/sh
```