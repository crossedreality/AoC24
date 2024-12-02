from enum import Enum

class ReactorStatus(Enum):
    Unknown = 0
    Increasing = 1
    Decreasing = 2
    Safe = 3
    Unsafe = 4

class Report:
    def __init__(self, status, values):
        self.status = status
        self.values = values

def validate(report:list) -> ReactorStatus:
    status = ReactorStatus.Unknown
    rtype = int(report[1]) - int(report[0]) #Pew pew
    if rtype < 0: status = ReactorStatus.Decreasing
    elif rtype > 0: status = ReactorStatus.Increasing
    else: status = ReactorStatus.Unsafe
        
    l = len(report) - 1
    for i, level in enumerate(report):
        if status == ReactorStatus.Unsafe: break
        elif i < l: 
            level = int(level)
            nextlevel = int(report[i+1])
            change = nextlevel - level
            
            if status == ReactorStatus.Decreasing and change >= 0 or change < -3:
                status = ReactorStatus.Unsafe
            elif status == ReactorStatus.Increasing and change <=0 or change > 3:
                status = ReactorStatus.Unsafe
        elif i == l and (status == ReactorStatus.Increasing or status == ReactorStatus.Decreasing):
            status = ReactorStatus.Safe
    return status

with open('AoC 2024/Input/Day2Data.txt') as file: #391 still too low
    safereports = []

    for report in file:
        report = report.strip().split()
        
        if validate(report) == ReactorStatus.Safe:
            safereports.append(report)
        
        else:
            for i,l in enumerate(report):
                r2 = report.copy()
                r2.pop(i)
                if validate(r2) == ReactorStatus.Safe:
                    safereports.append(report)
                    break

    print(len(safereports))