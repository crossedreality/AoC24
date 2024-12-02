from enum import Enum

class ReactorStatus(Enum):
    Increasing = 1
    Decreasing = 2
    Safe = 3
    Unsafe = 4


class Report:
    def __init__(self, status, values):
        self.status = status
        self.values = values


with open('AoC 2024/Input/Day2Data.txt') as file:
    safereports = []

    for report in file:
        report = report.strip().split()
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
        
        if status == ReactorStatus.Safe: safereports.append(Report(status,report))

    print(len(safereports))