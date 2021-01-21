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
params=['geojson_folder_path','mbtiles_folder_path']
ARGS = arg_parsing_v2(params)

foin=Path('/content/drive/Shared drives/soiqualang.chentreu/goolge_colab/json2mbtiles/geojson/')
foout='/content/drive/Shared drives/soiqualang.chentreu/goolge_colab/json2mbtiles/mbtiles/'
for fjson in foin.glob('*.geojson'):
    cmd='tippecanoe -zg -o "'+foout+'t_'+getFname(str(fjson))+'" --drop-densest-as-needed "'+str(fjson)+'"'
    #print(cmd)
    subprocess.Popen(cmd,shell=True)