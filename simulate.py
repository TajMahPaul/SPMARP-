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

model_alpha_1 = {
    1: ['King George Skytrain'],
    2: ['King George Skytrain', 'Surrey RCMP District #3 Newton'],
    3: ['APH Matthew Park', 'Surrey RCMP District #3 Newton', 'Lionel Park'],
    4: ['APH Matthew Park', 'Surrey RCMP District #3 Newton', 'Lionel Park', 'South Surrey RCMP'],
    5: ['APH Matthew Park', 'Surrey RCMP District #3 Newton', 'Lionel Park', 'Hillcrest Park', 'South Surrey RCMP'],
    6: ['APH Matthew Park','Chimney Heights Park', 'Unwin Park', 'Lionel Park', 'Hillcrest Park', 'South Surrey RCMP'],
    7: ['Chimney Heights Park', 'Unwin Park', 'Royal Canadian Mounted Police Guildford', 'Bonnie Schrenk Park', 'Hillcrest Park', 'South Surrey RCMP','David Brankin Elementary School/William Beagle Park'],
    8: ['David Brankin Elementary School/William Beagle Park', 'Chimney Heights Park', 'Unwin Park', 'Royal Canadian Mounted Police Guildford', 'Bonnie Schrenk Park', 'Hillcrest Park', 'Dogwood Park', 'The Shops at Morgan Crossing Outlet'],
    9: ['Plaza at 88 and scott road', 'King George Skytrain', 'Chimney Heights Park', 'Unwin Park', 'Fraser Heights Park', 'Fleetwood Park', 'Hillcrest Park', 'Dogwood Park', 'The Shops at Morgan Crossing Outlet']
}

key = "AIzaSyBYdFvLeDTTUdif62AJ4hXuTcMI7_hGrx0"
gmaps = googlemaps.Client(key=key)

model = {}

# set data class as global
data = Data()

def get_crime_overage(patrol):


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
    crime = crime.sample(frac=1).reset_index(drop=True)
    crime = crime.reset_index(drop=True)
    crime = crime[crime.index < 50]

    crime_stats = pd.read_csv('qa03402_2016 _edited.csv')

    events = get_events(crime_stats, 50)
    n = 9
    crime['time'] = events

    response_time = []
    coverage_area = []
    coverage_pop = []
    coverage_crime = []

    for h in range(0,24):
        for m in range(0,60):
            current_events = crime[crime['time'] == (h,m)]



if __name__ == "__main__":
    main()