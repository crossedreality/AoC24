from enum import Enum

class Robot:
    def __init__(self,location):
        self.location = location

class Direction(Enum):
     N = 0
     E = 2
     S = 4
     W = 6

map = {}
robot = Robot((0,0))

def north(location: tuple) -> tuple: return (location[0], location[1] - 1)
def south(location: tuple) -> tuple: return (location[0], location[1] + 1)
def east(location: tuple) -> tuple: return (location[0] + 1, location[1])
def west(location: tuple) -> tuple: return (location[0] - 1, location[1])
def getnext(location: tuple, direction: Direction) -> tuple:
    if direction == Direction.N: return north(location)
    elif direction == Direction.S: return south(location)
    elif direction == Direction.E: return east(location)
    elif direction == Direction.W: return west(location)

def move(location: tuple, direction: Direction, obj: str):
    destination = getnext(location, direction)
    if canmove(destination,direction):
        if map[destination] == "[" and (direction == Direction.N or direction == Direction.S):
            move(destination,direction,"[")
            move(east(destination),direction,"]")
        elif map[destination] == "[" and (direction == Direction.W or direction == Direction.E):
            move(destination,direction,"[")
        elif map[destination] == "]" and (direction == Direction.N or direction == Direction.S):
            move(destination,direction,"]")
            move(west(destination),direction,"[")
        elif map[destination] == "]" and (direction == Direction.W or direction == Direction.E):
            move(destination,direction,"]")       
        map[destination] = obj
        map[location] = "."
        if obj == "@": robot.location = destination

def canmove(location: tuple, direction: Direction) -> bool:
    obj = map.get(location)
    if obj:
        if obj == "#": return False
        elif obj == "[":
            if direction == Direction.N:
                if canmove(north(location), direction) and canmove(north(east(location)), direction): return True
                else: return False
            elif direction == Direction.S:
                if canmove(south(location), direction) and canmove(south(east(location)), direction): return True
                else: return False
            elif direction == Direction.E: return canmove(east(location), direction)
            elif direction == Direction.W: return canmove(west(location), direction)
        elif obj == "]":
            if direction == Direction.N:
                if canmove(north(location), direction) and canmove(north(west(location)), direction): return True
                else: return False
            elif direction == Direction.S:
                if canmove(south(location), direction) and canmove(south(west(location)), direction): return True
                else: return False
            elif direction == Direction.E: return canmove(east(location), direction)
            elif direction == Direction.W: return canmove(west(location), direction)
        elif obj == ".": return True
    else: return False

with open('AoC 2024/Input/Day15Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))
    moves = ''

    for y,line in enumerate(file):
        if not(line.strip()): continue
        elif line[:1] in ["<",">","^","v"]: moves = line
        else:
            x = 0
            for c in line:
                match c:
                    case "#":
                        map[(x,y)] = "#"
                        map[(x+1,y)] = "#"
                    case "O":
                        map[(x,y)] = "["
                        map[(x+1,y)] = "]"
                    case ".":
                        map[(x,y)] = "."
                        map[(x+1,y)] = "."
                    case "@":
                        map[(x,y)] = "@"
                        map[(x+1,y)] = "."
                if c == "@": robot.location = (x,y)
                x += 2

    for m in moves:
        match m: #Oh hey, Python added switch (match) statements!
            case "^": move(robot.location,Direction.N,"@")
            case "v": move(robot.location,Direction.S,"@")
            case ">": move(robot.location,Direction.E,"@")
            case "<": move(robot.location,Direction.W,"@")

    gps = 0
    for key,value in map.items():
        if value == "[": gps += (100 * key[1]) + key[0]

    print(gps)