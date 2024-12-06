from enum import Enum

size = (0,0)

class Guard:
    def __init__(self,location,direction, onpatrol = True):
        self.start = location
        self.location = location
        self.direction = direction
        self.onpatrol = onpatrol
        self.visits = set()

    def visit(self, location, direction) -> bool:
        self.location = location
        t = (location, direction)
        if t in self.visits: return True
        else: 
            self.visits.add((location, direction))
            return False
    
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
     if 0 <= location[0] <= size[0] and 0 <= location[1] <= size[1]: return True 


with open('AoC 2024/Input/Day6Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))
    obstacles = set()
    visited = set()
    loops = 0

    for y,line in enumerate(file):
        if "^" in line: 
            guard = Guard((line.find("^"), y), Direction.N)
            guard.visit(guard.location, guard.location)
        obstacles.update({(x,y) for x, letter in enumerate(line) if letter == "#"})
    
    while guard.onpatrol:
        visited.add(guard.location)
        loc = guard.walk()
        if loc in obstacles: guard.rotate()
        else: guard.location = loc

        if not(inbounds(guard.location)): guard.onpatrol = False
    
    visited.remove(guard.start)
    for possibility in visited:
        newobs = obstacles.copy()
        newobs.add(possibility)
        
        guard = Guard(guard.start, Direction.N)
        isloop = False
        while guard.onpatrol and not(isloop):
            loc = guard.walk()
            if loc in newobs: guard.rotate()
            else: 
                isloop = guard.visit(loc,guard.direction)
            if not(inbounds(guard.location)): guard.onpatrol = False

        if isloop: loops += 1

    print(loops)