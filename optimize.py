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
RADIUS = 3000
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


def relocation_model(distances, waiting, pop_dict, crime_dict, coverage, MAX_OFFICERS, lamb):

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

    
    obj1 = gp.quicksum(prob[k]*population[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))
    obj2 = gp.quicksum(prob[k]*crime_index[r]*is_covered[r,k] for r in regions for k in range(1,MAX_OFFICERS+1))

    m.setObjective(lamb*(obj1) + (1-lamb)*obj2, GRB.MAXIMIZE)
    m.optimize()

    return m, build

def get_covered_matrix():
    return
 
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
    n_range = range(5,20, 5)
    lambda_range = [.05, .10, .15, .20, .25, .30, .35, .40, .45, .50, .55, .60, .65, .70, .75, .80, .85, .90, .95]
    x = []
    y = []
    for l in lambda_range:

        WPnames = []
        m, build = relocation_model(distances_pivot, waiting, pop_dict, crime_dict, coverage, 15, l)
        for points in build.keys():
            if (abs(build[points].x) > 1e-6):
                if points[1] == 15:
                    WPnames.append(points[0])
        covered_da = distances[distances['WPname'].isin(WPnames)]
        covered_da = covered_da[covered_da['in_range'] == 1 ]['DAuid'].unique()
        crime_perc = crime[crime['DAuid'].isin(covered_da)]['incidents'].sum()
        pop_perc = demand[demand['DAuid'].isin(covered_da)]['population_val'].sum()
        x.append(crime_perc)
        y.append(pop_perc)
        plt.annotate("{l}".format(l=l), (crime_perc, pop_perc))

    plt.plot(x, y, 'o')

    plt.xlabel("Crime")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()