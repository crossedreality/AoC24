import re

with open('AoC 2024/Input/Day3Data.txt') as file:
    instructions = ' '.join(line.strip() for line in file) #Don't love this construction, but it joins all of the lines without linefeeds
    total = 0
    disabledrange = []
    
    clicker = re.finditer(r"(don't\(\))(.*?)(do\(\))", instructions)
    for click in clicker: disabledrange.append((click.end(1), click.end(3))) #Group 1 is don't(), group 3 is do()
    
    #Damn, the above was slightly too elegant.
    last = disabledrange[-1][1]
    lastnot = re.search(r"(don't\(\))", instructions[last:])
    if lastnot: disabledrange.append((lastnot.start() + last, len(instructions)))
    
    muls = list(re.finditer(r'mul\(\d{1,},\d{1,}\)', instructions))
    for mul in muls:
        if not(any(mul.start() in range(start, end) for start, end in disabledrange)):
            m = re.findall("\d+", mul.group())
            total += int(m[0]) * int(m[1])

    print (total)