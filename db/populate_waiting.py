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
    
    waiting_points_newton = pd.DataFrame(np.array([ ["Helling Park", 33, "Surrey Newton", 49.16078217302037, -122.89679935340443], 
                                                 ["Anytime Fitness", 33, "Surrey Newton", 49.16108121137133, -122.89156332001276],
                                                 ["Boston Pizza", 33, "Surrey Newton", 49.16147634514606, -122.88826634869848],
                                                 ["Mcdonalds", 33, "Surrey Newton", 49.159225925172066, -122.88962600153869],
                                                 ["Triple O's, Chevron", 33, "Surrey Newton", 49.15926052337047, -122.89124753645356],
                                                 ["Coast Capital", 33, "Surrey Newton", 49.15669775832766, -122.89085428316494],
                                                 ["Tasty Indian Bistro", 33, "Surrey Newton", 49.1541868494338, -122.89078342744128],
                                                 ["SuperStore", 33, "Surrey Newton", 49.151140221826765, -122.89182837805852],
                                                 ["Scott Road Centre Shopping Mall", 33, "Surrey Newton", 49.14994315530216, -122.88893334238882],
                                                 ["IHOP", 33, "Surrey Newton", 49.151991213886454, -122.8896964947562],
                                                 ["RBC Royal Bank", 33, "Surrey Newton", 49.14791839284902, -122.88975766890354],
                                                 ["Canadian Tire", 33, "Surrey Newton", 49.14613555377925, -122.88893859413541],
                                                 ["Shoppers Drugmart", 33, "Surrey Newton", 49.13970336001576, -122.88956429215322],
                                                 ["CIBC Branch", 49.13773938875949, -122.88879918941763],
                                                 ["Srawberry Hill Shopping Centre Shopping Mall", 33, "Surrey Newton", 49.13517773529771, -122.88755922607767],
                                                 ["Bank of Montreal", 33, "Surrey Newton", 49.13310094196062, -122.88961483373437],
                                                 ["Kabaddi Park", 33, "Surrey Newton", 49.130677467311855, -122.88696201497827],
                                                 ["Cougar Creek Park", 33, "Surrey Newton", 49.128729480038125, -122.88508906083756],
                                                 ["Beaver Creek Heights Park", 33, "Surrey Newton", 49.12481589035672, -122.8825833451809],
                                                 ["Spice of Punjab", 33, "Surrey Newton", 49.1188222218442, -122.88914532843687],
                                                 ["Go Dodge Surrey", 33, "Surrey Newton", 49.11695095846254, -122.88931350087675],
                                                 ["Boundary Park", 33, "Surrey Newton", 49.11247082102219, -122.88780949035618],
                                                 ["Corrigan Park", 33, "Surrey Newton", 49.11039585447977, -122.8744569711992],
                                                 ["Joe Brown Park", 33, "Surrey Newton", 49.10090594683712, -122.87721172977916],
                                                 ["Mud Bay Park", 33, "Surrey Newton", 49.08986982158833, -122.86112810263145],
                                                 ["Sobeys Surrey RSC", 33, "Surrey Newton", 49.100326498786785, -122.8028452162617],
                                                 ["Browns Social House", 33, "Surrey Newton", 49.103929838105586, -122.79867847598175],
                                                 ["Fresh St. Market Panorama Surrey", 33, "Surrey Newton", 49.10565346332678, -122.80460053175523],
                                                 ["Sullivan Park", 33, "Surrey Newton", 49.11728248395325, -122.79715013110747],
                                                 ["Sabzi Mandi Supermarket", 33, "Surrey Newton", 49.12686201138344, -122.79922760965194],
                                                 ["TE Scott Park", 33, "Surrey Newton", 49.13037084018439, -122.81147797791704],
                                                 ["Surrey Lake Park", 33, "Surrey Newton", 49.138399550984865, -122.79614612704677],
                                                 ["Chimney Hill Elementary", 33, "Surrey Newton", 49.13822527423844, -122.81381901795474],
                                                 ["British Manjor Park", 33, "Surrey Newton", 49.146310042500154, -122.8192625829443],
                                                 ["Enver Creek Park", 33, "Surrey Newton", 49.15136862411817, -122.81744473001768],
                                                 ["Petro Canada", 33, "Surrey Newton", 49.15365296398649, -122.82320672274209],
                                                 ["Bear Creek Park", 33, "Surrey Newton", 49.159596885999484, -122.84092847109878],
                                                 ["Enver Creek Secondary School", 33, "Surrey Newton", 49.15760550526286, -122.82129165829915],
                                                 ["Brookside Elementary", 33, "Surrey Newton", 49.1582866577973, -122.82844826133451],
                                                 ["Kennedy Trail Elementary", 33, "Surrey Newton", 49.15390982659449, -122.88320347939208],
                                                 ["Kennedy Trail Park", 33, "Surrey Newton", 49.15266227060392, -122.88351003680141],
                                                 ["Payak Business Centre", 33, "Surrey Newton", 49.15034542510537, -122.86584010494788],
                                                 ["Petro-Canada", 33, "Surrey Newton", 49.14887268423801, -122.84464383475735],
                                                 ["Hazelnut Meadows Community Park", 33, "Surrey Newton", 49.127854674248496, -122.83193509116693],
                                                 ["Unwin Park", 33, "Surrey Newton", 49.12715293603855, -122.85384248228392],
                                                 ["Princess Margaret Secondary School", 33, "Surrey Newton", 49.131929413860554, -122.86690539273616],
                                                 ["Newton Athletic Park", 33, "Surrey Newton", 49.13747554514121, -122.86942148962463],
                                                 ["Strawberry Hill Park", 33, "Surrey Newton", 49.14262065017988, -122.88158296025193],
                                                 ["Kwantlen Polytechnic University", 33, "Surrey Newton", 49.132899187070514, -122.87092494544596],
                                                 ["Goldstone Park Elementary School", 33, "Surrey Newton", 49.11675238320878, -122.81869438655457],
                                                 ["Sullivan Heights Secondary School", 33, "Surrey Newton", 49.11602909988081, -122.82163816369875],
                                                 ["Ecole Woodward Hill Elementary School", 33, "Surrey Newton", 49.11335042374483, -122.82800575927526],
                                                 ["North Ridge Elementary", 33, "Surrey Newton", 49.11487568912901, -122.84924877145428],
                                                 ["Panorama Ridge Secondary School", 49.118055820525235, -122.85462545867671],
                                                 ["Panorama Park", 33, "Surrey Newton", 49.112649904758, -122.86519265156743],
                                                 ["Panorama Park Elementary School", 33, "Surrey Newton", 49.11474687052454, -122.86602453235363],
                                                 ["Tamanawis Secondary School", 33, "Surrey Newton", 49.122496514538376, -122.87166534757912],
                                                 ["Tamanawis Park", 33, "Surrey Newton", 49.12000384653464, -122.87397204769884],
                                                 ["Aspen Park", 33, "Surrey Newton", 49.1107621338274, -122.85099555940889],
                                                 ["Goldstone Park", 33, "Surrey Newton", 49.10916663022377, -122.81623995208818],
                                                 ["Cambridge Elementary School", 33, "Surrey Newton", 49.11357209648151, -122.80824274791796],
                                                 ["White Spot Panorama", 33, "Surrey Newton", 49.10560056013907, -122.80211183260481],
                                                 ["Fresh St. Market Panorama Surrey", 33, "Surrey Newton", 49.10547288070621, -122.80506702798465],
                                                 ["Panorama Village Park", 33, "Surrey Newton", 49.105922627375506, -122.80881205662443],
                                                 ["West Newton Community Park", 33, "Surrey Newton", 49.1092704144431, -122.86057679520977],
                                                 ["J T Brown Elementary", 33, "Surrey Newton", 49.11111471637796, -122.87548708753694],
                                                 ["Martha Jane Norris Elementary School", 33, "Surrey Newton", 49.123510023684105, -122.86501489387742],
                                                 ["WE Kinvig Elementary School", 33, "Surrey Newton", 49.13042842611057, -122.85436626614965],
                                                 ["Newton Square Maill", 33, "Surrey Newton", 49.1309688535362, -122.84723184251526],
                                                 ["Newton Town Centre", 33, "Surrey Newton", 49.13206858819059, -122.84012734554067],
                                                 ["Newton Recreation Centre", 33, "Surrey Newton", 49.1330383061244, -122.84250687272599],
                                                 ["Surrey RCMP District #3 Newton", 33, "Surrey Newton", 49.13438186323409, -122.8435026171556],
                                                 ["Real Canadian Superstore", 33, "Surrey Newton", 49.13948880639876, -122.84388413939232],
                                                 ["Costco", 49.13831874499279, 33, "Surrey Newton", -122.8482202490181],
                                                 ["Frank Hurt Secondary School", 33, "Surrey Newton", 49.14214211241678, -122.83672371941478],
                                                 ["Todd Crescent Park", 33, "Surrey Newton", 49.136198105896646, -122.83203633529243],
                                                 ["Surrey Fire Service Hall 10", 33, "Surrey Newton", 49.13514537729331, -122.85549787588404],
                                                 ["Club16", 33, "Surrey Newton", 49.12789273833502, -122.84663299634751]



                                                 
                                                 ]))



    insert_records(waiting_points_whalley)



if __name__ == "__main__":
    main()