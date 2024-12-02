with open('AoC 2024/Input/Day1Data.txt') as file:
    
    listsep = "   "
    lista = []
    listb = []
    total = 0
    
    for line in file:
        parseline = line.strip().split(listsep)
        lista.append(int(parseline[0]))
        listb.append(int(parseline[1]))
    lista.sort()
    listb.sort()

    for i,v in enumerate(lista):
        total += abs(v - listb[i])

    print (total)