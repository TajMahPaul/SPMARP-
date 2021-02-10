from db.data import Data
import pandas as pd
import os

# set data class as global
data = Data()
import matplotlib.pyplot as plt
import numpy as np

def main():
    # demand_points = data.get_demand()
    # surrey_map = gpd.read_file(os.path.join(os.path.dirname(__file__),'maps','surrey_city_boundary.json'), encoding = 'unicode_escape')
    # surrey_map.plot()
    # plt.show()
    x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
    plt.plot(x, np.sin(x))       # Plot the sine of each x point
    plt.show()     
    
if __name__ == "__main__":
    main()