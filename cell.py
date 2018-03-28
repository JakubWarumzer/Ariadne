from enum import Enum

class Direction(Enum):
    NORTH = 'N'
    EAST = 'E'
    WEST = 'W'
    SOUTH = 'S'

    def opposite(self):
        #Using dictionary mapping as a switch case
        oppositeSwitch = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.WEST: Direction.EAST,
            Direction.EAST: Direction.WEST,
        }

        return oppositeSwitch[self]
    
    #Returning shift coordinates on a grid according to direction
    def shift_coordinates(self):
        shiftSwitch = {
            Direction.NORTH: (-1,0),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0,-1),
            Direction.EAST: (0, 1),
        }

        return shiftSwitch[self]

class Border(Enum):
    PASSAGE = 0
    WALL = 1    

class Cell:
    def __init__(self):
        self.borders = {Direction.NORTH: Border.WALL,
                        Direction.EAST: Border.WALL,
                        Direction.WEST: Border.WALL,
                        Direction.SOUTH: Border.WALL}
        
        self.visited = False

    def carve_passage(self, direction):
        if direction not in self.borders:
            raise ValueError('Invalid direction. Accepted values: North, East, West, South from Direction enum.')
        else:
            self.borders[direction] = Border.PASSAGE