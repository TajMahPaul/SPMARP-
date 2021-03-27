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

# set data class as global
data = Data()

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

def calc_time(distance_km):
    return 2.52977421*distance_km+1.00638416

def calc_clostest_waiting_distance(demand_point, distances, patrol):
    distances = distances[distances['WPname'].isin(patrol)]
    distances = distances[distances['DAuid'] == demand_point]
    distances = distances[distances['distance'] == distances['distance'].min()]
    return distances

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
    distances = data.get_distances()
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

    officer_busy = []
    crime_waiting = []
    printed_n = None
    printed_p = None
    printed_c = None
    for h in range(0,24):
        for m in range(0,60):

            # check if officers become free
            if (h,m) in officer_busy:
                current_number = len(officer_busy)
                officer_busy = remove_values_from_list(officer_busy, (h,m))
                difference =  current_number - len(officer_busy)
                n = n + difference

            # check if crimes are waiting and officers are available
            if n > 0 and len(crime_waiting) > 0:
                for i in range(n):
                    if len(crime_waiting) > 0:
                        officer_busy.append((h+1, m))
                        demand_point = crime_waiting.pop()
                        distance_to_travel = calc_clostest_waiting_distance(demand_point, distances, model_alpha_1[n])
                        distance_in_km = distance_to_travel['distance'].values[0] / 1000
                        time_to_travel = calc_time(distance_in_km)
                        response_time.append(time_to_travel)
                        n = n - 1

            # now check if a crime accures at this time 
            current_crimes  = crime[crime['time'] == (h,m)]
            # there are crimes occuring and here are officers available
            if not current_crimes.empty and n > 0:
                for i in range (n):
                    if not current_crimes.empty:
                        officer_busy.append((h+1, m))
                        demand_point = current_crimes.iloc[0]['closest_demand']
                        current_crimes = current_crimes[1:]
                        current_crimes = current_crimes.reset_index(drop=True)
                        distance_to_travel = calc_clostest_waiting_distance(demand_point, distances, model_alpha_1[n])
                        distance_in_km = distance_to_travel['distance'].values[0] / 1000
                        time_to_travel = calc_time(distance_in_km)
                        response_time.append(time_to_travel)
                        n = n - 1
            
            # no officers available and crimes are being committed
            
            if not current_crimes.empty and n == 0:
                while not current_crimes.empty:
                    crime_waiting.append(current_crimes.iloc[0]['closest_demand'])
                    current_crimes = current_crimes[1:]
                    current_crimes = current_crimes.reset_index(drop=True)

            if  printed_p != len(officer_busy) or printed_c != len(crime_waiting) or printed_n != n:
                printed_p = len(officer_busy)
                printed_c = len(crime_waiting)
                printed_n = n
                print('There are now {p} officers on patrol, there are now {c} crime waiting, there are {n} officers waiting'.format(p=printed_p, c=printed_c, n=printed_n))
                if (printed_p + n != 9):
                    print('WTF\n\n\n\n\n\n\n')
    print(response_time)
if __name__ == "__main__":
    main()