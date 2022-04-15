from colorama import Fore, Back, Style
from os import system
from time import sleep, time
import math
from src.buildings import *


class King:
    def __init__(self, x, y,health,damage):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.Mhpts = health
        self.hpts = health
        self.damage = damage
        self.speed = 1
        self.alive = True
        self.pixel1 = Back.MAGENTA+' '+Style.RESET_ALL
        self.pixel2 = Back.LIGHTBLUE_EX+' '+Style.RESET_ALL
        self.pixel3 = Back.LIGHTCYAN_EX+' '+Style.RESET_ALL

    def move_up(self, unfilled_blocks):
        #print("up1")
        if self.y-1 >= 0 and unfilled_blocks[self.y-1][self.x] == 0:
            self.y -= 1
            return True
        return False

    def move_down(self, unfilled_blocks):
        if self.y+1 < 50 and unfilled_blocks[self.y+1][self.x] == 0:
            self.y += 1
            return True
        return False

    def move_left(self, unfilled_blocks):
        if self.x-1 >= 0 and unfilled_blocks[self.y][self.x-1] == 0:
            self.x -= 1
            return True
        return False

    def move_right(self, unfilled_blocks):
        if self.x+1 < 100 and unfilled_blocks[self.y][self.x+1] == 0:
            self.x += 1
            return True
        return False

        
