#  this file will be to populate distances using google maps api
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
import os
import googlemaps
from data import Data
from math import cos, sin, asin, sqrt, pi, atan2, radians

key = "AIzaSyBYdFvLeDTTUdif62AJ4hXuTcMI7_hGrx0"
gmaps = googlemaps.Client(key=key)

def hav_distance(row):
        #Taken from https://stackoverflow.com/a/4913653
        """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [float(row['lon_demand']), float(row['lat_demand']), float(row['lon_waiting']), float(row['lat_waiting'])])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in km
        return c * r

def cal_distances(row):
    hav = row['hav']
    if (hav < 10):
        waiting = (float(row['lat_demand']), float(row['lon_demand']))
        demand = (float(row['lat_waiting']), float(row['lon_waiting']))
        matrix = gmaps.distance_matrix(waiting, demand, mode="driving")

        try:
            return matrix['rows'][0]['elements'][0]['distance']['value']

        except Exception as e:
            return np.nan
    else:
        return hav*1000

def main():
    data = Data()
    df_demand = data.get_demand()
    df_waiting = data.get_waiting()
    df_waiting = df_waiting[df_waiting['FEDcode'] == '33']

    distances = df_demand.merge(df_waiting, how="cross")
    distances = distances.drop(columns=['population_val', 'DAarea', 'FEDcode_y', 'FEDcode_x', 'FEDName', 'FEDname'])
    distances = distances.rename(columns={"lat_x": "lat_demand", "lon_x": "lon_demand", "lat_y": "lat_waiting", "lon_y": "lon_waiting", "name": "WPname"})
    
    distances['hav'] = distances.apply(hav_distance, axis=1)

    distances['distances'] = distances.apply(cal_distances, axis=1)
    distances = distances.drop(columns=['lat_demand', 'lon_demand', 'lat_waiting', 'lon_waiting'])
    distances.to_csv(os.path.join(os.path.dirname(__file__), 'filter_data', 'distance_newton.csv'), index=False)


if __name__ == "__main__":
    main()