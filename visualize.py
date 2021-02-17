from db.data import Data
import pandas as pd
import os
import numpy as np

# set data class as global
data = Data()



def main():
    waiting = data.get_waiting()
    print(waiting)
   
    
if __name__ == "__main__":
    main()