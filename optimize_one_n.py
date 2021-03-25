from db.data import Data
import gurobipy as gp
from gurobipy import GRB
from scipy.special import comb

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplleaflet

# set data class as global
data = Data()

# define constants
RADIUS = 4200
ALPHA = 1
LAMBDA = 1.35
SERVICE_TIME = 1

incident_weight = {'Break and Enter - Business':3,
 'Break and Enter - Residence':5,
 'Fatal/Injury Collision':5,
 'Graffiti':2,
 'Shoplifting':1,
 'Theft from Motor Vehicle':4,
 'Theft of Motor Vehicle':4}

def relocation_model_con_pop(distances, waiting, pop_dict, crime_dict, coverage, MAX_OFFICERS, lamb):

    regions, population = gp.multidict(pop_dict)
    regions, crime_index = gp.multidict(crime_dict)

    total_pop = population
    total_crime = crime_index
    waits, covered = gp.multidict(coverage)
    prob = [comb(MAX_OFFICERS,k)*((0.6)**k)*((0.4)**(MAX_OFFICERS-k)) for k in range(0,MAX_OFFICERS+1)]

    m = gp.Model("SPMARP")
    m.Params.LogToConsole = 0 #dont print model information
    wait_size = [(name,size) for name in list(waiting['name']) for size in range(0,MAX_OFFICERS+1)]
    demand_size = [(DAuid,size) for DAuid in list(distances.columns) for size in range(0,MAX_OFFICERS+1)]

    build = m.addVars(wait_size, vtype=GRB.BINARY, name="wait_points")
    is_covered = m.addVars(demand_size, vtype=GRB.BINARY, name="Is_covered")
    build_change = m.addVars(wait_size, vtype=GRB.BINARY, name="wait_change")

    #sum demand points only where officers can reach
    for size in range(0,MAX_OFFICERS+1):
        m.addConstrs((gp.quicksum(build[wait,size] for wait in waits if r in covered[wait]) >= is_covered[r,size] for r in regions), name="Build2cover")

    #only allow max officers
    for size in range(0,MAX_OFFICERS+1):
        m.addConstr(gp.quicksum(build[wait,size] for wait in waits) == size, name="officers")   

    #Control waiting site change
    for size in range(1,MAX_OFFICERS):
        m.addConstrs( (build[wait,size] - build[wait,size+1] <= build_change[wait,size] for wait in waits), name="cease_wait")

    #Max amount of location changes
    for size in range(1,MAX_OFFICERS):
        m.addConstrs( (build_change[wait,size] <= ALPHA for wait in waits), name="cease_wait")

    m.addConstr(gp.quicksum(population[r]*is_covered[r,15]for r in regions) >= lamb, name="crime")

    obj = gp.quicksum(crime_index[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))

    try:
        m.setObjective(obj, GRB.MAXIMIZE)
        m.optimize()
        return m, build
    except Exception as e:
        print(str(e))
        return None, None

    # obj1 = gp.quicksum(population[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))
    # obj2 = gp.quicksum(crime_index[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))

    # m.setObjective(lamb*(obj1) + (1-lamb)*obj2, GRB.MAXIMIZE)
    # m.optimize()


def relocation_model_con_crime(distances, waiting, pop_dict, crime_dict, coverage, MAX_OFFICERS, lamb):

    regions, population = gp.multidict(pop_dict)
    regions, crime_index = gp.multidict(crime_dict)

    total_pop = population
    total_crime = crime_index
    waits, covered = gp.multidict(coverage)
    prob = [comb(MAX_OFFICERS,k)*((0.6)**k)*((0.4)**(MAX_OFFICERS-k)) for k in range(0,MAX_OFFICERS+1)]

    m = gp.Model("SPMARP")
    m.Params.LogToConsole = 0 #dont print model information
    wait_size = [(name,size) for name in list(waiting['name']) for size in range(0,MAX_OFFICERS+1)]
    demand_size = [(DAuid,size) for DAuid in list(distances.columns) for size in range(0,MAX_OFFICERS+1)]

    build = m.addVars(wait_size, vtype=GRB.BINARY, name="wait_points")
    is_covered = m.addVars(demand_size, vtype=GRB.BINARY, name="Is_covered")
    build_change = m.addVars(wait_size, vtype=GRB.BINARY, name="wait_change")

    #sum demand points only where officers can reach
    for size in range(0,MAX_OFFICERS+1):
        m.addConstrs((gp.quicksum(build[wait,size] for wait in waits if r in covered[wait]) >= is_covered[r,size] for r in regions), name="Build2cover")

    #only allow max officers
    for size in range(0,MAX_OFFICERS+1):
        m.addConstr(gp.quicksum(build[wait,size] for wait in waits) == size, name="officers")   

    #Control waiting site change
    for size in range(1,MAX_OFFICERS):
        m.addConstrs( (build[wait,size] - build[wait,size+1] <= build_change[wait,size] for wait in waits), name="cease_wait")

    #Max amount of location changes
    for size in range(1,MAX_OFFICERS):
        m.addConstrs( (build_change[wait,size] <= ALPHA for wait in waits), name="cease_wait")

    m.addConstr(gp.quicksum(crime_index[r]*is_covered[r,15]for r in regions) >= lamb, name="crime")

    obj = gp.quicksum(population[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))

    try:
        m.setObjective(obj, GRB.MAXIMIZE)
        m.optimize()
        return m, build
    except Exception as e:
        print(str(e))
        return None, None
    # obj1 = gp.quicksum(population[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))
    # obj2 = gp.quicksum(crime_index[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))

    # m.setObjective(lamb*(obj1) + (1-lamb)*obj2, GRB.MAXIMIZE)
    # m.optimize()

    return m, build

def main():

    # get values from db
    demand = data.get_demand()
    waiting = data.get_waiting()
    distances = data.get_distances()

    # Structure distances
    distances['in_range'] = (distances['distance'] <= RADIUS).astype(int)
    distances = distances[ distances['WPname'] != 'Holland Park']

    # get filter disemination areas
    disemination_areas = list(distances['DAuid'].unique())

    # only care about filtered demand points from distances
    demand = demand[demand['DAuid'].isin(disemination_areas)]
    total_pop = demand['population_val'].sum()
    demand['population_val'] = demand['population_val'] / total_pop

    # calculate coverage matrix
    distances_pivot = distances.pivot(index='WPname',columns='DAuid',values='in_range')
    coverage = {}
    for index, row in distances_pivot.iterrows():
        coverage[index] = [set(row[row==1].keys())]
    
    pop_dict = pd.Series(demand.population_val.values,index=(demand.DAuid)).to_dict()
    
    # integrate crime data
    crime = data.get_crime()
    crime['weight'] = crime['type'].replace(incident_weight)
    crime = crime[crime['distance'] < 200] #removing errors
    crime = demand.set_index('DAuid').join(crime['closest_demand'].value_counts()).reset_index().rename(columns={'closest_demand':'incidents'})
    crime['incidents'] = crime['incidents'].replace(np.nan, 0)

    total_crime = crime['incidents'].sum()
    crime['incidents'] = crime['incidents'] / total_crime

    crime_dict = pd.Series(crime.incidents.values,index=(crime.DAuid)).to_dict()

    results = {}
    
    x = []
    y = []
        
    WPnames = []
    l = 0.9185
    m, build = relocation_model_con_pop(distances_pivot, waiting, pop_dict, crime_dict, coverage, 15, l)
    for points in build.keys():

        try: 
            test = abs(build[points].x)
        except Exception as e:
            print (str(e))
            print(l)
            break

        if (abs(build[points].x) > 1e-6):
            if points[1] == 9:
                WPnames.append(points[0])
            

    output_wp = waiting[waiting['name'].isin(WPnames)]
    plt.plot(output_wp['lon'].astype(np.float64), output_wp['lat'].astype(np.float64), 'bs')
     
    mplleaflet.show()


if __name__ == "__main__":
    main()