import pandas as pd
import sqlite3
from pathlib import Path
import os 

def main():
    distance_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'filter_data', 'distance_whalley.csv'))
    sqliteConnection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))
    distance_df.to_sql('distances', con=sqliteConnection, if_exists='replace', index=False)

if __name__ == "__main__":
    main()