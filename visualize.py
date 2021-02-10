from db.data import Data
import pandas as pd

# set data class as global
data = Data()

def main():
    demand_points = data.get_demand()
    print(demand_points)

if __name__ == "__main__":
    main()