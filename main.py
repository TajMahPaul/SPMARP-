# main file that will run the algorithm
from db.data import Data
import gurobipy as gp
from gurobipy import GRB
# def structure_data():

# 1.5 km / 1500m
RADIUS = 1500

def main ():
    
    data = Data()

    demand = data.get_demand()
    waiting = data.get_waiting()
    distances = data.get_distances()
    crime = data.get_crime()

    distances = distances[distances['distance'] <= RADIUS]



if __name__ == "__main__":
    main()