with open('AoC 2024/Input/Day1Data.txt') as file:
    
    listsep = "   "
    lista = []
    listb = []
    score = 0
    
    for line in file:
        parseline = line.strip().split(listsep)
        lista.append(int(parseline[0]))
        listb.append(int(parseline[1]))
    lista.sort()
    listb.sort() #I'm sure there's an elegant way to do this that I don't know.

    for a in lista:
        score += a * listb.count(a) #Built-in count of occurences

    print (score)