blinks = 75
stones = {
    '0': 0,
    '1': 0
}

with open('AoC 2024/Input/Day11Data.txt') as file:
    start = [s for s in file.readline().strip().split()]
    for s in start: stones[s] = 1
    
    for blink in range(blinks):
        values = list(stones.items())
        for rock in values: 
            if int(rock[0]) == 0: 
                stones['1'] += rock[1]
                stones['0'] -= rock[1]
            elif len(rock[0]) % 2 == 0: 
                s1, s2 = str(int(rock[0][:len(rock[0])//2])), str(int(rock[0][len(rock[0])//2:]))
                if s1 in stones: stones[s1] += rock[1]
                else: stones[s1] = rock[1]
                if s2 in stones: stones[s2] += rock[1]
                else: stones[s2] = rock[1]
                stones[rock[0]] -= rock[1]
            else: 
                nr = str(int(rock[0]) * 2024)
                if nr in stones: stones[nr] += rock[1]
                else: stones[nr] = rock[1]
                stones[rock[0]] -= rock[1]
        
        if blink == 24: print(f"Puzzle 1 solution: {sum(stones.values())}") #Putting this here because it's funny.
                
    print(f"Puzzle 2 solution: {sum(stones.values())}")