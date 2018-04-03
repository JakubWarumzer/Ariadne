from cell import Direction, Cell, Border
import random

#Class used to solve maze, that is find shortest path from entry to exit
class Ariadne:
    def __init__(self, maze):
        self.path = []
        self.maze = maze
        self.find_path()

    #Function used to generate list of points leading from start to exit
    def find_path(self):
        self.traverse_labirynth(self.maze.entrance, [])

    def traverse_labirynth(self, point, path):
        self.maze.area[point].visited = True
        
        path.append(point)
        self.maze.display(path)

        if point == self.maze.exit: 
            self.path = path
            return True

        #Randomizing direction frees us from bias 
        directions = list(Direction)
        random.shuffle(directions)

        for direction in directions:
            #Checking if there's passage in chosen direction
            if self.maze.area[point].borders[direction] == Border.WALL: continue
            
            #Adjusting current point coordinates for potential shift
            shifted_point = tuple([sum(x) for x in zip(point, direction.shift_coordinates())])

            #We want to proceed only if shifted point is in area's bound
            try:
                if self.maze.area[shifted_point].visited: continue
                else:                    
                    if self.traverse_labirynth(shifted_point, path.copy()): return True


            except KeyError:
                continue
