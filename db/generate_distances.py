#  this file will be to populate distances using google maps api
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
import os
import googlemaps
from data import Data

key = "AIzaSyApefMuRG57ImJYcHR0gDFzGXecDBL-iDw"
gmaps = googlemaps.Client(key=key)

def cal_distances(row):
    waiting = (float(row['lat_demand']), float(row['lon_demand']))
    demand = (float(row['lat_waiting']), float(row['lon_waiting']))
    matrix = gmaps.distance_matrix(waiting, demand, mode="driving")

    try:
        return matrix['rows'][0]['elements'][0]['distance']['value']

    except Exception as e:
        return np.nan

def main():
    data = Data()
    df_demand = data.get_demand()
    df_waiting = data.get_waiting()

    distances = df_demand.merge(df_waiting, how="cross")
    distances = distances.drop(columns=['population_val', 'DAarea', 'FEDcode_y', 'FEDcode_x', 'FEDName', 'FEDname'])
    distances = distances.rename(columns={"lat_x": "lat_demand", "lon_x": "lon_demand", "lat_y": "lat_waiting", "lon_y": "lon_waiting", "name": "WPname"})

    distances['distance'] = distances.apply(cal_distances, axis=1)
    distances = distances.drop(columns=['lat_demand', 'lon_demand', 'lat_waiting', 'lon_waiting'])
    distances.to_csv(os.path.join(os.path.dirname(__file__), 'filter_data', 'distance_whalley.csv'), index=False)


if __name__ == "__main__":
    main()