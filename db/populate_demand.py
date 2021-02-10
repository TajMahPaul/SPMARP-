import pandas as pd
import sqlite3
from pathlib import Path
import os 

def add_FE_names(row):
    FE_NAMEs = {
        32:'Surrey-Centre/Whalley',
        12:'Fleetwood/Port Kells',
        7: 'Cloverdale',
        30: 'White Rock/South Surrey',
        33: 'Surrey Newton'
    }
    return FE_NAMEs[row['FEDcode']]

def get_surrey(df):
    df = df[df['PRuid'] == 59 ]
    df = df[df['CDcode'] == 15]
    df = df[df['CCScode'] == 4]
    return df

def insert_records(df):
    sqliteConnection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))
    df.to_sql('demand_points', con=sqliteConnection, if_exists='replace', index=False)



def main():
    df_DA = pd.read_csv(os.path.join(os.path.dirname(__file__), 'raw_data', 'DA.csv'))
    df_DB = pd.read_csv(os.path.join(os.path.dirname(__file__), 'raw_data', 'DB.csv'))

    surrey_DA = get_surrey(df_DA)
    surrey_DB = get_surrey(df_DB)

    surrey_DB = surrey_DB[['DAcode', 'FEDcode']].drop_duplicates(subset=['DAcode'])
    surrey_df = pd.merge(surrey_DA, surrey_DB[['DAcode','FEDcode']],on='DAcode', how='left')
    surrey_df['FEDName'] = surrey_df.apply(add_FE_names, axis=1)
    surrey_df = surrey_df[['DAuid', 'DApop_2016', 'DAarea', 'DArplat', 'DArplong', 'FEDcode', 'FEDName']]
    surrey_df = surrey_df.rename(columns={"DApop_2016": "population_val", "DArplat": "lat", "DArplong": "lon"})
    insert_records(surrey_df)
    

if __name__ == "__main__":
    main()