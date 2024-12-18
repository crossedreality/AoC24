def Decompiled(a: int) -> list: #This makes it work only for my input; maybe I'll actually write a generalized version later.
    b = 0
    c = 0
    o = []
    while a != 0:
        b = a % 8 
        b = b ^ 1 
        c = int(a / (2 ** b))
        b = b ^ c 
        b = b ^ 4 
        a = int(a / 8) 
        o.append(b % 8)
    return o

def solve(a: str, instructions: list, results: list):
    fuckit = [ "000", "001", "010", "011", "100", "101", "110", "111"]
    for fu in fuckit:
        r = a + fu
        output = Decompiled(int(r,2))
        strprogram = ''.join([str(s) for s in instructions])
        strout = ''.join([str(s) for s in output])
        if strprogram == strout: results.append(int(r,2))
        elif strprogram.endswith(strout) and len(strout) > 0: solve(r,instructions,results)

with open('/Users/graeme/Documents/VS Code/AoC 2024/Input/Day17Data.txt') as file:
    instructions = []
    for line in file:
        line = line.strip()
        if line.startswith("Program: "): instructions = [int(i) for i in (line.split(': ')[1]).split(',')]

    results = []
    solve('',instructions, results)
    print(min(results))