import numpy as np
import pandas as pd
import sqlite3
from pathlib import Path
import os 



def insert_records(df):
    sqliteConnection = sqlite3.connect(os.path.join(os.path.dirname(__file__),'surrey.db'))
    df.to_sql('waiting_points', con=sqliteConnection, if_exists='replace', index=False)

def main():
    waiting_points_whalley = pd.DataFrame(np.array([ ["Bear Creek Park", 32, "Surrey-Centre/Whalley", 49.161383456039424, -122.84075812112808],
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
                                        ["APH Matthew Park", 32, "Surrey-Centre/Whalley", 49.17973374729407, -122.85377220651083] ]), columns=['name', 'FEDcode', 'FEDname', 'lat', 'lon'])
    
    waiting_points_newton = pd.DataFrame(np.array([ ["Nordel Crossing Shopping Mall", 33, "Surrey Newton", 49.16104243899859, -122.88865587131885], 
                                                 ["Super Store", 33, "Surrey Newton", 49.151140221826765, -122.89182837805852],
                                                 ["Scott Road Centre Shopping Mall", 33, "Surrey Newton", 49.14994315530216, -122.88893334238882],
                                                 ["Srawberry Hill Shopping Centre Shopping Mall", 33, "Surrey Newton", 49.13517773529771, -122.88755922607767],
                                                 ["Sunshine Hills Center Shopping Mall", 33, "Surrey Newton", 49.12002062040362, -122.89175370307956],
                                                 ["Mud Bay Park", 33, "Surrey Newton", 49.08986982158833, -122.86112810263145],
                                                 ["Sullivan Park", 33, "Surrey Newton", 49.11728248395325, -122.79715013110747],
                                                 ["TE Scott Park", 33, "Surrey Newton", 49.13037084018439, -122.81147797791704],
                                                 ["Surrey Lake Park", 33, "Surrey Newton", 49.138399550984865, -122.79614612704677],
                                                 ["Chimney Heights Park", 33, "Surrey Newton", 49.138556607716716, -122.81531466423046],
                                                 ["Bear Creek Park", 33, "Surrey Newton", 49.159596885999484, -122.84092847109878],
                                                 ["Hazelnut Meadows Community Park", 33, "Surrey Newton", 49.127854674248496, -122.83193509116693],
                                                 ["Unwin Park", 33, "Surrey Newton", 49.12715293603855, -122.85384248228392],
                                                 ["Panorama Park", 33, "Surrey Newton", 49.112649904758, -122.86519265156743],
                                                 ["Tamanawis Park", 33, "Surrey Newton", 49.12000384653464, -122.87397204769884],
                                                 ["Goldstone Park", 33, "Surrey Newton", 49.10916663022377, -122.81623995208818],
                                                 ["West Newton Community Park", 33, "Surrey Newton", 49.1092704144431, -122.86057679520977],
                                                 ["Surrey RCMP District #3 Newton", 33, "Surrey Newton", 49.13438186323409, -122.8435026171556],
                                                 ["King's Cross Shopping Centre", 33, "Surrey Newton", 49.13835815761408, -122.84374257798639],
                                                 
                                                 ]))



    insert_records(waiting_points_whalley)



if __name__ == "__main__":
    main()