import pandas as pd
import sqlite3
from pathlib import Path
import os 

waiting_points = pd.DataFrame(np.array([["Bear Creek Park", 32, "Surrey-Centre/Whalley", 49.161383456039424, -122.84075812112808],
                                        ["Walmart Supercenter (88ave)", 32, "Surrey-Centre/Whalley", 49.164798886139444, -122.87728979723549],
                                        ["Devon Gardens Elementary", 32, "Surrey-Centre/Whalley", 49.164811236711394, -122.91464087440681],
                                        ["Big plaza at 88 and scott road", 32, "Surrey-Centre/Whalley", 49.16316787821308, -122.89116665706219],
                                        ["Devon Gardens Park", 32, "Surrey-Centre/Whalley", 49.16510371711971, -122.92433373769487],
                                        ["Annieville Lions Park", 32, "Surrey-Centre/Whalley", 49.16921497340804, -122.91122776486202],
                                        ["Delview Secondary School", 32, "Surrey-Centre/Whalley", 49.16904757390888, -122.90256871805357],
                                        ["Kennedy Park", 32, "Surrey-Centre/Whalley", 49.16834352390594, -122.88958231071858],
                                        ["Royal Heights Park", 32, "Surrey-Centre/Whalley", 49.18058245443267, -122.90497575218133],
                                        ["Royal Heights Elementary School", 32, 49.17932812230354, -122.89809230677821],
                                        ["Jagga Sweets", 32, "Surrey-Centre/Whalley", 49.17200628921393, -122.89055923197498],
                                        ["Robertson Drive Park", 32, "Surrey-Centre/Whalley", 49.168687539819665, -122.87039799586984],
                                        ["LA Matheson Secondary School", 32, "Surrey-Centre/Whalley", 49.17540473873445, -122.88402203419959],
                                        ["Scott Road Substation", 32, "Surrey-Centre/Whalley", 49.18294117484918, -122.88920937886512],
                                        ["Burger King scott rd", 32, "Surrey-Centre/Whalley", 49.19116624259907, -122.89093078859793],
                                        ["Tannery Park", 32, "Surrey-Centre/Whalley", 49.19818394113428, -122.90021828112194],
                                        ["Save on Foods Scott rd", 32, "Surrey-Centre/Whalley", 49.19385454169428, -122.88961145238706],
                                        ["Brownville Pub", 32, "Surrey-Centre/Whalley", 49.20328808608704, -122.89136852995762],
                                        ["Aria Banquet Convention Center", 32, "Surrey-Centre/Whalley", 49.202926587238494, -122.88020950870624],
                                        ["The Hive Climbing and Fitness", 32, "Surrey-Centre/Whalley", 49.2052106937602, -122.88182629111486],
                                        ["A1 Metal Recycling", 32, "Surrey-Centre/Whalley", 49.208424456895706, -122.8833161124976],
                                        ["Deep Tire Service", 32, "Surrey-Centre/Whalley", 49.21202049358631, -122.87915149610126],
                                        ["Bridgeview Park", 32, "Surrey-Centre/Whalley", 49.21096169398329, -122.87214764068614],
                                        ["Central City Brewers and Distillers", 32, "Surrey-Centre/Whalley", 49.209900785153636, -122.8635651777272],
                                        ["Tim Hortons", 32, "Surrey-Centre/Whalley", 49.21193256285162, -122.86253599096582],
                                        ["Groundworks Construction Supply", 32, "Surrey-Centre/Whalley", 49.213681063974306, -122.86990324554002],
                                        ["Global Agriculture Trans-loading Inc", 32, "Surrey-Centre/Whalley", 49.21522633267858, -122.86182441841775],
                                        ["Bolivar Park", 32, "Surrey-Centre/Whalley", 49.21087717824431, -122.85068319796093],
                                        ["Scott Road Skytrain", 32, "Surrey-Centre/Whalley", 49.204124140244105, -122.87376903812165],
                                        ["Home Depot 128th", 32, "Surrey-Centre/Whalley", 49.2039143137177, -122.86847116171421],
                                        ["A&W Canada 128th", 32, "Surrey-Centre/Whalley", 49.205845640544304, -122.86674266501687],
                                        ["Bridgeview Elementary", 32, "Surrey-Centre/Whalley", 49.21126028509715, -122.86506244855633],
                                        ["Bolivar Park Parking lott", 32, "Surrey-Centre/Whalley", 49.21075763701341, -122.85043870354724],
                                        ["olivar Park Upper playground", 32, "Surrey-Centre/Whalley", 49.20984607999906, -122.84296312768431],
                                        ["James Ardiel Elementary", 32, "Surrey-Centre/Whalley", 49.20655826401143, -122.8413940228007],
                                        ["Husky hensen rd Grosvenor rd", 32, "Surrey-Centre/Whalley", 49.203628639497275, -122.83692353071045],
                                        ["Forsyth Park", 32, "Surrey-Centre/Whalley", 49.19594448531151, -122.83661786281426],
                                        ["Our Lady of Good counsel School", 32, "Surrey-Centre/Whalley", 49.19311467051692, -122.83560463845909],
                                        ["Chartwell Imperial Place Retirement Residence", 32, "Surrey-Centre/Whalley", 49.18864967394737, -122.83797334126137],
                                        ["Lyonridge Christmas Lights Christmas store", 32, "Surrey-Centre/Whalley", 49.18397079512638, -122.8349028928958],
                                        ["Petro-canada 140th", 32, "Surrey-Centre/Whalley", 49.17960114530056, -122.83501001538316],
                                        ["Surrey memorial parking", 32, "Surrey-Centre/Whalley", 49.178221569194086, -122.84438980347035],
                                        ["LifeLabs Medical Laboratory Services", 32, "Surrey-Centre/Whalley", 49.177750077282546, -122.84283623230127],
                                        ["Simon Cunningham Elementary School", 32, "Surrey-Centre/Whalley", 49.172677101073695, -122.83388427650662],
                                        ["School District No 36", 32, "Surrey-Centre/Whalley", 49.170380098636684, -122.83347337074065],
                                        ["Kiyo Park", 32, "Surrey-Centre/Whalley", 49.16753570564422, -122.83395397557732],
                                        ["Creekside elementary", 32, "Surrey-Centre/Whalley", 49.16763899898092, -122.83913709496753],
                                        ["Bear Creek Park", 32, "Surrey-Centre/Whalley", 49.16148066643378, -122.84073615759783],
                                        ["Surrey Fire Service Hall 1", 32, "Surrey-Centre/Whalley", 49.16233025951351, -122.85737317992898],
                                        ["Queen Mary Park", 32, "Surrey-Centre/Whalley", 49.16520961674437, -122.86079087826407],
                                        ["Robertson Drive Park", 32, "Surrey-Centre/Whalley", 49.16879177260187, -122.87012382356606],
                                        ["David Brankin Elementary School/William Beagle Park", 32, "Surrey-Centre/Whalley", 49.169459404399525, -122.86597859752978],
                                        ["Moffat Park", 32, "Surrey-Centre/Whalley", 49.1742354436414, -122.88278236604714],
                                        ["Betty Huff Elementary", 32, "Surrey-Centre/Whalley", 49.17323580234572, -122.86007521805942],
                                        ["Chicken World", 32, "Surrey-Centre/Whalley", 49.176675812363285, -122.86690986329299],
                                        ["Chevron", 32, "Surrey-Centre/Whalley", 49.1774872307507, -122.86848116828992],
                                        ["Cedar Hills Animal Hospital", 32, "Surrey-Centre/Whalley", 49.17757861966512, -122.86503863469748],
                                        ["Mathew Park", 32, "Surrey-Centre/Whalley", 49.180436974139056, -122.85545350081746],
                                        ["Holland Park", 32, "Surrey-Centre/Whalley", 49.18375344119001, -122.84769112915504],
                                        ["Central City Shopping mall", 32, "Surrey-Centre/Whalley", 49.186230019191825, -122.84695573365077],
                                        ["City of Surrey Lot #817", 32, "Surrey-Centre/Whalley", 49.18841317161566, -122.84871051482729],
                                        ["Kwantlen Park Secondary School", 32, "Surrey-Centre/Whalley", 49.1924137553657, -122.85790647745792],
                                        ["Kwantlen Park", 32, "Surrey-Centre/Whalley", 49.19231778262659, -122.86341770459984],
                                        ["King George Skytrain", 32, "Surrey-Centre/Whalley", 49.182481964458994, -122.84374366480155],
                                        ["Surrey Central", 32, "Surrey-Centre/Whalley", 49.189535827335895, -122.8475398262315],
                                        ["Service Canada Centre", 32, "Surrey-Centre/Whalley", 49.19181659042972, -122.837826939261],
                                        ["Planet Fitness", 32, "Surrey-Centre/Whalley", 49.19602338792103, -122.84447966245351],
                                        ["Whalley Athletic Park", 32, "Surrey-Centre/Whalley", 49.196124835396034, -122.85191471420286],
                                        ["Prince Charles Elementary School", 32, "Surrey-Centre/Whalley", 49.18572444946391, -122.8773959904833],
                                        ["Brooke Elementary School", 32, "Surrey-Centre/Whalley", 49.16352308630861, -122.92566355797689],
                                        ["Queen Elizabeth Secondary School", 32, "Surrey-Centre/Whalley", 49.17371112323518, -122.84700493889056],
                                        ["APH Matthew Park", 32, "Surrey-Centre/Whalley", 49.17973374729407, -122.85377220651083]                                  

]))
# '''CREATE TABLE IF NOT EXISTS waiting_points (WPid integer PRIMARY KEY AUTOINCREMENT, name text, FEDcode integer, FEDname text, lon integer, lat integer)'''
def add_FE_names(row):
    FE_NAMEs = {
        32:'Surrey-Centre/Whalley',
        12:'Fleetwood/Port Kells',
        7: 'Cloverdale',
        30: 'White Rock/South Surrey',
        33: 'Surrey Newton'
    }
    return FE_NAMEs[row['FEDcode']]


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