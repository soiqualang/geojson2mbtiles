# -*- coding: utf-8 -*-

import os
from pathlib import Path
import subprocess
import argparse

def getFname(path):
    #/content/drive/Shared drives/soiqualang.chentreu/goolge_colab/json2mbtiles/geojson/dl_vhlichsu_1.geojson
    if('/' in path):
        arr1=path.split('/')
    else:
        arr1=path.split('\\')
    #return arr1[len(arr1)-1].replace("geojson", "mbtiles")
    return [arr1[len(arr1)-1], arr1[len(arr1)-1].replace("geojson", "mbtiles")]

def arg_parsing_v2(params):
    parser = argparse.ArgumentParser(description='ArgumentParser by soiqualang')
    for param in params:
        param='-'+str(param)
        parser.add_argument(param, required=True,
                            help='Input parammeter')
    args = parser.parse_args()
    args = vars(args)
    return args

# Main
params=['geojson_folder_path','mbtiles_folder_path','maxzoom']
ARGS = arg_parsing_v2(params)

foin = Path(ARGS['geojson_folder_path'])
foout = ARGS['mbtiles_folder_path']
maxzoom = ARGS['maxzoom']
# -zg: chương trình tự chọn để tối ưu
# -z18: Đến mức zoom 18

# print(foin)
# print(foout)

# foin=Path('/content/drive/Shared drives/soiqualang.chentreu/goolge_colab/json2mbtiles/geojson/')
# foout='/content/drive/Shared drives/soiqualang.chentreu/goolge_colab/json2mbtiles/mbtiles/'

for fjson in foin.glob('*.geojson'):
    # cmd='tippecanoe -zg -f -o "t_%s" --drop-densest-as-needed "%s"' % (getFname(str(fjson))[1],getFname(str(fjson))[0])
    cmd='tippecanoe -z%s -f -o "%st_%s" --drop-densest-as-needed "%s"' % (maxzoom,foout,getFname(str(fjson))[1],fjson)
    # print(cmd)
    print('Start processing %s file' % (getFname(str(fjson))[0]))
    process = subprocess.Popen(cmd,shell=True)
    process.wait()
    print('Done!')