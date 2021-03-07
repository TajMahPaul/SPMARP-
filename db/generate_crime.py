#  this file will be to populate distances using google maps api
import pandas as pd
import numpy as np
import sqlite3
from pathlib import Path
import os
import googlemaps

key = "AIzaSyApefMuRG57ImJYcHR0gDFzGXecDBL-iDw"
gmaps = googlemaps.Client(key=key)

def get_lon_lat(row):
    address_string = row['HUNDRED_BLOCK'] + ', Surrey, BC'
    geocode_result = gmaps.geocode(address_string)
    try:
        lon = geocode_result[0]['geometry']['location']['lng']
        lat = geocode_result[0]['geometry']['location']['lat']
    except:
        return pd.Series([np.nan,np.nan])
    return pd.Series([lon, lat])


def main():

    df_crime = pd.read_csv(os.path.join(os.path.dirname(__file__), 'raw_data', 'crime_2020.csv'), skiprows=range(1, 14011))
    df_crime[['lon', 'lat']] = df_crime.apply(get_lon_lat, axis=1)
    df_crime.to_csv(os.path.join(os.path.dirname(__file__), 'filter_data', 'crime.csv'), mode='a', index=False, header=False)


if __name__ == "__main__":
    main()