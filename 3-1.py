import re

with open('AoC 2024/Input/Day3Test.txt') as file:
    total = 0
    pattern = r'mul\(\d{1,},\d{1,}\)'

    for line in file:
        muls = re.findall(pattern, line)
        for mul in muls:
            m = re.findall("\d+", mul)
            total += int(m[0]) * int(m[1])

    print (total)