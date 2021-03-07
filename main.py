# main file that will run the algorithm
from db.data import Data
import matplotlib.pyplot as plt
import mplleaflet

def main ():
    
    data = Data()
    
    demand = data.get_demand()
    waiting = data.get_waiting()
    distances = data.get_distances()
    crime = data.get_crime()
    
    plt.plot(demand['lon'], demand['lat'], 'rs')
    mplleaflet.show()

if __name__ == "__main__":
    main()