from enum import Enum

class XMAS(Enum):
    M = 1
    A = 2
    S = 3

class Direction(Enum):
     NE = 1
     SE = 3
     SW = 5
     NW = 7

def getmap(letter: XMAS) -> list:
    if letter == XMAS.M: return mmap
    elif letter == XMAS.A: return amap
    elif letter == XMAS.S: return smap
    else: return

def isletter(letter: XMAS, dir: Direction, location: tuple) -> bool:
    if dir == Direction.NE: location = neast(location)
    elif dir == Direction.SE: location = seast(location)
    elif dir == Direction.SW: location = swest(location)
    elif dir == Direction.NW: location = nwest(location)

    if location in getmap(letter): return True
    else: return False

def north(location: tuple): return (location[0], location[1] - 1)
def neast(location: tuple): return north(east(location))
def south(location: tuple): return (location[0], location[1] + 1)
def seast(location: tuple): return south(east(location))
def east(location: tuple): return (location[0] + 1, location[1])
def swest(location: tuple): return south(west(location))
def west(location: tuple): return (location[0] - 1, location[1])
def nwest(location: tuple): return north(west(location))

mmap = []
amap = []
smap = []

with open('AoC 2024/Input/Day4Data.txt') as file:
    countxmas = 0

    for y,line in enumerate(file):
        mmap += [(x,y) for x, letter in enumerate(line) if letter == "M"]
        amap += [(x,y) for x, letter in enumerate(line) if letter == "A"]
        smap += [(x,y) for x, letter in enumerate(line) if letter == "S"]
     
    for a in amap:
        words = 0
        for d in Direction:
            if isletter(XMAS.M, d, a):
                if d == Direction.NE and isletter(XMAS.S, Direction.SW, a): words += 1
                elif d == Direction.NW and isletter(XMAS.S, Direction.SE, a): words += 1
                elif d == Direction.SE and isletter(XMAS.S, Direction.NW, a): words += 1
                elif d == Direction.SW and isletter(XMAS.S, Direction.NE, a): words += 1
        if words == 2: countxmas += 1

print(countxmas)