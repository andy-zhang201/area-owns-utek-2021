import json
import pathFunctions

with open("UTEK 2021/3.json","r") as f:
    station_data = f.read()
    print(station_data)

    print(pathFunctions.distance(0,0,3,4))