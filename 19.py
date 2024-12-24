from functools import cache

towels = set()
patterns = []
goodpatterns = []

@cache
def refold(pattern: str, sequence: str) -> int:
    if len(pattern) == 0: return 1
    else:
        value = 0
        for towel in towels:
            nextseq = sequence + towel
            if pattern.startswith(towel): 
                value += refold(pattern[len(towel):], nextseq)
        return value

with open('/Users/graeme/Documents/VS Code/AoC 2024/Input/Day19Data.txt') as file:
    file = file.read().splitlines()
    for line in file: 
        if ',' in line: 
            t = line.split(',')
            for towel in t:
                towel = towel.strip()
                towels.add(towel)
        elif line: patterns.append(line)

permutations = 0
for pattern in patterns:
    result = refold(pattern, '')
    permutations += result
    if result > 0: goodpatterns.append(pattern)

print(f"Valid patterns: {len(goodpatterns)}")
print(f"Total permutations: {permutations}")