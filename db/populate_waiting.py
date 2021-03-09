import numpy as np
import pandas as pd
import sqlite3
from pathlib import Path
import os 



def insert_records(df):
    sqliteConnection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))
    df.to_sql('waiting_points', con=sqliteConnection, if_exists='replace', index=False)

def main():
    waiting_points = pd.DataFrame(np.array([ ["Bear Creek Park", 32, "Surrey-Centre/Whalley", 49.161383456039424, -122.84075812112808],
                                        ["Walmart Supercenter (88ave)", 32, "Surrey-Centre/Whalley", 49.164798886139444, -122.87728979723549],
                                        ["Big plaza at 88 and scott road", 32, "Surrey-Centre/Whalley", 49.16316787821308, -122.89116665706219],
                                        ["LA Matheson Secondary School/Moffat Park", 32, "Surrey-Centre/Whalley", 49.17540473873445, -122.88402203419959],
                                        ["Tannery Park", 32, "Surrey-Centre/Whalley", 49.19818394113428, -122.90021828112194],
                                        ["Brownville Pub", 32, "Surrey-Centre/Whalley", 49.20328808608704, -122.89136852995762],
                                        ["Aria Banquet Convention Center", 32, "Surrey-Centre/Whalley", 49.202926587238494, -122.88020950870624],
                                        ["Bridgeview Park", 32, "Surrey-Centre/Whalley", 49.21096169398329, -122.87214764068614],
                                        ["Bolivar Park", 32, "Surrey-Centre/Whalley", 49.21087717824431, -122.85068319796093],
                                        ["Scott Road Skytrain", 32, "Surrey-Centre/Whalley", 49.204124140244105, -122.87376903812165],
                                        ["Surrey memorial parking", 32, "Surrey-Centre/Whalley", 49.178221569194086, -122.84438980347035],
                                        ["David Brankin Elementary School/William Beagle Park", 32, "Surrey-Centre/Whalley", 49.169459404399525, -122.86597859752978],
                                        ["Cedar Hills Shopping Center", 32, "Surrey-Centre/Whalley", 49.176728942266095, -122.86734027340427],
                                        ["Holland Park", 32, "Surrey-Centre/Whalley", 49.18375344119001, -122.84769112915504],
                                        ["Central City Shopping mall", 32, "Surrey-Centre/Whalley", 49.186230019191825, -122.84695573365077],
                                        ["Kwantlen Park", 32, "Surrey-Centre/Whalley", 49.19231778262659, -122.86341770459984],
                                        ["King George Skytrain", 32, "Surrey-Centre/Whalley", 49.182481964458994, -122.84374366480155],
                                        ["Surrey Central", 32, "Surrey-Centre/Whalley", 49.189535827335895, -122.8475398262315],
                                        ["Surrey RCMP City Centre", 32, "Surrey-Centre/Whalley", 49.19736417274005, -122.84496916732236],
                                        ["APH Matthew Park", 32, "Surrey-Centre/Whalley", 49.17973374729407, -122.85377220651083] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon'])
    
    waiting_points = waiting_points.append(pd.DataFrame(np.array([ ["Nordel Crossing Shopping Mall", 33, "Surrey Newton", 49.16104243899859, -122.88865587131885], 
                                                 ["Scott Road Centre Shopping Mall", 33, "Surrey Newton", 49.14994315530216, -122.88893334238882],
                                                 ["Srawberry Hill Shopping Centre Shopping Mall", 33, "Surrey Newton", 49.13517773529771, -122.88755922607767],
                                                 ["Sunshine Hills Center Shopping Mall", 33, "Surrey Newton", 49.12002062040362, -122.89175370307956],
                                                 ["Mud Bay Park", 33, "Surrey Newton", 49.08986982158833, -122.86112810263145],
                                                 ["Sullivan Park", 33, "Surrey Newton", 49.11728248395325, -122.79715013110747],
                                                 ["TE Scott Park", 33, "Surrey Newton", 49.13037084018439, -122.81147797791704],
                                                 ["Surrey Lake Park", 33, "Surrey Newton", 49.138399550984865, -122.79614612704677],
                                                 ["Chimney Heights Park", 33, "Surrey Newton", 49.138556607716716, -122.81531466423046],
                                                 ["Hazelnut Meadows Community Park", 33, "Surrey Newton", 49.127854674248496, -122.83193509116693],
                                                 ["Unwin Park", 33, "Surrey Newton", 49.12715293603855, -122.85384248228392],
                                                 ["Panorama Park", 33, "Surrey Newton", 49.112649904758, -122.86519265156743],
                                                 ["Tamanawis Park", 33, "Surrey Newton", 49.12000384653464, -122.87397204769884],
                                                 ["Goldstone Park", 33, "Surrey Newton", 49.10916663022377, -122.81623995208818],
                                                 ["Royal Canadian Mounted Police", 33, "Surrey Newton", 49.107025425725375, -122.8244847402248],
                                                 ["West Newton Community Park", 33, "Surrey Newton", 49.1092704144431, -122.86057679520977],
                                                 ["Surrey RCMP District #3 Newton", 33, "Surrey Newton", 49.13438186323409, -122.8435026171556],
                                                 ["King's Cross Shopping Centre", 33, "Surrey Newton", 49.13835815761408, -122.84374257798639] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon']))

    waiting_points = waiting_points.append(pd.DataFrame(np.array([ ["Hawthorne Park", 12, "Fleetwood/Port Kells", 49.194293852181154, -122.82525889712429],
                                              ["Guildford Town Centre Shopping Mall", 12, "Fleetwood/Port Kells", 49.18971183911622, -122.80367239167182],
                                              ["Royal Canadian Mounted Police", 12, "Fleetwood/Port Kells", 49.19116938902156, -122.81309341483708],
                                              ["Riverside Heights Shopping Centre Shopping Mall", 12, "Fleetwood/Port Kells", 49.19926557107054, -122.81132354023254],
                                              ["Surrey Bend Regional Park", 12, "Fleetwood/Port Kells", 49.19432107678709, -122.7293082759732],
                                              ["Hemlock Park", 12, "Fleetwood/Port Kells", 49.17187849493195, -122.78266199414952],
                                              ["Fleetwood Park", 12, "Fleetwood/Port Kells", 49.14781441541337, -122.78117394619879],
                                              ["Surrey Lake Park", 12, "Fleetwood/Port Kells", 49.13927308960329, -122.80029424566669],
                                              ["Maple Green Park", 12, "Fleetwood/Port Kells", 49.16510673434747, -122.80777508939637],
                                              ["RCMP E-Division Headquarters", 12, "Fleetwood/Port Kells", 49.18013371631835, -122.8290536569733],
                                              ["Invergarry Bike Park", 12, "Fleetwood/Port Kells", 49.20794266165954, -122.81561068953008],
                                              ["Fraser View Park", 12, "Fleetwood/Port Kells", 49.206228454196506, -122.7778762790848],
                                              ["Bonnie Schrenk Park", 12, "Fleetwood/Port Kells", 49.15413989972187, -122.76416001200707],
                                              ["Tynehead Regional Park", 12, "Fleetwood/Port Kells", 49.17770674869902, -122.76075680798155],
                                              ["Port Kells Park", 12, "Fleetwood/Port Kells", 49.1622496141686, -122.68619782931457] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon']))

    waiting_points = waiting_points.append(pd.DataFrame(np.array([ ["North Creek Park", 7, "Cloverdale", 49.1321628523296, -122.72942945407485], 
                                                ["Hazelgrove Park", 7, "Cloverdale", 49.131407394343455, -122.69576298916574],
                                                ["Brooks Crescent Park", 7, "Cloverdale", 49.112863037325106, -122.68271761563372],
                                                ["Sunrise Ridge Park", 7, "Cloverdale", 49.10892373087935, -122.70377923462273],
                                                ["Don Christian Park", 7, "Cloverdale", 49.115861354718454, -122.71104191201809],
                                                ["Cloverdale Ball Park", 7, "Cloverdale", 49.115124466669315, -122.74147125579762],
                                                ["Katzei Park", 7, "Cloverdale", 49.12764098096632, -122.6853245350876],
                                                ["Hi-Knoll Park", 7, "Cloverdale", 49.092798819999025, -122.68070439458927],
                                                ["Claude Harvie Park", 7, "Cloverdale", 49.10737272282152, -122.71694530918182],
                                                ["Cloverdale Heights Park", 7, "Cloverdale", 49.10919137738007, -122.75021872584512],
                                                ["Royal Canadian Mounted Police", 7, "Cloverdale", 49.10646036064877, -122.73319992063335],
                                                ["Hillcrest Park", 7, "Cloverdale", 49.122177457766576, -122.70866377816668],
                                                ["North Cloverdale West Park", 7, "Cloverdale", 49.12523290483206, -122.71881229060615],
                                                ["Hunter Park", 7, "Cloverdale", 49.10183349389153, -122.70841441602116],
                                                ["Royal Canadian Mounted Police", 7, "Cloverdale", 49.10647633307813, -122.73349034912661],
                                                ["Greenaway Park", 7, "Cloverdale", 49.11182828374219, -122.72684933230092] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon']))

    waiting_points = waiting_points.append(pd.DataFrame(np.array([ ["Crescent Beach", 30, "White Rock/South Surrey", 49.05881587775597, -122.88148227520253],
                                                    ["Crescent Park", 30, "White Rock/South Surrey", 49.049562077200555, -122.86348973512933],
                                                    ["Kwomais Point Park", 30, "White Rock/South Surrey", 49.02769443381753, -122.86805946382756],
                                                    ["South Surrey Athletic Park", 30, "White Rock/South Surrey", 49.039206941325325, -122.81761561543483],
                                                    ["Peace Arch Hospital", 30, "White Rock/South Surrey", 49.0303975907737, -122.79318478985397],
                                                    ["Peace Arch Provincial Park", 30, "White Rock/South Surrey", 49.00578322388365, -122.75850651044877],
                                                    ["Redwood Park", 30, "White Rock/South Surrey", 49.03591073795251, -122.7250129785101],
                                                    ["Latimer Park", 30, "White Rock/South Surrey", 49.0512642348224, -122.69119059490397],
                                                    ["Dr. RJ Allan Hogg Rotary Park", 30, "White Rock/South Surrey", 49.02416625235945, -122.79344504996257],
                                                    ["Dogwood Park", 30, "White Rock/South Surrey", 49.03890118942815, -122.84918709556298],
                                                    ["Semiahmoo Shopping Centre", 30, "White Rock/South Surrey", 49.032784706643554, -122.80322188455305],
                                                    ["Centennial Park", 30, "White Rock/South Surrey", 49.029476102832035, -122.81658481917272],
                                                    ["Blumsen Park", 30, "White Rock/South Surrey", 49.06413099881579, -122.79365748633471],
                                                    ["The Shops at Morgan Crossing Outlet", 30, "White Rock/South Surrey", 49.04813617899905, -122.78349352621741],
                                                    ["Elgin Heritage Park", 30, "White Rock/South Surrey", 49.06488413728526, -122.84269477822286],
                                                    ["South Surrey RCMP", 30, "White Rock/South Surrey", 49.03488590031148, -122.80093099642106] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon']))

    print(waiting_points)
    insert_records(waiting_points)




if __name__ == "__main__":
    main()