import re

allrules = []
updates = []
badupdates = []
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

def rectify(update: list) -> list:
    solved = False
    while not(solved):
        solved = validate(update)
        for i,u in enumerate(update):
            restart = False
            rules = [r for r in allrules if r[0] == u]
            for rule in rules:
                try:
                    rdx = update.index(rule[1])
                    if rdx < i:
                        update[rdx], update[i] = update[i], update[rdx]
                        restart = True
                        break
                except ValueError: continue
            if restart: break
    return update

        
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
        if not(validate(update)): badupdates.append(update)

    for update in badupdates:
        middles += rectify(update)[int(len(update) / 2)]

print(middles)