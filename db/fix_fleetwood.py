import pandas as pd
import sqlite3
from pathlib import Path
import os 

def fix(row):
    if (row['distances'] < 60):
        return row['distances'] * 1000
    else:
        return row['distances']
def main():
    distance_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'filter_data', 'distance_fleetwood.csv'))
    distance_df['distances'] = distance_df.apply(fix, axis=1)
    distance_df.to_csv(os.path.join(os.path.dirname(__file__), 'filter_data', 'distance_fleetwood.csv'), index=False)

if __name__ == "__main__":
    main()