import re

allrules = []
updates = []
middles = 0

def validate(update: list) -> bool:
    valid = True
    for i,u in enumerate(update):
        if not(valid): break
        rules = [r for r in allrules if r[0] == u]
        for rule in rules:
            try:
                if update.index(rule[1]) < i: valid = False
            except ValueError: continue
    return valid

with open('AoC 2024/Input/Day5Data.txt') as file:
    rulepattern = r'\d{2}\|\d{2}'

    for line in file:
        line = line.strip()
        if re.match(rulepattern, line):
            rule = line.split("|")
            allrules.append((int(rule[0]),int(rule[1])))
        elif line:
            updates.append([int(i) for i in line.split(",")])
    
    for update in updates:
        if validate(update):
            middles += update[int(len(update) / 2)] #Thank god for zero indexing and assuming only odd numbers!
    
print(middles)