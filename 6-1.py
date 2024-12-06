from enum import Enum

size = (0,0)

class Guard:
    def __init__(self,location,direction, onpatrol = True):
        self.location = location
        self.direction = direction
        self.onpatrol = onpatrol
    
    def rotate(self):
        if self.direction == Direction.N: self.direction = Direction.E
        elif self.direction == Direction.E: self.direction = Direction.S
        elif self.direction == Direction.S: self.direction = Direction.W
        elif self.direction == Direction.W: self.direction = Direction.N
    
    def walk(self) -> tuple:
        if self.direction == Direction.N: return north(self.location)
        elif self.direction == Direction.E: return east(self.location)
        elif self.direction == Direction.S: return south(self.location)
        elif self.direction == Direction.W: return west(self.location)

class Direction(Enum):
     N = 0
     E = 2
     S = 4
     W = 6

def north(location: tuple): return (location[0], location[1] - 1)
def south(location: tuple): return (location[0], location[1] + 1)
def east(location: tuple): return (location[0] + 1, location[1])
def west(location: tuple): return (location[0] - 1, location[1])
def inbounds(location: tuple):  
     if location[0] in range(0,size[0]) and location[1] in range(0,size[1]): return True 


with open('AoC 2024/Input/Day6Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))
    guard = Guard((0,0), Direction.N)
    obstacles = []
    visited = set()

    for y,line in enumerate(file):
        if "^" in line: guard.location = (line.find("^"), y)
        obstacles += [(x,y) for x, letter in enumerate(line) if letter == "#"]
    
    while guard.onpatrol:
        visited.add(guard.location)
        loc = guard.walk()
        if loc in obstacles:
            guard.rotate()
        else: guard.location = loc

        if not(inbounds(guard.location)): guard.onpatrol = False

    print(len(visited))