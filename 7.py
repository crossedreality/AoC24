from itertools import product

operators = ["+", "*"]

def calibrate(c: tuple) -> bool:
    operands = [int(n) for n in c[1].split()]
    operations = list(product(operators, repeat=len(operands) - 1))
    target = c[0]
    valid = False

    for permutation in operations:
        value = calculate(permutation,operands)
        if value == target: 
            valid = True
            break
    
    return valid

def calculate(permutation: list, operands: list) -> int:
    value = operands[0]
    for i,digit in enumerate(operands[1:]):
        if permutation[i] == "+": value = value + digit
        elif permutation[i] == "*": value = value * digit
        elif permutation[i] == "||": value = int(str(value) + str(digit))
    return value

with open('AoC 2024/Input/Day7Data.txt') as file:
    result = 0
    calibrations = set()
    failed = set()

    for line in file:
        equation = line.strip().split(":")
        calibrations.add((int(equation[0]), equation[1]))
    
    for c in calibrations:
        valid = calibrate(c)
        if valid: result += c[0]
        else: failed.add(c)
    
    print(f"Puzzle 1 result: {result}")

    operators.append("||")
    for c in failed:
        valid = calibrate(c)
        if valid: result += c[0]
    
    print(f"Puzzle 2 result: {result}")