from enum import Enum

class XMAS(Enum):
    X = 0
    M = 1
    A = 2
    S = 3

class Direction(Enum):
     N = 0
     NE = 1
     E = 2
     SE = 3
     S = 4
     SW = 5
     W = 6
     NW = 7

def getmap(letter: XMAS) -> list:
    if letter == XMAS.M: return mmap
    elif letter == XMAS.A: return amap
    elif letter == XMAS.S: return smap
    else: return

def getnext(letter: XMAS, dir: Direction, location: tuple) -> bool:
    if dir == Direction.N: location = north(location)
    elif dir == Direction.NE: location = neast(location)
    elif dir == Direction.E: location = east(location)
    elif dir == Direction.SE: location = seast(location)
    elif dir == Direction.S: location = south(location)
    elif dir == Direction.SW: location = swest(location)
    elif dir == Direction.W: location = west(location)
    elif dir == Direction.NW: location = nwest(location)

    if location in getmap(letter):
        if letter.value < 3:
            return getnext(XMAS(letter.value + 1), dir, location)
        elif letter.value == 3: return True
    else: return False

def north(location: tuple): return (location[0], location[1] - 1)
def neast(location: tuple): return north(east(location))
def south(location: tuple): return (location[0], location[1] + 1)
def seast(location: tuple): return south(east(location))
def east(location: tuple): return (location[0] + 1, location[1])
def swest(location: tuple): return south(west(location))
def west(location: tuple): return (location[0] - 1, location[1])
def nwest(location: tuple): return north(west(location))

xmap = []
mmap = []
amap = []
smap = []

with open('AoC 2024/Input/Day4Data.txt') as file:
    words = 0

    for y,line in enumerate(file):
        xmap += [(x,y) for x, letter in enumerate(line) if letter == "X"]
        mmap += [(x,y) for x, letter in enumerate(line) if letter == "M"]
        amap += [(x,y) for x, letter in enumerate(line) if letter == "A"]
        smap += [(x,y) for x, letter in enumerate(line) if letter == "S"]
     
    for x in xmap:
        for d in Direction:
            if getnext(XMAS.M, d, x): words += 1

print(words)