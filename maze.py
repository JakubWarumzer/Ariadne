import random
import time
import os
from cell import Cell, Direction, Border  

class Maze:
    def __init__(self, width, height):
        if (width < 8):
            raise ValueError('Height of the maze has to be greater than 3.')
        
        if (height < 8):
            raise ValueError('Width of the maze has to be greater than 3.')

        self.width = width
        self.height = height
       
        #For convinience, we use dictionary as a two-dimensional array substitute
        self.area = {} 

        self.generate()

    #Function used to initialize area
    def generate(self):
        #At first, we fill labirynth with grid of cells with complete borders
        for i in range(self.height):
            for j in range(self.width):
                self.area[i,j] = Cell()

        #Now, we can create random web of passages from starting point
        starting_point = 0, 0
        self.create_passages(starting_point)

    #Implementation of recursive backtracking algorithm 
    def create_passages(self, point):
        #Randomizing direction frees us from bias 
        directions = list(Direction)
        random.shuffle(directions)

        for direction in directions:
            #Adjusting current point coordinates for potential shift
            shifted_point = tuple([sum(x) for x in zip(point, direction.shift_coordinates())])

            #We want to proceed only if shifted point is in area's bound
            try:
                if self.area[shifted_point].visited: continue
                else:
                    #animating creation
                    self.display()
                    
                    #we don't want to come back to this cell in the future
                    self.area[shifted_point].visited = True

                    self.area[point].carve_passage(direction)
                    self.area[shifted_point].carve_passage(direction.opposite())

                    self.create_passages(shifted_point)
            except KeyError:
                continue


    def display(self):
        os.system('clear')

        #Upper border, always solid
        for i in range(self.width):
            print(" _", end='')
        
        
        #Then we display borders for each cell
        for i in range(self.height):
            print('')
            
            for j in range(self.width):
                print('|', end='') if self.area[i,j].borders[Direction.WEST] == Border.WALL else print(' ', end='')
                print('_', end='') if self.area[i,j].borders[Direction.SOUTH] == Border.WALL else print(' ', end='')

                if j == self.width - 1: print('|', end='')         

        print('')

        #short sleep for animation's sake
        time.sleep(.01)
