from src.village import Village
from src.input import *

import os
import sys

import os.path

village = Village()
village.build_huts()
village.build_walls()
village.build_cannons()
village.build_towers()

if (os.path.exists('./replays')==False):
    os.makedirs('./replays')
file_name = "./replays/replay_"
check=1
while(1):
    if(os.path.exists(file_name+str(check)+".txt")):
        check+=1
    else:
        break   
file_name=file_name+str(check)+".txt"

print("Select Queen(q) or King(k)")
queen_or_king = input()
while(True):
    village.render(file_name,queen_or_king)
    cha = get_input()
    village.take_input(cha,queen_or_king)
    if cha == 'q':
        break               