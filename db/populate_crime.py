#  this file will be to populate distances using google maps api
import pandas as pd
import sqlite3
from pathlib import Path
import os
import googlemaps
import networkx as nx

key = "AIzaSyApefMuRG57ImJYcHR0gDFzGXecDBL-iDw"
gmaps = googlemaps.Client(key=key)
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

def main():

    # df_crime = pd.read_csv(os.path.join(os.path.dirname(__file__), 'raw_data', 'crime2019.csv'))
    # one_crime = df_crime.loc[0]
    # # geocode_result = gmaps.geocode(one_crime['HUNDRED_BLOCK'] + ', Surrey, BC')
    # print(geocode_result)
    G = nx.read_gml(os.path.join(os.path.dirname(__file__), 'raw_data', 'gfed000a11g_e.gml'))
    print(G.node)


if __name__ == "__main__":
    main()