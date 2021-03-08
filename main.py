# main file that will run the algorithm
from db.data import Data
import matplotlib.pyplot as plt
import mplleaflet
import numpy as np

def main ():
    
    data = Data()
    
    demand = data.get_demand()
    waiting = data.get_waiting()
    distances = data.get_distances()
    crime = data.get_crime()
    
    print(waiting)
    print(demand)
    print(demand.dtypes)
    print(waiting.dtypes)

    plt.plot(demand['lon'], demand['lat'], 'rs')
    plt.plot(waiting['lon'].astype(np.float64), waiting['lat'].astype(np.float64), 'bs')
    mplleaflet.show()

if __name__ == "__main__":
    main()