import os
import sys

def Replay(file_name):
    with open(file_name,'r') as f:
        all_lines=f.readlines()
        frame=[]
        check=0
        for line in all_lines:
            frame.append(line)
            check = check+1
            if(check%60==0):
                os.system('clear')
                print(''.join(frame))
                os.system('sleep 0.5')
                frame=[]

replay_no=input("Enter replay number: ")
file_name="./replays/replay_"+replay_no+".txt"
Replay(file_name)                