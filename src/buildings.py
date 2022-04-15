from colorama import Fore, Back, Style 
from os import system
from time import sleep,time
import math


class Building():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=10
        self.height=10

        
class TownHall(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=3
        self.height=4
        self.Mhpts = 300
        self.hpts = 300
        self.pixel1 = Back.GREEN+' '+Style.RESET_ALL
        self.pixel2 = Back.CYAN+' '+Style.RESET_ALL
        self.pixel3 = Back.BLUE+' '+Style.RESET_ALL
        self.alive = True

        
        

class Hut(Building):
    def __init__(self,x,y) :
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 40
        self.hpts = 40
        self.pixel1 = Back.GREEN+' '+Style.RESET_ALL
        self.pixel2 = Back.CYAN+' '+Style.RESET_ALL
        self.pixel3 = Back.BLUE+' '+Style.RESET_ALL
        self.alive = True

class Wall(Building):
    def __init__(self,x,y) :
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 30
        self.hpts = 30
        self.pixel1 = Back.RED+' '+Style.RESET_ALL      
        self.pixel2 = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.pixel3 = Back.LIGHTRED_EX+' '+Style.RESET_ALL
        self.alive = True  

class Troop(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 50
        self.hpts = 50
        self.damage=5
        #self.damage=0
        self.speed =1
        self.pixel1 = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.pixel2 = Back.BLUE+' '+Style.RESET_ALL
        self.pixel3 = Back.WHITE+' '+Style.RESET_ALL
        self.alive =True  
        self.target_no=100
        #self.target

class Archer(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 25
        self.hpts = 25
        self.damage=2.5
        self.speed =2
        self.pixel1 = Back.BLUE+'A'+Style.RESET_ALL
        self.pixel2 = Back.WHITE+'A'+Style.RESET_ALL
        self.pixel3 = Back.LIGHTYELLOW_EX+'A'+Style.RESET_ALL
        self.alive =True
        self.range=4
        self.target_no=100

class Balloon(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 50
        self.hpts = 50
        self.damage=10
        self.speed =2
        self.pixel1 = Back.WHITE+'B'+Style.RESET_ALL
        self.pixel2 = Back.LIGHTYELLOW_EX+'B'+Style.RESET_ALL
        self.pixel3 = Back.BLUE+'B'+Style.RESET_ALL
        self.alive =True
        self.target_no=100        


class Cannon(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 60
        self.hpts = 60
        self.range=6
        self.damage=20
        # self.damage=0
        self.pixel1 = Back.RED+' '+Style.RESET_ALL  
        self.pixel2 = Back.WHITE+' '+Style.RESET_ALL 
        self.pixel3 = Back.BLUE+' '+Style.RESET_ALL  
        self.pixel4=Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.alive =True
        self.attacking_on=100  

class Tower(Building):
    def __init__(self,x,y):
        Building.__init__(self,x,y)
        self.width=1
        self.height=1
        self.Mhpts = 50
        self.hpts = 50
        self.range=6
        self.damage=20
        # self.damage=0
        self.pixel1 = Back.RED+'T'+Style.RESET_ALL  
        self.pixel2 = Back.WHITE+'T'+Style.RESET_ALL 
        self.pixel3 = Back.BLUE+'T'+Style.RESET_ALL  
        self.pixel4=Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL
        self.alive =True  
        self.attacking_on=100             