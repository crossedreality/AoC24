from enum import Enum #for Peter
map = {}
regions = []
size = (0,0)

class Direction(Enum):
     N = 0
     E = 2
     S = 4
     W = 6

class Corner:
    def __init__(self, edge: Direction):
        pass

class Plot:
    def __init__(self, label: str, location: tuple):
        self.label = label
        self.location = location
        self.inregion = False
    
    def getPerimeters(self) -> int:
        p = 0
        edges = cardinal(self.location)
        for edge in edges:
            if not(inbounds(edge)): p += 1
            elif inbounds(edge) and map[edge].label != self.label: p += 1
        return p

    def getNS(self) -> set:
        corners = set()
        n = north(self.location)
        s = south(self.location)
        if not(inbounds(n)) or map[n].label != self.label: corners.add(Direction.N)
        if not(inbounds(s)) or map[s].label != self.label: corners.add(Direction.S)
        return corners
    
    def getEW(self) -> set:
        corners = set()
        e = east(self.location)
        w = west(self.location)
        if not(inbounds(e)) or map[e].label != self.label: corners.add(Direction.E)
        if not(inbounds(w)) or map[w].label != self.label: corners.add(Direction.W)
        return corners

    perimeters = property(getPerimeters)
    nsperimeters = property(getNS)
    ewperimeters = property(getEW)

class Region:
    def __init__(self):
        self.plots = set()

    def add(self, plot: Plot):
        plot.inregion = True
        self.plots.add(plot)

    def getPrice(self) -> int:
        p = 0
        for plot in self.plots: p += plot.perimeters
        return p * len(self.plots)
    
    def getDiscount(self) -> int:
        return len(self.plots) * self.edges
    
    def getEdges(self) -> int:
        bounds = [p for p in self.plots if p.perimeters > 0]
        bounds.sort(key= lambda p: p.location[1]) 
        yvalues = set([b.location[1] for b in bounds])
        xvalues = set([b.location[0] for b in bounds])
        count = 0
        for r in yvalues: 
            start = sorted([b for b in bounds if b.location[1] == r],key=lambda x: x.location[0])[0]
            count += len(start.nsperimeters)
            count += sideways(self, start, 0)
        for r in xvalues:
            start = sorted([b for b in bounds if b.location[0] == r], key=lambda x:x.location[0])[0]
            count += len(start.ewperimeters)
            count += downways(self, start, 0)
        return count

    price = property(getPrice)
    edges = property(getEdges)
    discount = property(getDiscount)

def traverse(region, plot):
    if not(plot.inregion):
        region.add(plot)
        edges = cardinal(plot.location)
        for edge in edges:
            if inbounds(edge) and map[edge].label == plot.label and not(map[edge].inregion):
                traverse(region,map[edge])

def sideways(region, plot, count):
    nextplot = getnext(region,plot,Direction.E)
    if nextplot:
        nextnsp = nextplot.nsperimeters
        plotnsp = plot.nsperimeters
        if ((plotnsp == nextnsp and (nextplot.location[0] - plot.location[0]) == 1) or
            (len(nextnsp) < len(plotnsp) and (nextplot.location[0] - plot.location[0]) == 1) or
            (plotnsp == nextnsp and len(nextnsp) == 0)):
            return sideways(region,nextplot,count)
        elif plotnsp == nextnsp and len(nextnsp) > 0 and (nextplot.location[0] - plot.location[0]) > 1:
            return sideways(region,nextplot,count+len(nextnsp))
        else: 
            if (nextplot.location[0] - plot.location[0]) > 1: return sideways(region,nextplot,count+len(nextnsp)) #this can be an or above?
            else: return sideways(region,nextplot,count+max(abs(len(plotnsp) - len(nextnsp)),1))
    else: return count

def downways(region, plot, count):
    nextplot = getnext(region,plot,Direction.S)
    if nextplot:
        nextewp = nextplot.ewperimeters
        plotewp = plot.ewperimeters
        if ((plotewp == nextewp and (nextplot.location[1] - plot.location[1]) == 1) or
            (len(nextewp) < len(plotewp) and (nextplot.location[1] - plot.location[1]) == 1) or
            (plotewp == nextewp and len(nextewp) == 0)):
            return downways(region,nextplot,count)
        elif plotewp == nextewp and len(nextewp) > 0 and (nextplot.location[1] - plot.location[1]) > 1:
            return downways(region,nextplot,count+len(nextewp))
        else:
            if (nextplot.location[1] - plot.location[1]) > 1: return downways(region,nextplot,count+len(nextewp)) #this can be an or above?
            else: return downways(region,nextplot,count+max(abs(len(plotewp) - len(nextewp)),1))
    else: return count

def getnext(region, plot, direction) -> Plot:
    if direction == Direction.E: next = east(plot.location)
    elif direction == Direction.S: next = south(plot.location)
    if inbounds(next) and map[next] in region.plots: return map[next]
    elif inbounds(next): return getnext(region,map[next],direction)
    else: return None

def north(location: tuple): return (location[0], location[1] - 1)
def south(location: tuple): return (location[0], location[1] + 1)
def east(location: tuple): return (location[0] + 1, location[1])
def west(location: tuple): return (location[0] - 1, location[1])
def inbounds(location: tuple): 
    if 0 <= location[0] < size[0] and 0 <= location[1] < size[1]: return True
def cardinal(location: tuple) -> list:
        n = north(location)
        s = south(location)
        e = east(location)
        w = west(location)
        return [n, s, e, w]

with open('AoC 2024/Input/Day12Data.txt') as file:
    file = file.read().splitlines()
    size = (len(file[0]),len(file))

    for y,line in enumerate(file):
        for x,l in enumerate(line):
            map[(x,y)] = Plot(l, (x,y)) #build the map
    
    for loc, plot in map.items():
        if plot.inregion: continue
        else:
            region = Region()
            regions.append(region)
            traverse(region,plot)

print(f"Part 1 Price: {sum(list(r.price for r in regions))}")
print(f"Part 2 Discount: {sum(list(r.discount for r in regions))}")