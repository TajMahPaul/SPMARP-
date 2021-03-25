from db.data import Data
import pandas as pd
import os
import numpy as np
import googlemaps
import random

map = {
    '12AM': 0,
    '1AM': 1,
    '2AM': 2,
    '3AM': 3,
    '4AM': 4,
    '5AM': 5,
    '6AM': 6,
    '7AM': 7,
    '8AM': 8,
    '9AM': 9,
    '10AM': 10,
    '11AM': 11,
    '12PM': 12,
    '1PM': 13,
    '2PM': 14,
    '3PM': 15,
    '4PM': 16,
    '5PM': 17,
    '6PM': 18,
    '7PM': 19,
    '8PM': 20,
    '9PM': 21,
    '10PM': 22,
    '11PM': 23
}

key = "AIzaSyBYdFvLeDTTUdif62AJ4hXuTcMI7_hGrx0"
gmaps = googlemaps.Client(key=key)

results = {}

# set data class as global
data = Data()

def get_events(crime_stats, n):
    events = []
    
    crime_stats['total'] = crime_stats.sum(axis=1)
    crime_stats = crime_stats.drop(crime_stats.columns.difference(['Time','total']), axis=1)
    crime_stats['prob'] = crime_stats['total'] / crime_stats['total'].sum() 
    crime_stats['time_24'] = crime_stats['Time'].apply( lambda x:  map[x])
    crime_stats = crime_stats.sort_values(['time_24'])

    random.seed(a=50, version=2)
    for i in range(50):
        hour = random.choices(crime_stats['time_24'], crime_stats['prob'])[0]
        minute = random.randint(0, 60)
        ev = (hour,minute)
        events.append(ev)

    return events

def main():
    distance = data.get_distances()
    crime = data.get_crime()
    crime = crime[crime['month']==3]
    crime = crime.reindex()
    
    crime_stats = pd.read_csv('qa03402_2016 _edited.csv')
    events = get_events(crime_stats, 50)
    
    for range(0,24):
        for range(0,60):

if __name__ == "__main__":
    main()