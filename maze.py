from enum import Enum
import random


class Border(Enum):
    PASSAGE = 0
    WALL = 1

class Cell:
    def __init__(self):
        self.borders = {'N': Border.WALL,
                        'E': Border.WALL,
                        'W': Border.WALL,
                        'S': Border.WALL}

    def carve_passage(self, direction):
        if direction not in self.borders:
            raise ValueError('Direction has to be N, E, W or S.')
        else:
            self.borders[direction] = Border.PASSAGE
    

class Maze:
    def __init__(self, width, height):
        if (width < 8):
            raise ValueError('Height of the maze has to be greater than 3.')
        
        if (height < 8):
            raise ValueError('Width of the maze has to be greater than 3.')

        self.width = width
        self.height = height

        self.generate()


    def generate(self):
        #At first, we fill labirynth with walls
        self.area = [[Cell() for i in range(self.width)] for i in range(self.height)]
        
    def create_passage(self, point):
        self.area[point[0]][point[1]] = Border.PASSAGE

    def display(self):
        #Upper border, always solid
        for i in range(self.width):
            print(" _", end='')
        
        
        #Then we display borders for each cell
        for i in range(self.height):
            print('')
            
            for j in range(self.width):
                print('|', end='') if self.area[i][j].borders['W'] == Border.WALL else print(' ', end='')
                print('_', end='') if self.area[i][j].borders['S'] == Border.WALL else print(' ', end='')

                if j == self.width - 1: print('|', end='')         