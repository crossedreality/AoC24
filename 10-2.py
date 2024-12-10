class Trailhead:
    def __init__(self, location):
        self.location = location
        self.peaks = []

size = (0,0)
map = {}
peaks = set()
trailheads = {}

def north(location: tuple): return (location[0], location[1] - 1)
def south(location: tuple): return (location[0], location[1] + 1)
def east(location: tuple): return (location[0] + 1, location[1])
def west(location: tuple): return (location[0] - 1, location[1])
def inbounds(location: tuple):  
     if 0 <= location[0] < size[0] and 0 <= location[1] < size[1]: return True

def traverse(location: tuple, elevation: int, trailheads: list, peak: tuple):
    if elevation == 0: 
        if location in trailheads: trailheads[location].peaks.append(peak)
        else:
            t = Trailhead(location)
            t.peaks.append(peak)
            trailheads[location] = t
    else: 
        n = north(location)
        s = south(location)
        e = east(location)
        w = west(location)
        if inbounds(n) and map[n] == (elevation - 1): traverse(n, map[n], trailheads, peak)
        if inbounds(s) and map[s] == (elevation - 1): traverse(s, map[s], trailheads, peak)
        if inbounds(e) and map[e] == (elevation - 1): traverse(e, map[e], trailheads, peak)
        if inbounds(w) and map[w] == (elevation - 1): traverse(w, map[w], trailheads, peak)


with open('AoC 2024/Input/Day10Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))

    for y,line in enumerate(file):
        for x,c in enumerate(line):
            c = int(c)
            map[(x,y)] = c
            if c == 9: peaks.add((x,y))
    
    for p in peaks:
        traverse(p, 9, trailheads, p)

score = 0
for t in trailheads.values(): score += len(t.peaks)
print(score)