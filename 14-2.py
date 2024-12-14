import re

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def blink(self):
        nx = self.position[0] + self.velocity[0]
        ny = self.position[1] + self.velocity[1]
        if not(inbounds((nx,ny))):
            if nx >= size[0]: nx = nx - size[0]
            elif nx < 0: nx = size[0] + nx
            if ny >= size[1]: ny = ny - size[1]
            elif ny < 0: ny = size[1] + ny
        self.position = (nx,ny)

#Regions and maps again
size = (101,103) #Defined outside of the input files
def inbounds(location: tuple) -> bool: 
    if 0 <= location[0] < size[0] and 0 <= location[1] < size[1]: return True
def inquad(min: tuple, max:tuple, location: tuple) -> bool:
    if min[0] <= location[0] <= max[0] and min[1] <= location[1] <= max[1]: return True
    
#I LLM regex strings and you can't stop me.
pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"

robits = []
seconds = 10000
with open('AoC 2024/Input/Day14Data.txt') as file:
    for line in file:
        match = re.search(pattern,line)
        px = int(match.group(1))
        py = int(match.group(2))
        vx = int(match.group(3))
        vy = int(match.group(4))
        robits.append(Robot((px,py),(vx,vy)))
    
    for s in range(seconds):
        for robot in robits:
            robot.blink()
        
        rlines = set([rf.position[1] for rf in robits])
        for ry in rlines:
            formation = sorted([r.position[0] for r in robits if r.position[1] == ry])
            if len(formation) > 10:
                count = 0
                for i,r in enumerate(formation[:-1]):
                    if formation[i] + 1 == formation[i + 1]: count += 1 #Find straight lines, I guess? 
                    else: count = 0
                    if count > 10: 
                        print(f"Christmas tree? {s + 1}")
                        break