class Block:
    def __init__(self, ID, position):
        self.ID = ID
        self.position = position

blocks = []
with open('AoC 2024/Input/Day9Data.txt') as file:
    map = file.read().strip()

    id = 0
    position = 0
    for i,c in enumerate(map):
        c = int(c)
        if i % 2 == 0:
            for b in range(c):
                blocks.append(Block(id,position))
                position += 1
            id += 1
        else: 
            for b in range(c):
                blocks.append(Block(None, position))
                position += 1
    
freespace = [fs for fs in blocks if fs.ID == None]
fileblocks = [fb for fb in blocks if fb.ID != None]
fileblocks.sort(key=lambda fb: fb.position, reverse=True)

for space in freespace:
    if fileblocks[0].position > space.position:
        space.ID = fileblocks[0].ID
        fileblocks.pop(0)

blocks = fileblocks + freespace
blocks = [fb for fb in blocks if fb.ID != None]
blocks.sort(key=lambda b: b.position)

checksum = 0
for block in blocks:
    checksum += (block.position * block.ID)

print(checksum)

#It was bound to happen eventually: my part 1 had a bug because I forgot to indent a command.