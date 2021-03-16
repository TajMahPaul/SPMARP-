# main file that will run the algorithm
from db.data import Data
import matplotlib.pyplot as plt
import mplleaflet
import numpy as np

# define constants
RADIUS = 1000

def main ():
    
    data = Data()
    
    demand = data.get_demand()
    waiting = data.get_waiting()
    distances = data.get_distances()
    crime = data.get_crime()

    # plt.plot(demand['lon'], demand['lat'], 'rs')
    # plt.plot(waiting['lon'].astype(np.float64), waiting['lat'].astype(np.float64), 'bs')
    # mplleaflet.show()

    distances['in_range'] = (distances['distance'] <= RADIUS).astype(int)
    distances = distances[ distances['WPname'] != 'Holland Park']
    distances = distances[ distances['in_range'] == 1]
    unique_wp = distances['WPname'].unique()
    unique_wp = [unique_wp[6]]
    unique_dp = distances [ distances['WPname'] == unique_wp[0] ]['DAuid']

    demand = demand[demand['DAuid'].isin(unique_dp)]
    waiting = waiting[waiting['name'].isin(unique_wp)]
    plt.plot(demand['lon'], demand['lat'], 'rs')
    plt.plot(waiting['lon'].astype(np.float64), waiting['lat'].astype(np.float64), 'bs')
    mplleaflet.show()

if __name__ == "__main__":
    main()