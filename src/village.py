from difflib import unified_diff
from colorama import Fore, Back, Style
from os import system
from time import sleep, time
import math

from src.buildings import *
from src.king import *


class Village():
    def __init__(self):
        self.rows = 60
        self.cols = 100
        self.king = King(5, 6,200,30)
        self.townhall = TownHall(50, 25)
        self.huts = []
        self.walls = []
        self.cannons = []
        self.troops = []
        self.archers = []
        self.balloons = []
        self.towers=[]
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.start_time = -0.5
        self.start_time_2 = -0.5
        self.attacking_on1 = 100
        self.attacking_on2 = 100
        self.current_time = 0
        self.rage_time = 5
        self.rage_start_time = 0
        self.start_time_bar = -0.5
        self.start_time_arch = -0.25
        self.start_time_balloon = -0.25
        self.queen_prev='p'
        self.queen_x=self.king.x
        self.queen_y=self.king.y
        self.level=1
        self.mtime=0
        self.mattack=False
        self.qchange=False
        # self.unfilled_blocks = [
        #     [0 for i in range(self.cols)] for j in range(self.rows)]

    def build_huts(self):
        hut = Hut(0, 0)
        self.huts.append(hut)
        hut = Hut(0, 49)
        self.huts.append(hut)
        hut = Hut(99, 0)
        self.huts.append(hut)
        hut = Hut(99, 49)
        self.huts.append(hut)
        # hut = Hut(99, 6)
        # self.huts.append(hut)
        hut = Hut(54, 23)
        self.huts.append(hut)
        # print(self.huts)

    def build_walls(self):
        wall = Wall(self.townhall.x-1, self.townhall.y-1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x, self.townhall.y-1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+1, self.townhall.y-1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+2, self.townhall.y-1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y-1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x-1, self.townhall.y)
        self.walls.append(wall)
        wall = Wall(self.townhall.x-1, self.townhall.y+1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x-1, self.townhall.y+2)
        self.walls.append(wall)
        wall = Wall(self.townhall.x-1, self.townhall.y+3)
        self.walls.append(wall)
        wall = Wall(self.townhall.x-1, self.townhall.y+4)
        self.walls.append(wall)
        wall = Wall(self.townhall.x, self.townhall.y+4)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+1, self.townhall.y+4)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+2, self.townhall.y+4)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y+4)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y+3)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y+2)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y+1)
        self.walls.append(wall)
        wall = Wall(self.townhall.x+3, self.townhall.y)
        self.walls.append(wall)

    def build_cannons(self):
        cannon = Cannon(20, 30)
        self.cannons.append(cannon)
        cannon = Cannon(30, 40)
        self.cannons.append(cannon)
        cannon = Cannon(40, 20)
        self.cannons.append(cannon)
        self.cannons[2].alive = False
        cannon = Cannon(50, 10)
        self.cannons.append(cannon)
        self.cannons[3].alive = False

    def build_towers(self):
        tower=Tower(46,17)  
        self.towers.append(tower)
        tower=Tower(89,39)  
        self.towers.append(tower)
        tower=Tower(89,17)
        self.towers.append(tower)
        self.towers[2].alive=False
        tower=Tower(46,39)
        self.towers.append(tower)
        self.towers[3].alive=False

    def build_troops(self, x, y):
        if(len(self.troops) < 6):
            troop = Troop(x, y)
            self.troops.append(troop)

    def build_archer(self, x, y):
        if(len(self.archers) < 6):
            archer = Archer(x, y)
            self.archers.append(archer)

    def build_balloon(self, x, y):
        if(len(self.balloons) < 3):
            balloon = Balloon(x, y)
            self.balloons.append(balloon)

    def king_shoot(self):
        attack_done = False
        if self.townhall.alive == True:
            if((self.king.y == self.townhall.y-1 or self.king.y == self.townhall.y+4) and (self.king.x == self.townhall.x-1 or self.king.x == self.townhall.x or self.king.x == self.townhall.x+1 or self.king.x == self.townhall.x+2 or self.king.x == self.townhall.x+3)):
                self.townhall.hpts -= self.king.damage
                attack_done = True
                if self.townhall.hpts <= 0:
                    self.townhall.alive = False
                    self.townhall.hpts = 0

            elif((self.king.x == self.townhall.x-1 or self.king.x == self.townhall.x+3) and (self.king.y == self.townhall.y-1 or self.king.y == self.townhall.y or self.king.y == self.townhall.y+1 or self.king.y == self.townhall.y+2 or self.king.y == self.townhall.y+3 or self.king.y == self.townhall.y+4)):
                self.townhall.hpts -= self.king.damage
                attack_done = True
                if self.townhall.hpts <= 0:
                    self.townhall.alive = False
                    self.townhall.hpts = 0
        if(attack_done == False):
            for cannon in self.cannons:
                if(cannon.alive == True):
                    if((self.king.x == cannon.x-1 or self.king.x == cannon.x+1) and (self.king.y == cannon.y-1 or self.king.y == cannon.y or self.king.y == cannon.y+1)):
                        cannon.hpts -= self.king.damage
                        attack_done = True
                        if cannon.hpts <= 0:
                            cannon.hpts = 0
                            # self.cannons.remove(cannon)
                            cannon.alive = False
                        break
                    elif(self.king.x == cannon.x and (self.king.y == cannon.y-1 or self.king.y == cannon.y+1)):
                        cannon.hpts -= self.king.damage
                        attack_done = True
                        if cannon.hpts <= 0:
                            cannon.hpts = 0
                            # self.cannons.remove(cannon)
                            cannon.alive = False
                        break
        if attack_done == False:
            for tower in self.towers:
                if(tower.alive == True):
                    if((self.king.x == tower.x-1 or self.king.x == tower.x+1) and (self.king.y == tower.y-1 or self.king.y == tower.y or self.king.y == tower.y+1)):
                        tower.hpts -= self.king.damage
                        attack_done = True
                        if tower.hpts <= 0:
                            tower.hpts = 0
                            # self.towers.remove(tower)
                            tower.alive = False
                        break
                    elif(self.king.x == tower.x and (self.king.y == tower.y-1 or self.king.y == tower.y+1)):
                        tower.hpts -= self.king.damage
                        attack_done = True
                        if tower.hpts <= 0:
                            tower.hpts = 0
                            # self.towers.remove(tower)
                            tower.alive = False
                        break
        if(attack_done == False):
            for hut in self.huts:
                if(hut.alive == True):
                    if((self.king.x == hut.x-1 or self.king.x == hut.x+1) and (self.king.y == hut.y-1 or self.king.y == hut.y or self.king.y == hut.y+1)):
                        hut.hpts -= self.king.damage
                        attack_done = True
                        if hut.hpts <= 0:
                            hut.hpts = 0
                            hut.alive = False
                        break
                    elif(self.king.x == hut.x and (self.king.y == hut.y-1 or self.king.y == hut.y+1)):
                        hut.hpts -= self.king.damage
                        attack_done = True
                        if hut.hpts <= 0:
                            hut.hpts = 0
                            hut.alive = False
                        break
        if(attack_done == False):

            # print("wall\n")
            for wall in self.walls:
                #print(wall.x, ",", wall.y)
                if(wall.alive == True):
                    if((self.king.x == wall.x-1 or self.king.x == wall.x+1) and (self.king.y == wall.y-1 or self.king.y == wall.y or self.king.y == wall.y+1)):
                        wall.hpts -= self.king.damage
                        attack_done = True
                        if wall.hpts <= 0:
                            wall.hpts = 0
                            wall.alive = False
                        break
                    elif(self.king.x == wall.x and (self.king.y == wall.y-1 or self.king.y == wall.y+1)):
                        wall.hpts -= self.king.damage
                        attack_done = True
                        if wall.hpts <= 0:
                            wall.hpts = 0
                            wall.alive = False
                        break

    def queen_shoot(self, prev):
        #print(prev,"\n")
        x_cord = self.king.x
        y_cord = self.king.y
        if(prev == 'p'):
            return
        if prev == 'w':
            x_cord = self.king.x
            y_cord= self.king.y-8

        if prev == 'a':
            x_cord = self.king.x-8
            y_cord = self.king.y

        if prev == 's':
            x_cord = self.king.x
            y_cord = self.king.y+8
        if prev == 'd':
            x_cord = self.king.x+8
            y_cord = self.king.y

        if x_cord<0:
            x_cord = 0
        if x_cord>=self.cols:
            x_cord = self.cols-1  
        if y_cord<0:
            y_cord = 0
        if y_cord>=self.rows:
            y_cord = self.rows-1 
        # print(prev,"\n")    
        # print(self.king.x, ",", self.king.y, "\n")    
        # print(center_x, ",", center_y)
        for cannon in self.cannons:
            if(cannon.alive == True):
                if(cannon.x>=x_cord-2 and cannon.x<=x_cord+2 and cannon.y>=y_cord-2 and cannon.y<=y_cord+2):
                    cannon.hpts -= self.king.damage
                    if cannon.hpts <= 0:
                        cannon.hpts = 0
                        cannon.alive = False
                        break
        for tower in self.towers:
            if(tower.alive == True):
                if(tower.x>=x_cord-2 and tower.x<=x_cord+2 and tower.y>=y_cord-2 and tower.y<=y_cord+2):
                    tower.hpts -= self.king.damage
                    if tower.hpts <= 0:
                        tower.hpts = 0
                        tower.alive = False
                        break       
        for hut in self.huts:
            if(hut.alive == True):
                if(hut.x>=x_cord-2 and hut.x<=x_cord+2 and hut.y>=y_cord-2 and hut.y<=y_cord+2):
                    hut.hpts -= self.king.damage
                    if hut.hpts <= 0:
                        hut.hpts = 0
                        hut.alive = False
                        break

        for wall in self.walls:
            if(wall.alive == True):
                if(wall.x>=x_cord-2 and wall.x<=x_cord+2 and wall.y>=y_cord-2 and wall.y<=y_cord+2):
                    wall.hpts -= self.king.damage
                    if wall.hpts <= 0:
                        wall.hpts = 0
                        wall.alive = False
                        break
        if self.townhall.alive:
            in_range=False
            for row in range(self.townhall.y,self.townhall.y+self.townhall.height):
                for col in range(self.townhall.x,self.townhall.x+self.townhall.width):
                    if(row>=y_cord-2 and row<=y_cord+2 and col>=x_cord-2 and col<=x_cord+2):
                        in_range=True
                        break
                if(in_range):
                    break
            if(in_range):
                self.townhall.hpts -= self.king.damage
                if self.townhall.hpts <= 0:
                    self.townhall.hpts = 0
                    self.townhall.alive = False                     

    def queen_shoot2(self,prev,queen_x,queen_y):
        #print(prev,"\n")
        x_cord = queen_x
        y_cord = queen_y
        if(prev == 'p'):
            return
        if prev == 'w':
            x_cord = queen_x
            y_cord= queen_y-16

        if prev == 'a':
            x_cord = queen_x-16
            y_cord = queen_y

        if prev == 's':
            x_cord = queen_x
            y_cord = queen_y+16
        if prev == 'd':
            x_cord = queen_x+16
            y_cord = queen_y

        if x_cord<0:
            x_cord = 0
        if x_cord>=self.cols:
            x_cord = self.cols-1  
        if y_cord<0:
            y_cord = 0
        if y_cord>=self.rows:
            y_cord = self.rows-1 
        # print(prev,"\n")    
      
        for cannon in self.cannons:
            if(cannon.alive == True):
                if(cannon.x>=x_cord-4 and cannon.x<=x_cord+4 and cannon.y>=y_cord-4 and cannon.y<=y_cord+4):
                    cannon.hpts -= self.king.damage
                    if cannon.hpts <= 0:
                        cannon.hpts = 0
                        cannon.alive = False
        for tower in self.towers:
            if(tower.alive == True):
                if(tower.x>=x_cord-4 and tower.x<=x_cord+4 and tower.y>=y_cord-4 and tower.y<=y_cord+4):
                   
                    tower.hpts -= self.king.damage
                    if tower.hpts <= 0:
                        tower.hpts = 0
                        tower.alive = False
                        break       
        for hut in self.huts:
            if(hut.alive == True):
                if(hut.x>=x_cord-4 and hut.x<=x_cord+4 and hut.y>=y_cord-4 and hut.y<=y_cord+4):
                    hut.hpts -= self.king.damage
                    if hut.hpts <= 0:
                        hut.hpts = 0
                        hut.alive = False
                        break

        for wall in self.walls:
            if(wall.alive == True):
                if(wall.x>=x_cord-4 and wall.x<=x_cord+4 and wall.y>=y_cord-4 and wall.y<=y_cord+4):
                    wall.hpts -= self.king.damage
                    if wall.hpts <= 0:
                        wall.hpts = 0
                        wall.alive = False
                        break
        if self.townhall.alive:
            in_range=False
            for row in range(self.townhall.y,self.townhall.y+self.townhall.height):
                for col in range(self.townhall.x,self.townhall.x+self.townhall.width):
                    if(row>=y_cord-2 and row<=y_cord+2 and col>=x_cord-2 and col<=x_cord+2):
                        in_range=True
                        break
                if(in_range):
                    break
            if(in_range):
                self.townhall.hpts -= self.king.damage
                if self.townhall.hpts <= 0:
                    self.townhall.hpts = 0
                    self.townhall.alive = False   
  
    def dist_from_king(self, x, y):
        dist = ((self.king.x - x)**2 + (self.king.y - y)**2)**0.5
        return dist

    def leviathan(self):
        for cannon in self.cannons:
            if(cannon.alive == True):
                if(self.dist_from_king(cannon.x, cannon.y) <= 7):
                    cannon.hpts -= self.king.damage
                    if cannon.hpts <= 0:
                        cannon.hpts = 0
                        cannon.alive = False
        for tower in self.towers:
            if(tower.alive == True):
                if(self.dist_from_king(tower.x, tower.y) <= 7):
                    tower.hpts -= self.king.damage
                    if tower.hpts <= 0:
                        tower.hpts = 0
                        tower.alive = False
        for hut in self.huts:
            if(hut.alive == True):
                if(self.dist_from_king(hut.x, hut.y) <= 7):
                    hut.hpts -= self.king.damage
                    if hut.hpts <= 0:
                        hut.hpts = 0
                        hut.alive = False

        for wall in self.walls:
            if(wall.alive == True):
                if(self.dist_from_king(wall.x, wall.y) <= 7):
                    wall.hpts -= self.king.damage
                    if wall.hpts <= 0:
                        wall.hpts = 0
                        wall.alive = False

        if self.townhall.alive == True:
            in_range = False
            for row in range(self.townhall.y, self.townhall.y+self.townhall.height):
                for col in range(self.townhall.x, self.townhall.x+self.townhall.width):
                    if(self.dist_from_king(col, row) <= 7):
                        in_range = True
                        break
                if in_range == True:
                    break
            if in_range == True:
                self.townhall.hpts -= self.king.damage
                if self.townhall.hpts <= 0:
                    self.townhall.hpts = 0
                    self.townhall.alive = False

    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def cannon_attack(self, cannon):
        attacking = False
        if(cannon.alive):
            if(cannon.attacking_on == 0):
               if self.king.alive==False:
                cannon.attacking_on = 100
            if cannon.attacking_on>0 and cannon.attacking_on<=6: 
                if(self.troops[cannon.attacking_on-1].alive==False):

                    cannon.attacking_on = 100      

            if cannon.attacking_on>6 and cannon.attacking_on<=12:
                if(self.archers[cannon.attacking_on-7].alive==False): 
                    cannon.attacking_on = 100  

            if cannon.attacking_on>12 and cannon.attacking_on<=15:
                if(self.balloons[cannon.attacking_on-13].alive==False):
                    cannon.attacking_on = 100
            if(cannon.attacking_on == 0 and self.king.alive):
                if(self.dist(cannon.x, cannon.y, self.king.x, self.king.y) < cannon.range):
                    self.king.hpts -= cannon.damage
                    cannon.attacking_on = 0
                    attacking = True
                    if self.king.hpts <= 0:
                        self.king.alive = False
                        self.king.hpts = 0
                        cannon.attacking_on = 100
            if(cannon.attacking_on != 100 and cannon.attacking_on != 0):
                if(len(self.troops) > 0 and cannon.attacking_on <=6):
                    if(self.troops[cannon.attacking_on-1].alive):
                        if(self.dist(cannon.x, cannon.y, self.troops[cannon.attacking_on-1].x, self.troops[cannon.attacking_on-1].y) < cannon.range):
                            self.troops[cannon.attacking_on -1].hpts -= cannon.damage
                            attacking = True
                            if(self.troops[cannon.attacking_on-1].hpts <= 0):
                                self.troops[cannon.attacking_on -1].alive = False
                                self.troops[cannon.attacking_on-1].hpts = 0
                                cannon.attacking_on = 100
                elif(cannon.attacking_on > 6 and cannon.attacking_on <= 12 and len(self.archers) > 0):
                    if(self.archers[cannon.attacking_on-7].alive):
                        if(self.dist(cannon.x, cannon.y, self.archers[cannon.attacking_on-7].x, self.archers[cannon.attacking_on-7].y) < cannon.range):
                            self.archers[cannon.attacking_on -7].hpts -= cannon.damage
                            attacking = True
                            if(self.archers[cannon.attacking_on-7].hpts <= 0):
                                self.archers[cannon.attacking_on -7].alive = False
                                self.archers[cannon.attacking_on-7].hpts = 0
                                cannon.attacking_on = 100            
            if(cannon.attacking_on == 100):
                if(self.king.alive):
                    if(self.dist(cannon.x, cannon.y, self.king.x, self.king.y) < cannon.range):
                        self.king.hpts -= cannon.damage
                        cannon.attacking_on = 0
                        attacking = True
                        if self.king.hpts <= 0:
                            self.king.alive = False
                            self.king.hpts = 0
                            cannon.attacking_on = 100

                if(self.king.alive == False or self.dist(cannon.x, cannon.y, self.king.x, self.king.y) > cannon.range):
                    for i in range(len(self.troops)):
                        if(self.troops[i].alive):
                            if(self.dist(cannon.x, cannon.y, self.troops[i].x, self.troops[i].y) < cannon.range):
                                self.troops[i].hpts -= cannon.damage
                                cannon.attacking_on = i+1
                                attacking = True
                                if self.troops[i].hpts <= 0:
                                    self.troops[i].alive = False
                                    self.troops[i].hpts = 0
                                    cannon.attacking_on = 100
                                break
                    for i in range(len(self.archers)):
                        if(self.archers[i].alive):
                            if(self.dist(cannon.x, cannon.y, self.archers[i].x, self.archers[i].y) < cannon.range):
                                
                                self.archers[i].hpts -= cannon.damage
                                cannon.attacking_on = i+7
                                attacking = True
                                if self.archers[i].hpts <= 0:
                                    self.archers[i].alive = False
                                    self.archers[i].hpts = 0
                                    cannon.attacking_on = 100
                                break        
            if attacking:
                for row in range(cannon.y, cannon.y+(cannon.height)):
                    for col in range(cannon.x, cannon.x+(cannon.width)):
                        self.board[row][col] = cannon.pixel2
                        self.unfilled_blocks[row][col] = 1
            else:
                for row in range(cannon.y, cannon.y+(cannon.height)):
                    for col in range(cannon.x, cannon.x+(cannon.width)):
                        if cannon.hpts > cannon.Mhpts/2:
                            self.board[row][col] = cannon.pixel1
                        elif cannon.hpts <= cannon.Mhpts//2 and cannon.hpts > cannon.Mhpts//5:
                            self.board[row][col] = cannon.pixel3
                        else:
                            self.board[row][col] = cannon.pixel4
                        self.unfilled_blocks[row][col] = 1

    def tower_attack_kill_near_by(self, tower,x,y):
        if(tower.alive):
            if self.king.alive:
                if(self.king.x>=x-1 and self.king.x<=x+1 and self.king.y>=y-1 and self.king.y<=y+1):
                    self.king.hpts -= tower.damage
                    if self.king.hpts <= 0:
                        self.king.alive = False
                        self.king.hpts = 0
            for troop in self.troops:
                if(troop.alive):
                    if(troop.x>=x-1 and troop.x<=x+1 and troop.y>=y-1 and troop.y<=y+1):
                        troop.hpts-=tower.damage
                        if troop.hpts <= 0:
                            troop.alive = False
                            troop.hpts = 0
            for archer in self.archers:
                if(archer.alive):
                    if(archer.x>=x-1 and archer.x<=x+1 and archer.y>=y-1 and archer.y<=y+1):
                        archer.hpts-=tower.damage
                        if archer.hpts <= 0:
                            archer.alive = False
                            archer.hpts = 0
            for balloon in self.balloons:
                if(balloon.alive):
                    if(balloon.x>=x-1 and balloon.x<=x+1 and balloon.y>=y-1 and balloon.y<=y+1):
                        balloon.hpts-=tower.damage
                        if balloon.hpts <= 0:
                            balloon.alive = False
                            balloon.hpts = 0                                

    
    
    def tower_attack(self, tower):
        attacking = False
            
        if(tower.alive):
            if(tower.attacking_on == 0):
                if self.king.alive==False:
                    tower.attacking_on = 100
            if tower.attacking_on>0 and tower.attacking_on<=6: 
                if(self.troops[tower.attacking_on-1].alive==False):

                    tower.attacking_on = 100      

            if tower.attacking_on>6 and tower.attacking_on<=12:
                if(self.archers[tower.attacking_on-7].alive==False): 
                    tower.attacking_on = 100  

            if tower.attacking_on>12 and tower.attacking_on<=15:
                if(self.balloons[tower.attacking_on-13].alive==False):
                    tower.attacking_on = 100         

            if(tower.attacking_on == 0 and self.king.alive):
                if(self.dist(tower.x, tower.y, self.king.x, self.king.y) < tower.range):
                    #self.king.hpts -= tower.damage
                    tower.attacking_on = 0
                    attacking = True
                    self.tower_attack_kill_near_by(tower,self.king.x, self.king.y)
                    # if self.king.hpts <= 0:
                    #     self.king.alive = False
                    #     self.king.hpts = 0
                    #     tower.attacking_on = 100
            if(tower.attacking_on != 100 and tower.attacking_on != 0):
                if(len(self.troops) > 0 and tower.attacking_on <=6):
                    if(self.troops[tower.attacking_on-1].alive):
                        if(self.dist(tower.x, tower.y, self.troops[tower.attacking_on-1].x, self.troops[tower.attacking_on-1].y) < tower.range):
                            #self.troops[tower.attacking_on - 1].hpts -= tower.damage
                            attacking = True
                            self.tower_attack_kill_near_by(tower,self.troops[tower.attacking_on-1].x, self.troops[tower.attacking_on-1].y)
                            # if(self.troops[tower.attacking_on-1].hpts <= 0):
                            #     self.troops[tower.attacking_on - 1].alive = False
                            #     self.troops[tower.attacking_on-1].hpts = 0
                            #     tower.attacking_on = 100
                elif(tower.attacking_on > 6 and tower.attacking_on <= 12):
                    if(self.archers[tower.attacking_on-7].alive):
                        if(self.dist(tower.x, tower.y, self.archers[tower.attacking_on-7].x, self.archers[tower.attacking_on-7].y) < tower.range):
                            #self.archers[tower.attacking_on -7].hpts -= tower.damage
                            attacking = True
                            self.tower_attack_kill_near_by(tower,self.archers[tower.attacking_on-7].x, self.archers[tower.attacking_on-7].y)
                            # if(self.archers[tower.attacking_on-7].hpts <= 0):
                            #     self.archers[tower.attacking_on -7].alive = False
                            #     self.archers[tower.attacking_on-7].hpts = 0
                            #     tower.attacking_on = 100

                elif (tower.attacking_on > 12 and tower.attacking_on <= 15):
                    if(self.balloons[tower.attacking_on-13].alive):
                        if(self.dist(tower.x, tower.y, self.balloons[tower.attacking_on-13].x, self.balloons[tower.attacking_on-13].y) < tower.range):
                            #self.balloons[tower.attacking_on - 13].hpts -= tower.damage
                            attacking = True
                            self.tower_attack_kill_near_by(tower,self.balloons[tower.attacking_on-13].x, self.balloons[tower.attacking_on-13].y)
                            # if(self.balloons[tower.attacking_on-13].hpts <= 0):
                            #     self.balloons[tower.attacking_on - 13].alive = False
                            #     self.balloons[tower.attacking_on-13].hpts = 0
                            #     tower.attacking_on = 100              
            if(tower.attacking_on == 100):
                if(self.king.alive):
                    if(self.dist(tower.x, tower.y, self.king.x, self.king.y) < tower.range):
                        #self.king.hpts -= tower.damage
                        tower.attacking_on = 0
                        attacking = True
                        self.tower_attack_kill_near_by(tower,self.king.x, self.king.y)
                        # if self.king.hpts <= 0:
                        #     self.king.alive = False
                        #     self.king.hpts = 0
                        #     tower.attacking_on = 100
                if self.king.alive == False or self.dist(tower.x, tower.y, self.king.x, self.king.y) > tower.range:
                    for i in range(len(self.troops)):
                        if(self.troops[i].alive):
                            if(self.dist(tower.x, tower.y, self.troops[i].x, self.troops[i].y) < tower.range):
                               # self.troops[i].hpts -= tower.damage
                                tower.attacking_on = i+1
                                attacking = True
                                self.tower_attack_kill_near_by(tower,self.troops[i].x, self.troops[i].y)
                                # if self.troops[i].hpts <= 0:
                                #     self.troops[i].alive = False
                                #     self.troops[i].hpts = 0
                                #     tower.attacking_on = 100
                                break
                    for i in range(len(self.archers)):
                        if(self.archers[i].alive):
                            if(self.dist(tower.x, tower.y, self.archers[i].x, self.archers[i].y) < tower.range):
                                #self.archers[i].hpts -= tower.damage
                                tower.attacking_on = i+7
                                attacking = True
                                self.tower_attack_kill_near_by(tower,self.archers[i].x, self.archers[i].y)
                                # if self.archers[i].hpts <= 0:
                                #     self.archers[i].alive = False
                                #     self.archers[i].hpts = 0
                                #     tower.attacking_on = 100
                                break

                    for i in range(len(self.balloons)):
                        if (self.balloons[i].alive):
                            if (self.dist(tower.x, tower.y, self.balloons[i].x, self.balloons[i].y) < tower.range):
                                #self.balloons[i].hpts -= tower.damage
                                tower.attacking_on = i + 13
                                attacking = True
                                self.tower_attack_kill_near_by(tower, self.balloons[i].x, self.balloons[i].y)
                                # if self.balloons[i].hpts <= 0:
                                #     self.balloons[i].alive = False
                                #     self.balloons[i].hpts = 0
                                #     tower.attacking_on = 100
                                break         
            if attacking:
                for row in range(tower.y, tower.y+(tower.height)):
                    for col in range(tower.x, tower.x+(tower.width)):
                        self.board[row][col] = tower.pixel2
                        self.unfilled_blocks[row][col] = 1
            else:
                for row in range(tower.y, tower.y+(tower.height)):
                    for col in range(tower.x, tower.x+(tower.width)):
                        if tower.hpts > tower.Mhpts/2:
                            self.board[row][col] = tower.pixel1
                        elif tower.hpts <= tower.Mhpts//2 and tower.hpts > tower.Mhpts//5:
                            self.board[row][col] = tower.pixel3
                        else:
                            self.board[row][col] = tower.pixel4
                        self.unfilled_blocks[row][col] = 1                                        

                
    
    
    def wall_barb(self, troop):
        ret_val = False
        for wall in self.walls:
            if(wall.alive == True):
                if((troop.x == wall.x-1 or troop.x == wall.x+1) and (troop.y == wall.y-1 or troop.y == wall.y or troop.y == wall.y+1)):
                    wall.hpts -= troop.damage
                    ret_val = True
                    if wall.hpts <= 0:
                        wall.hpts = 0
                        wall.alive = False
                    break
                elif(troop.x == wall.x and (troop.y == wall.y-1 or troop.y == wall.y+1)):
                    wall.hpts -= troop.damage
                    ret_val = True
                    if wall.hpts <= 0:
                        wall.hpts = 0
                        wall.alive = False
                    break
        return ret_val

    def bar_attack(self, unfilled_blocks):
        
        for troop in self.troops:
            #print(troop.target_no)
            if troop.alive:
                if(troop.target_no <= 4):
                    if(self.huts[troop.target_no].alive == False):
                        troop.target_no = 100

                elif troop.target_no == 5 or troop.target_no == 6 or troop.target_no == 7 or troop.target_no == 8:
                    if(self.cannons[troop.target_no-5].alive == False):
                        troop.target_no = 100
                elif troop.target_no >=9 and troop.target_no <=12 :
                    if(self.towers[troop.target_no-9].alive == False):
                        troop.target_no = 100        
                elif troop.target_no == 13:
                    if(self.townhall.alive == False):
                        troop.target_no = 100

                if(troop.target_no == 100):
                    target_index = -1
                    min_distance = 10000
                    i = -1
                    for hut in self.huts:
                        i = i+1
                        if(hut.alive):
                            if(self.dist(troop.x, troop.y, hut.x, hut.y) < min_distance):
                                min_distance = self.dist(
                                    troop.x, troop.y, hut.x, hut.y)
                                target = hut
                                target_index = i
                    for cannon in self.cannons:
                        i = i+1
                        if(cannon.alive):
                            if(self.dist(troop.x, troop.y, cannon.x, cannon.y) < min_distance):
                                min_distance = self.dist(
                                    troop.x, troop.y, cannon.x, cannon.y)
                                target = cannon
                                target_index = i
                    for tower in self.towers:
                        i = i+1
                        if(tower.alive):
                            if(self.dist(troop.x, troop.y, tower.x, tower.y) < min_distance):
                                min_distance = self.dist(
                                    troop.x, troop.y, tower.x, tower.y)
                                target = tower
                                target_index = i                
                    if(self.townhall.alive):
                        for row in range(self.townhall.y, self.townhall.y+(self.townhall.height)):
                            for col in range(self.townhall.x, self.townhall.x+(self.townhall.width)):
                                if(self.dist(troop.x, troop.y, col, row) < min_distance):
                                    min_distance = self.dist(
                                        troop.x, troop.y, col, row)
                                    target = self.townhall
                                    target_index = 13
                                    break
                         
                    troop.target_no = target_index
                if(troop.target_no <= 12 and troop.target_no > -1 ):
                    if(troop.target_no <= 4):
                        target = self.huts[troop.target_no]

                    elif troop.target_no >= 5 and troop.target_no <= 8:
                        target = self.cannons[troop.target_no-5]
                    elif troop.target_no >= 9 and troop.target_no <= 12:
                        target = self.towers[troop.target_no-9]
                    if((troop.x == target.x-1 or troop.x == target.x+1) and (troop.y == target.y-1 or troop.y == target.y or troop.y == target.y+1)):
                        target.hpts = target.hpts-troop.damage
                        if(target.hpts <= 0):
                            target.hpts = 0
                            target.alive = False
                            troop.target_no = 100

                    elif(troop.x == target.x and (troop.y == target.y-1 or troop.y == target.y+1)):
                        target.hpts = target.hpts-troop.damage
                        if(target.hpts <= 0):
                            target.hpts = 0
                            target.alive = False
                            troop.target_no = 100
                    elif(troop.x > target.x and troop.y > target.y):
                        if(unfilled_blocks[troop.y-1][troop.x-1] == 1):
                            self.wall_barb(troop)
                        else:
                            troop.x += -1
                            troop.y += -1
                    elif(troop.x > target.x and troop.y < target.y):
                        if(unfilled_blocks[troop.y+1][troop.x-1] == 1):

                            if self.wall_barb(troop) == False:
                                troop.x += -1
                                troop.y += 1
                        else:
                            troop.x += -1
                            troop.y += 1
                    elif(troop.x < target.x and troop.y > target.y):
                        if(unfilled_blocks[troop.y-1][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += 1
                                troop.y += -1
                        else:
                            troop.x += 1
                            troop.y += -1
                    elif(troop.x < target.x and troop.y < target.y):
                        if(unfilled_blocks[troop.y+1][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += 1
                                troop.y += 1
                        else:
                            troop.x += 1
                            troop.y += 1
                    elif(troop.x == target.x and troop.y-1 > target.y):
                        if(unfilled_blocks[troop.y-1][troop.x] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += -1
                        else:
                            troop.y += -1
                    elif(troop.x == target.x and troop.y+1 < target.y):
                        if(unfilled_blocks[troop.y+1][troop.x] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += 1
                        else:
                            troop.y += 1
                    elif(troop.x > target.x+1 and troop.y == target.y):
                        if(unfilled_blocks[troop.y][troop.x-1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += -1
                        else:
                            troop.x += -1
                    elif(troop.x < target.x-1 and troop.y == target.y):
                        if(unfilled_blocks[troop.y][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += 1
                        else:
                            troop.x += 1

                if(troop.target_no == 13):
                    if(troop.y < self.townhall.y and troop.x > self.townhall.x+self.townhall.width):
                        if(unfilled_blocks[troop.y+1][troop.x-1] == 1):
                            self.wall_barb(troop)
                        else:
                            troop.y += 1
                            troop.x += -1

                    if(troop.y > self.townhall.y+self.townhall.height and troop.x < self.townhall.x):
                        if(unfilled_blocks[troop.y-1][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += -1
                                troop.x += 1
                        else:
                            troop.y += -1
                            troop.x += 1
                    if(troop.y > self.townhall.y+self.townhall.height and troop.x > self.townhall.x+self.townhall.width):
                        if(unfilled_blocks[troop.y-1][troop.x-1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += -1
                                troop.x += -1
                        else:
                            troop.y += - 1
                            troop.x += -1
                    if(troop.y < self.townhall.y and troop.x < self.townhall.x):
                        if(unfilled_blocks[troop.y+1][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += 1
                                troop.x += 1
                        else:
                            troop.y += 1
                            troop.x += 1

                    if(troop.y > self.townhall.y+self.townhall.height+1 and troop.x >= self.townhall.x and troop.x <= self.townhall.x+self.townhall.width):
                        if(unfilled_blocks[troop.y-1][troop.x] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += -1
                        else:
                            troop.y = troop.y-1
                    if(troop.y+1 < self.townhall.y and troop.x >= self.townhall.x and troop.x <= self.townhall.x+self.townhall.width):
                        if(unfilled_blocks[troop.y+1][troop.x] == 1):
                            if self.wall_barb(troop) == False:
                                troop.y += 1
                        else:
                            troop.y = troop.y+1
                    if(troop.y >= self.townhall.y and troop.y <= self.townhall.y+self.townhall.height and troop.x-1 > self.townhall.x+self.townhall.width):
                        if(unfilled_blocks[troop.y][troop.x-1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += -1
                        else:
                            troop.x = troop.x-1
                    if(troop.y >= self.townhall.y and troop.y <= self.townhall.y+self.townhall.height and troop.x+1 < self.townhall.x):
                        if(unfilled_blocks[troop.y][troop.x+1] == 1):
                            if self.wall_barb(troop) == False:
                                troop.x += 1
                        else:
                            troop.x = troop.x+1
                    if((troop.y == self.townhall.y-1 or troop.y == self.townhall.y+4) and (troop.x == self.townhall.x-1 or troop.x == self.townhall.x or troop.x == self.townhall.x+1 or troop.x == self.townhall.x+2 or troop.x == self.townhall.x+3)):
                        self.townhall.hpts -= troop.damage

                        if self.townhall.hpts <= 0:
                            self.townhall.alive = False
                            self.townhall.hpts = 0
                            troop.target_no = 100

                    elif((troop.x == self.townhall.x-1 or troop.x == self.townhall.x+3) and (troop.y == self.townhall.y-1 or troop.y == self.townhall.y or troop.y == self.townhall.y+1 or troop.y == self.townhall.y+2 or troop.y == self.townhall.y+3 or troop.y == self.townhall.y+4)):
                        self.townhall.hpts -= troop.damage

                        if self.townhall.hpts <= 0:
                            self.townhall.alive = False
                            self.townhall.hpts = 0
                            troop.target_no = 100

    def archer_attack(self, unfilled_blocks):
        for archer in self.archers:
            # print(archer.target_no)
            #target = self.huts[0]
            if archer.alive:
                if(archer.target_no <= 4):
                    if(self.huts[archer.target_no].alive == False):
                        archer.target_no = 100

                elif archer.target_no >= 5 and archer.target_no <= 8:
                    if(self.cannons[archer.target_no-5].alive == False):
                        archer.target_no = 100
                elif archer.target_no >= 9 and archer.target_no <= 12:
                    if self.towers[archer.target_no-9].alive == False:
                        archer.target_no = 100        
                elif archer.target_no == 13:
                    if(self.townhall.alive == False):
                        archer.target_no = 100

                if archer.target_no == 100:
                    min_distance = 10000
                    target_index = -1
                    i = -1
                    for hut in self.huts:
                        i = i+1
                        if(hut.alive):
                            if(self.dist(archer.x, archer.y, hut.x, hut.y) < min_distance):
                                min_distance = self.dist(
                                    archer.x, archer.y, hut.x, hut.y)
                                target = hut
                                target_index = i
                    for cannon in self.cannons:
                        i = i+1
                        if(cannon.alive):
                            if(self.dist(archer.x, archer.y, cannon.x, cannon.y) < min_distance):
                                min_distance = self.dist(
                                    archer.x, archer.y, cannon.x, cannon.y)
                                target = cannon
                                target_index = i
                    for tower in self.towers:
                        i = i+1
                        if(tower.alive):
                            if(self.dist(archer.x, archer.y, tower.x, tower.y) < min_distance):
                                min_distance = self.dist(
                                    archer.x, archer.y, tower.x, tower.y)
                                target = tower
                                target_index = i            
                    if self.townhall.alive:
                        for row in range(self.townhall.y, self.townhall.y+(self.townhall.height)):
                            for col in range(self.townhall.x, self.townhall.x+(self.townhall.width)):
                                if(self.dist(archer.x, archer.y, col, row) < min_distance):
                                    min_distance = self.dist(
                                        archer.x, archer.y, col, row)
                                    target = self.townhall
                                    target_index = 13
                                    break
                            if target_index == 13:
                                break    
                    archer.target_no = target_index
               
                if(archer.target_no <= 12 and archer.target_no > -1):
                    if(archer.target_no <= 4):
                        target = self.huts[archer.target_no]

                    elif archer.target_no >= 5 and archer.target_no <= 8:
                        target = self.cannons[archer.target_no-5]
                    elif archer.target_no >= 9 and archer.target_no <= 12:
                        target = self.towers[archer.target_no-9]    
                    if(target.alive):
                        if(self.dist(archer.x, archer.y, target.x, target.y) <= archer.range):
                            if(target.hpts > 0):
                                target.hpts -= archer.damage
                                if(target.hpts <= 0):
                                    target.alive = False
                                    target.hpts = 0
                                    archer.target_no = 100

                        else:
                            if archer.target_no <= 12 and archer.target_no > -1:
                                if(archer.x > target.x and archer.y > target.y):
                                    if(unfilled_blocks[archer.y-1][archer.x-1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += -1
                                            archer.x += -1
                                    else:
                                        archer.x += -1
                                        archer.y += -1
                                elif(archer.x > target.x and archer.y < target.y):

                                    if(unfilled_blocks[archer.y+1][archer.x-1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += 1
                                            archer.x += -1
                                    else:
                                        archer.x += -1
                                        archer.y += 1
                                elif(archer.x < target.x and archer.y > target.y):
                                    if(unfilled_blocks[archer.y-1][archer.x+1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += -1
                                            archer.x += 1

                                    else:
                                        archer.x += 1
                                        archer.y += -1
                                elif(archer.x < target.x and archer.y < target.y):

                                    if(unfilled_blocks[archer.y+1][archer.x+1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += 1
                                            archer.x += 1

                                    else:
                                        archer.x += 1
                                        archer.y += 1
                                elif(archer.x == target.x and archer.y-1 > target.y):
                                    if(unfilled_blocks[archer.y-1][archer.x] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += -1
                                    else:
                                        archer.y += -1
                                elif(archer.x == target.x and archer.y+1 < target.y):
                                    if(unfilled_blocks[archer.y+1][archer.x] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.y += 1

                                    else:
                                        archer.y += 1
                                elif(archer.x > target.x+1 and archer.y == target.y):
                                    if(unfilled_blocks[archer.y][archer.x-1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.x += -1
                                    else:
                                        archer.x += -1
                                elif(archer.x < target.x-1 and archer.y == target.y):
                                    if(unfilled_blocks[archer.y][archer.x+1] == 1):
                                        if self.wall_barb(archer) == False:
                                            archer.x += 1
                                    else:
                                        archer.x += 1
                if archer.target_no == 13:
                    if(self.townhall.alive):
                        t_range = False
                        for row in range(self.townhall.y, self.townhall.y+(self.townhall.height)):
                            for col in range(self.townhall.x, self.townhall.x+(self.townhall.width)):
                                if(self.dist(archer.x, archer.y, col, row) <= archer.range):
                                    t_range = True
                                    break
                            if t_range == True:
                                break    
                        if(t_range == True and self.townhall.hpts > 0):
                            self.townhall.hpts -= archer.damage
                            # print("\n",archer.damage)
                            if(self.townhall.hpts <= 0):
                                self.townhall.alive = False
                                self.townhall.hpts = 0
                                archer.target_no = 100
                        else:
                            # print("??")
                            if(archer.y < self.townhall.y and archer.x > self.townhall.x+self.townhall.width):
                                if(unfilled_blocks[archer.y+1][archer.x-1] == 1):
                                    self.wall_barb(archer)
                                else:
                                    archer.y += 1
                                    archer.x += -1

                            if(archer.y > self.townhall.y+self.townhall.height and archer.x < self.townhall.x):
                                if(unfilled_blocks[archer.y-1][archer.x+1] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.y += -1
                                        archer.x += 1
                                else:
                                    archer.y += -1
                                    archer.x += 1
                            if(archer.y > self.townhall.y+self.townhall.height and archer.x > self.townhall.x+self.townhall.width):
                                if(unfilled_blocks[archer.y-1][archer.x-1] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.y += -1
                                        archer.x += -1
                                else:
                                    archer.y += - 1
                                    archer.x += -1
                            if(archer.y < self.townhall.y and archer.x < self.townhall.x):
                                if(unfilled_blocks[archer.y+1][archer.x+1] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.y += 1
                                        archer.x += 1
                                else:
                                    archer.y += 1
                                    archer.x += 1

                            if(archer.y > self.townhall.y+self.townhall.height+1 and archer.x >= self.townhall.x and archer.x <= self.townhall.x+self.townhall.width):
                                if(unfilled_blocks[archer.y-1][archer.x] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.y += -1
                                else:
                                    archer.y = archer.y-1
                            if(archer.y+1 < self.townhall.y and archer.x >= self.townhall.x and archer.x <= self.townhall.x+self.townhall.width):
                                if(unfilled_blocks[archer.y+1][archer.x] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.y += 1
                                else:
                                    archer.y = archer.y+1
                            if(archer.y >= self.townhall.y and archer.y <= self.townhall.y+self.townhall.height and archer.x-1 > self.townhall.x+self.townhall.width):
                                if(unfilled_blocks[archer.y][archer.x-1] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.x += -1
                                else:
                                    archer.x = archer.x-1
                            if(archer.y >= self.townhall.y and archer.y <= self.townhall.y+self.townhall.height and archer.x+1 < self.townhall.x):
                                if(unfilled_blocks[archer.y][archer.x+1] == 1):
                                    if self.wall_barb(archer) == False:
                                        archer.x += 1
                                else:
                                    archer.x = archer.x+1

    def balloon_attack(self):
        for balloon in self.balloons:
            #print(balloon.target_no,"balloon target no1")
            if balloon.alive:
                if(balloon.target_no <= 4):
                    if(self.huts[balloon.target_no].alive == False):
                        balloon.target_no = 100

                elif balloon.target_no >= 5 and balloon.target_no <= 8:
                    if(self.cannons[balloon.target_no-5].alive == False):
                        balloon.target_no = 100 
                elif balloon.target_no >= 9 and balloon.target_no <= 12:
                    if(self.towers[balloon.target_no-9].alive == False):
                        balloon.target_no = 100
                elif balloon.target_no == 13:
                    if(self.townhall.alive == False):
                        balloon.target_no = 100
                if(balloon.target_no == 100):
                    def_found = False
                    min = 10000
                    i = -1
                    for cannon in self.cannons:
                        i = i+1
                        if cannon.alive:
                            def_found = True
                            if(self.dist(balloon.x, balloon.y, cannon.x, cannon.y) < min):
                                min = self.dist(
                                    balloon.x, balloon.y, cannon.x, cannon.y)
                                balloon.target_no = i+5
                    i=-1            
                    for tower in self.towers:
                        i=i+1
                        #print(tower.alive,i)
                        if tower.alive==True:
                            #print(i)
                            def_found = True
                            if(self.dist(balloon.x, balloon.y, tower.x, tower.y) < min):
                                min = self.dist(
                                    balloon.x, balloon.y, tower.x, tower.y)
                                balloon.target_no = i+9 
                                        

                    i = -1
                    if(def_found == False):
                        for hut in self.huts:
                            i = i+1
                            if hut.alive:
                                if(self.dist(balloon.x, balloon.y, hut.x, hut.y) < min):
                                    min = self.dist(
                                        balloon.x, balloon.y, hut.x, hut.y)
                                    balloon.target_no = i
                        if self.townhall.alive:
                            for row in range(self.townhall.y, self.townhall.y+(self.townhall.height)):
                                for col in range(self.townhall.x, self.townhall.x+(self.townhall.width)):
                                    if(self.dist(balloon.x, balloon.y, col, row) < min):
                                        min = self.dist(
                                            balloon.x, balloon.y, col, row)
                                        balloon.target_no = 13
                #print(balloon.target_no, "\n")
                if balloon.target_no <=12 and balloon.target_no > -1:
                    if(balloon.target_no <= 4):
                        target = self.huts[balloon.target_no]

                    elif balloon.target_no >= 5 and balloon.target_no <= 8:
                        target = self.cannons[balloon.target_no-5]
                    elif balloon.target_no >= 9 and balloon.target_no <= 12:
                        target = self.towers[balloon.target_no-9]

                    if target.alive:
                        if balloon.x == target.x and balloon.y == target.y:
                            target.hpts -= balloon.damage
                            if target.hpts <= 0:
                                target.hpts = 0
                                target.alive = False
                                
                                balloon.target_no = 100
                        elif balloon.x > target.x and balloon.y > target.y:
                            balloon.x -= 1
                            balloon.y -= 1
                        elif balloon.x > target.x and balloon.y < target.y:
                            balloon.x -= 1
                            balloon.y += 1
                        elif balloon.x < target.x and balloon.y > target.y:
                            balloon.x += 1
                            balloon.y -= 1
                        elif balloon.x < target.x and balloon.y < target.y:
                            balloon.x += 1
                            balloon.y += 1
                        elif balloon.x == target.x and balloon.y > target.y:
                            balloon.y -= 1
                        elif balloon.x == target.x and balloon.y < target.y:
                            balloon.y += 1
                        elif balloon.x > target.x and balloon.y == target.y:
                            balloon.x -= 1
                        elif balloon.x < target.x and balloon.y == target.y:
                            balloon.x += 1

                if balloon.target_no == 13:
                    if balloon.x >= self.townhall.x and balloon.x < self.townhall.x+self.townhall.width and balloon.y >= self.townhall.y and balloon.y < self.townhall.y+self.townhall.height:
                        self.townhall.hpts -= balloon.damage
                        if self.townhall.hpts <= 0:
                            self.townhall.hpts = 0
                            self.townhall.alive = False
                            balloon.target_no = 100
                    elif balloon.x >= self.townhall.x+self.townhall.width and balloon.y < self.townhall.y:
                        balloon.x -= 1
                        balloon.y += 1
                    elif balloon.x < self.townhall.x and balloon.y < self.townhall.y:
                        balloon.x += 1
                        balloon.y += 1
                    elif balloon.x < self.townhall.x and balloon.y >= self.townhall.y+self.townhall.height:
                        balloon.x += 1
                        balloon.y -= 1
                    elif balloon.x >= self.townhall.x+self.townhall.width and balloon.y >= self.townhall.y+self.townhall.height:
                        balloon.x -= 1
                        balloon.y -= 1
                    elif balloon.x >= self.townhall.x and balloon.x < self.townhall.x+self.townhall.width and balloon.y < self.townhall.y:
                        balloon.y += 1
                    elif balloon.x >= self.townhall.x and balloon.x < self.townhall.x+self.townhall.width and balloon.y >= self.townhall.y+self.townhall.height:
                        balloon.y -= 1
                    elif balloon.x < self.townhall.x and balloon.y >= self.townhall.y and balloon.y < self.townhall.y+self.townhall.height:
                        balloon.x += 1
                    elif balloon.x >= self.townhall.x+self.townhall.width and balloon.y >= self.townhall.y and balloon.y < self.townhall.y+self.townhall.height:
                        balloon.x -= 1

                

    def render(self, file_name,queen_or_king):
        # print("Level ",self.level)
        if queen_or_king=='q' and self.qchange==False:
            self.king.damage=25
        #     self.king.x=10
        #     self.king.y=11
        system('clear')
       # print(self.townhall.hpts)
        i = 0
        for troop in self.troops:
            if(troop.alive):
                i = i+1
        #print(len(self.balloons))
        for tower in self.towers:
            if(tower.alive):
                # print("Tower: ", tower.x, tower.y, tower.hpts)
                i = i+1
        for balloon in self.balloons:
            if(balloon.alive):
                # print("Balloon: ", balloon.x, balloon.y, balloon.hpts)
                i = i+1  
        # print(self.king.x,self.king.y)
        # for tower in self.towers:
            # print(tower.attacking_on)
        if(time()-self.rage_start_time < self.rage_time):

            self.board = [[Back.LIGHTGREEN_EX+' ' +
                           Style.RESET_ALL for i in range(self.cols)] for j in range(self.rows)]
        else:
            self.board = [[self.bg_pixel for i in range(
                self.cols)] for j in range(self.rows)]

        for row in range(self.rows-10, self.rows):
            for col in range(self.cols):
                self.board[row][col] = Back.LIGHTYELLOW_EX+' '+Style.RESET_ALL



        king_hpt = "King HP: " + str(self.king.hpts)
        if queen_or_king=='q':
            king_hpt = "Queen HP: " + str(self.king.hpts)   


        lev="Level " + str(self.level)
        for j in range(10, 10+len(king_hpt)):
            self.board[53][j] = Back.BLUE+Fore.RED + \
                king_hpt[j-10]+Style.RESET_ALL
        for j in range(10, 10+len(lev)):
            self.board[51][j]  = Back.BLUE+Fore.RED +lev[j-10]+Style.RESET_ALL 

        king_level = self.king.hpts//10
        for j in range(10, king_level+10):
            self.board[55][j] = Back.RED+' '+Style.RESET_ALL

     # GAME OVER
        game_over1 = True
        if self.townhall.alive:
            game_over1 = False

        for hut in self.huts:
            if hut.alive:
                game_over1 = False
                break

        for cannon in self.cannons:
            if(cannon.alive):
                game_over1 = False
        for tower in self.towers:
            if(tower.alive):
                game_over1 = False        
        game_over2 = True
        if self.king.alive:
            
            game_over2 = False

        for troop in self.troops:
            if troop.alive:
                
                game_over2 = False
                break
        for archer in self.archers:
            if archer.alive:
                game_over2 = False
                break
        for balloon in self.balloons:    
            if balloon.alive:
                game_over2 = False
                break
        game_over_string = "Game over !"
        vic = "Victory !"
        def_ = "Defeat !"
        
        
        
        
        
        
        if(game_over2):

            game_over_screen_width = self.cols//2
            game_over_offset = (game_over_screen_width -
                                len(game_over_string)) // 2
            for j in range(0, len(game_over_string)):
                self.board[25][game_over_offset+j] = Back.BLUE + \
                    Fore.RED+game_over_string[j]+Style.RESET_ALL
            for j in range(0, len(def_)):
                self.board[26][game_over_offset+j] = Back.BLUE + \
                    Fore.RED+def_[j]+Style.RESET_ALL
            #exit()            
                   
        if(game_over1):
            #print(len(self.troops),"\n")

            if self.level==1:
                
                self.king.alive=True
                self.king.hpts=self.king.Mhpts
                self.king.x=5
                self.king.y=6
                self.troops.clear()
                self.archers.clear()
                self.balloons.clear()
                for hut in self.huts:
                    hut.alive=True
                    hut.hpts=hut.Mhpts
                self.townhall.alive=True
                self.townhall.hpts=self.townhall.Mhpts
                for wall in self.walls:
                    wall.alive=True
                    wall.hpts=wall.Mhpts
                self.cannons[0].alive=True
                self.cannons[0].hpts=self.cannons[0].Mhpts
                self.cannons[0].attacking_on=100
                self.cannons[1].alive=True
                self.cannons[1].hpts=self.cannons[1].Mhpts
                self.cannons[1].attacking_on=100
                self.cannons[2].alive=True
                self.cannons[2].hpts=self.cannons[2].Mhpts
                self.cannons[2].attacking_on=100

                self.towers[0].alive=True
                self.towers[0].hpts=self.towers[0].Mhpts
                self.towers[0].attacking_on=100
                self.towers[1].alive=True
                self.towers[1].hpts=self.towers[1].Mhpts
                self.towers[1].attacking_on=100
                self.towers[2].alive=True
                self.towers[2].hpts=self.towers[2].Mhpts
                self.towers[2].attacking_on=100
                #print(len(self.troops))
            elif self.level==2:
                
                self.king.alive=True
                self.king.hpts=self.king.Mhpts
                self.king.x=5
                self.king.y=6
                self.troops.clear()
                self.archers.clear()
                self.balloons.clear()
                for hut in self.huts:
                    hut.alive=True
                    hut.hpts=hut.Mhpts
                self.townhall.alive=True
                self.townhall.hpts=self.townhall.Mhpts
                for wall in self.walls:
                    wall.alive=True
                    wall.hpts=wall.Mhpts
                self.cannons[0].alive=True
                self.cannons[0].hpts=self.cannons[0].Mhpts
                self.cannons[0].attacking_on=100
                self.cannons[1].alive=True
                self.cannons[1].hpts=self.cannons[1].Mhpts
                self.cannons[1].attacking_on=100
                self.cannons[2].alive=True
                self.cannons[2].hpts=self.cannons[2].Mhpts
                self.cannons[2].attacking_on=100
                self.cannons[3].alive=True
                self.cannons[3].hpts=self.cannons[3].Mhpts
                self.cannons[3].attacking_on=100

                self.towers[0].alive=True
                self.towers[0].hpts=self.towers[0].Mhpts
                self.towers[0].attacking_on=100
                self.towers[1].alive=True
                self.towers[1].hpts=self.towers[1].Mhpts
                self.towers[1].attacking_on=100
                self.towers[2].alive=True
                self.towers[2].hpts=self.towers[2].Mhpts
                self.towers[2].attacking_on=100
                self.towers[3].alive=True
                self.towers[3].hpts=self.towers[3].Mhpts
                self.towers[3].attacking_on=100


            elif self.level==3:
                game_over_screen_width = self.cols//2
                game_over_offset = (game_over_screen_width -
                                    len(game_over_string)) // 2
                for j in range(0, len(game_over_string)):
                    self.board[25][game_over_offset+j] = Back.BLUE + \
                        Fore.RED+game_over_string[j]+Style.RESET_ALL
                for j in range(0, len(vic)):
                    self.board[26][game_over_offset+j] = Back.BLUE + \
                        Fore.RED+vic[j]+Style.RESET_ALL
               # exit()        
        
            self.level=self.level+1
                ##########################
             
        self.unfilled_blocks = [
            [0 for i in range(self.cols)] for j in range(self.rows)]

        if(self.king.alive):
            if(self.king.hpts > self.king.Mhpts//2):
                self.board[self.king.y][self.king.x] = self.king.pixel1
            elif(self.king.hpts <= self.king.Mhpts//2 and self.king.hpts > self.king.Mhpts//5):
                self.board[self.king.y][self.king.x] = self.king.pixel2
            else:
                self.board[self.king.y][self.king.x] = self.king.pixel3
            self.unfilled_blocks[self.king.y][self.king.x] = 1
        if(self.townhall.alive):
            for row in range(self.townhall.y, self.townhall.y+self.townhall.height):
                for col in range(self.townhall.x, self.townhall.x+self.townhall.width):

                    if self.townhall.hpts > self.townhall.Mhpts//2:
                        self.board[row][col] = self.townhall.pixel1
                    elif self.townhall.hpts <= self.townhall.Mhpts//2 and self.townhall.hpts > self.townhall.Mhpts//5:
                        self.board[row][col] = self.townhall.pixel2
                    else:
                        self.board[row][col] = self.townhall.pixel3
                    self.unfilled_blocks[row][col] = 1

        for hut in self.huts:
            if hut.alive:
                for row in range(hut.y, hut.y+(hut.height)):
                    for col in range(hut.x, hut.x+(hut.width)):
                        if hut.hpts > hut.Mhpts//2:
                            self.board[row][col] = hut.pixel1
                        elif hut.hpts <= hut.Mhpts//2 and hut.hpts > hut.Mhpts//5:
                            self.board[row][col] = hut.pixel2
                        else:
                            self.board[row][col] = hut.pixel3

                        self.unfilled_blocks[row][col] = 1

        for wall in self.walls:
            if wall.alive:
                for row in range(wall.y, wall.y+(wall.height)):
                    for col in range(wall.x, wall.x+(wall.width)):
                        if wall.hpts > wall.Mhpts//2:
                            self.board[row][col] = wall.pixel1
                        elif wall.hpts <= wall.Mhpts//2 and wall.hpts > wall.Mhpts//5:
                            self.board[row][col] = wall.pixel2
                        else:
                            self.board[row][col] = wall.pixel3
                        self.unfilled_blocks[row][col] = 1

        for troop in self.troops:
            if troop.alive:
                for row in range(troop.y, troop.y+(troop.height)):
                    for col in range(troop.x, troop.x+(troop.width)):
                        if troop.hpts > troop.Mhpts//2:
                            self.board[row][col] = troop.pixel1
                        elif troop.hpts <= troop.Mhpts//2 and troop.hpts > troop.Mhpts//5:
                            self.board[row][col] = troop.pixel2
                        else:
                            self.board[row][col] = troop.pixel3
                        self.unfilled_blocks[row][col] = 1

            # print(troop.hpts)

        for archer in self.archers:
            if archer.alive:
                # print(archer.target_no)

                if archer.hpts > archer.Mhpts//2:
                    self.board[archer.y][archer.x] = archer.pixel1
                elif archer.hpts <= archer.Mhpts//2 and archer.hpts > archer.Mhpts//5:
                    self.board[archer.y][archer.x] = archer.pixel2
                else:
                    self.board[archer.y][archer.x] = archer.pixel3
                self.unfilled_blocks[archer.y][archer.x] = 1

        for balloon in self.balloons:
            if balloon.alive:
                if balloon.hpts > balloon.Mhpts//2:
                    self.board[balloon.y][balloon.x] = balloon.pixel1
                elif balloon.hpts <= balloon.Mhpts//2 and balloon.hpts > balloon.Mhpts//5:
                    self.board[balloon.y][balloon.x] = balloon.pixel2
                else:
                    self.board[balloon.y][balloon.x] = balloon.pixel3
                self.unfilled_blocks[balloon.y][balloon.x] = 1

        if time() - self.start_time_2 >= 0.5: 
            for tower in self.towers:
                self.tower_attack(tower)
            self.start_time_2 = time()
        else:
            for tower in self.towers:
                if tower.alive:
                    if tower.hpts > tower.Mhpts//2:
                        self.board[tower.y][tower.x] = tower.pixel1
                    elif tower.hpts <= tower.Mhpts//2 and tower.hpts > tower.Mhpts//5:
                        self.board[tower.y][tower.x] = tower.pixel2
                    else:
                        self.board[tower.y][tower.x] = tower.pixel3
                    self.unfilled_blocks[tower.y][tower.x] = 1      

        if(time()-self.start_time >= 0.5):
            for cannon in self.cannons:
                self.cannon_attack(cannon)
            self.start_time = time()
        else:
            for cannon in self.cannons:
                if cannon.alive:
                    for row in range(cannon.y, cannon.y+(cannon.height)):
                        for col in range(cannon.x, cannon.x+(cannon.width)):
                            if cannon.hpts > cannon.Mhpts//2:

                                self.board[row][col] = cannon.pixel1
                            elif cannon.hpts <= cannon.Mhpts//2 and cannon.hpts > cannon.Mhpts//5:
                                self.board[row][col] = cannon.pixel3
                            else:
                                self.board[row][col] = cannon.pixel4
                            self.unfilled_blocks[row][col] = 1

        if(time()-self.rage_start_time < self.rage_time):
            if(time()-self.start_time_bar >= 0.25):
                self.bar_attack(self.unfilled_blocks)
                self.start_time_bar = time()

      
        else:
            if(time()-self.start_time_bar >= 0.5):
                self.bar_attack(self.unfilled_blocks)
                self.start_time_bar = time()
           
        if (time()-self.rage_start_time<self.rage_time):
            if(time()-self.start_time_arch >= 0.125):
                self.archer_attack(self.unfilled_blocks)
                self.start_time_arch = time()
        else:
            if(time()-self.start_time_arch >= 0.25):
                self.archer_attack(self.unfilled_blocks)
                self.start_time_arch = time()        
         
        if (time()-self.rage_start_time<self.rage_time):
            if(time()-self.start_time_balloon >= 0.125):
                self.balloon_attack()
                self.start_time_balloon = time()
        else:
            if(time()-self.start_time_balloon >= 0.25):
                self.balloon_attack()
                self.start_time_balloon = time() 

        # print(time()-self.mtime)    
        # print(self.king.x,self.king.y)    
        # print("prev",self.queen_x,self.queen_y)   

        if time()-self.mtime>=1 and self.mattack==True:
            #print("hmm")
            self.queen_shoot2(self.queen_prev,self.queen_x,self.queen_y)
            self.mattack=False


        print("\n".join(["".join(row) for row in self.board]))
        file = open(file_name, "a")
        file.write("\n".join(["".join(row) for row in self.board]))
        file.write("\n")
        file.close()

        if((game_over1 and self.level==3 )or game_over2):
            exit()

    def take_input(self, cha, queen_or_king):
        
        
        if(time()-self.rage_start_time < self.rage_time):
            if cha == 'w':
                self.queen_prev = cha
                self.king.move_up(self.unfilled_blocks)
                self.king.move_up(self.unfilled_blocks)

            elif cha == 's':
                self.queen_prev = cha
                self.king.move_down(self.unfilled_blocks)
                self.king.move_down(self.unfilled_blocks)
            elif cha == 'a':
                self.queen_prev = cha
                self.king.move_left(self.unfilled_blocks)
                self.king.move_left(self.unfilled_blocks)
            elif cha == 'd':
                self.queen_prev = cha
                self.king.move_right(self.unfilled_blocks)
                self.king.move_right(self.unfilled_blocks)
            self.king.damage = 60
            for troop in self.troops:
                troop.damage = 10
            for archer in self.archers:
                archer.damage = 5
            for  balloon in self.balloons:
                balloon.damage = 20    
        else:
            if cha == 'w':
                self.queen_prev = cha
                self.king.move_up(self.unfilled_blocks)
            elif cha == 's':
                self.queen_prev = cha
                self.king.move_down(self.unfilled_blocks)
            elif cha == 'a':
                self.queen_prev = cha
                self.king.move_left(self.unfilled_blocks)
            elif cha == 'd':
                self.queen_prev = cha
                self.king.move_right(self.unfilled_blocks)
            if queen_or_king=='k':
                self.king.damage = 30
            else:
                self.king.damage=25   
            for troop in self.troops:
                troop.damage = 5
            for archer in self.archers:
                archer.damage = 2.5
            for balloon in self.balloons:
                balloon.damage = 10        

        if cha == 'i':
            self.build_troops(6, 9)
        elif cha == 'j':
            self.build_troops(10, 45)
        elif cha == 'k':
            self.build_troops(20, 10)

        elif cha == 'c':
            self.build_archer(60, 38)

        elif cha == 'v':
            self.build_archer(69, 18)

        elif cha == 'b':
            self.build_archer(30, 27)
        elif cha == 't':
            self.build_balloon(55, 15)
        elif cha == 'y':
            self.build_balloon(72, 35)

        elif cha == 'u':
            self.build_balloon(26, 4)
        elif cha == 'h':

            self.king.hpts = (self.king.hpts*3)//2
            if(self.king.hpts > 200):
                self.king.hpts = 200
            for troop in self.troops:
                troop.hpts = (troop.hpts*3)//2
                if(troop.hpts > troop.Mhpts):
                    troop.hpts = troop.Mhpts
            for archer in self.archers:
                archer.hpts = (archer.hpts*3)//2
                if(archer.hpts > archer.Mhpts):
                    archer.hpts = archer.Mhpts
            for balloon in self.balloons:
                balloon.hpts = (balloon.hpts*3)//2
                if(balloon.hpts > balloon.Mhpts):
                    balloon.hpts = balloon.Mhpts                
        elif cha == 'l':
            self.leviathan()
        elif cha == 'r':
            self.rage_start_time = time()
        elif cha == ' ':
            if queen_or_king == 'k':
                self.king_shoot()
            if queen_or_king == 'q':
                self.queen_shoot(self.queen_prev)

        elif cha=='m' and queen_or_king=='q':
            #print("hmm1")
            self.queen_x=self.king.x
            self.queen_y=self.king.y
            self.mattack=True
            self.mtime=time()
            
                
