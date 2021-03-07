import sqlite3
import pandas as pd
import os 

class Data:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))

    def get_demand(self):
        return pd.read_sql('select * from demand_points', con=self.connection)

    def get_waiting(self):
        return pd.read_sql('select * from waiting_points', con=self.connection)

    def get_crime(self):
        return pd.read_sql('select * from crime_points', con=self.connection)    

    def get_distances(self):
        return pd.read_sql('select * from distances', con=self.connection)    