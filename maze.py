from enum import Enum
import random

class Border(Enum):
    PASSAGE = 0
    WALL = 1

class Cell:
    def __init__(self):
        self.borders = {'N': Border.Wall,
                        'E': Border.Wall,
                        'W': Border.Wall,
                        'S': Border.Wall}

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
        self.area = [[Cell()]*self.width for i in range(self.height)]
        
        #Then, we pick Entry and Exit
        self.entry = 0, random.randint(1, self.width - 2)
        self.exit = self.width - 1, random.randint(1, self.width - 2)

        self.create_passage(self.entry)
        self.create_passage(self.exit)

        #Now, we can create random web of passage between Entry and Exit

    def check_if_border_wall(self, point):
        if point[0] == 0 or point[0] == self.height - 1: return True
        if point[1] == 0 or point[1] == self.width - 1: return True

        return False


    def create_passage(self, point):
        self.area[point[0]][point[1]] = SpotType.PASSAGE

    def display(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.area[i][j].value, end='') #'end' argument ensures that there is no newline printed
            print('\n')