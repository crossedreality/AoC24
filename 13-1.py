import numpy #I had to look up basically every use of this module but at least I knew it existed.
import re

class ClawMachine:
    def __init__(self, abutton: tuple = None, bbutton: tuple = None, prize: tuple = None):
        self.abutton = abutton
        self.bbutton = bbutton
        self.prize = prize

    def GetTokens(self) -> int:
        buttons = numpy.array([[self.abutton[0],self.bbutton[0]],[self.abutton[1],self.bbutton[1]]]) #X values, then Y values, for the two equations
        prize = numpy.array([self.prize[0],self.prize[1]]) #Target X, Y
        a,b = numpy.linalg.solve(buttons,prize) #Have NumPy do the linear algebra for us because I can barely do this on paper
        a = round(a, 4) #Floating point inaccuracies! Sometimes I was geting 1.00000000000001 because NumPy returns a Float64
        b = round(b, 4) #I don't want to round "all the way" so just close enough to be sure. 
        if a.is_integer() and b.is_integer():
            return round((a * 3) + b) #I was getting weird errors using int() for this. I should have used round() from the jump.
        else:
            return None
                
    tokens = property(GetTokens)

buttonpattern = r"X\+(\d+), Y\+(\d+)"
prizepattern = r"X=(\d+), Y=(\d+)"

machines = []
with open('AoC 2024/Input/Day13Data.txt') as file:
    for i,line in enumerate(file):
        mod = i % 4
        if mod == 0:
            cm = ClawMachine()
            split = re.search(buttonpattern, line)
            cm.abutton = (int(split.group(1)), int(split.group(2)))
        if mod == 1:
            split = re.search(buttonpattern, line)
            cm.bbutton = (int(split.group(1)), int(split.group(2)))
        if mod == 2:
            split = re.search(prizepattern, line)
            cm.prize = (int(split.group(1)), int(split.group(2)))
            machines.append(cm)
        if mod == 3:
            continue

print(sum(t.tokens for t in machines if t.tokens is not None))