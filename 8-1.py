from itertools import combinations
from operator import itemgetter

size = (0,0)

class Frequency:
    def __init__(self, frequency: str, location: tuple):
        self.frequency = frequency
        self.antennas = set()
        if location: self.antennas.add(location)
    
    def add_antenna(self, location):
        self.antennas.add(location)

    def gen_antinodes(self) -> list:
        anodes = []
        nodes = list(combinations(self.antennas, 2))
        nodes.sort(key=itemgetter(1))
        for n in nodes: 
            anodes.extend(vplot(n[0],n[1]))
        return anodes    

def vplot(a: tuple, b: tuple) -> list:
    distance = (b[0] - a[0],b[1] - a[1])
    anodes = []
    anodes.append((a[0] - distance[0],a[1] - distance[1])) #Twice as far from b
    anodes.append((b[0] + distance[0],b[1] + distance[1])) #Twice as far from a

    return [c for c in anodes if inbounds(c)]

def inbounds(location: tuple):  
     if 0 <= location[0] < size[0] and 0 <= location[1] < size[1]: return True 

frequencies = {}
with open('AoC 2024/Input/Day8Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))

    for y,line in enumerate(file):
        found = [(letter,x,y) for x, letter in enumerate(line) if letter != "."] #triple
        for f in found:
            a = frequencies.get(f[0])
            if a: a.add_antenna((f[1],f[2]))
            else: frequencies[f[0]] = Frequency(f[0],(f[1],f[2]))

antinodes = []
for f in frequencies.values():
    antinodes.extend(f.gen_antinodes())

print(len(set(antinodes)))