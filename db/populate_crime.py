import pandas as pd
import sqlite3
from pathlib import Path
import os 

def main():
    crime_df = pd.read_csv(os.path.join(os.path.dirname(__file__),'filter_data', 'crime_matched.csv'))
    crime_df = crime_df.drop(columns=['INCIDENT_TYPE'])
    crime_df = crime_df.rename(columns={"HUNDRED_BLOCK": "location_string", "demand_point": "closest_demand", "MONTH": "month", "YEAR": "year", "FILE_NUMBER": "file_number"})
    sqliteConnection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))
    crime_df.to_sql('crime_points', con=sqliteConnection, if_exists='replace', index=False)

if __name__ == "__main__":
    main()