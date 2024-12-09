class Block:
    def __init__(self, ID, position):
        self.ID = ID
        self.position = position

class File:
    def __init__(self, ID, blocks: list):
        self.ID = ID
        self.blocks = blocks

    def getSize(self):
        return len(self.blocks)
    
    def getPos(self):
        return self.blocks[0].position
    
    size = property(getSize)
    position = property(getPos)

class Space:
    def __init__(self, blocks: list):
        self.blocks = blocks

    def getSize(self):
        return len(self.blocks)

    def getPos(self):
        return self.blocks[0].position
    
    def fill(self, file: File):
        for fb in file.blocks:
            fb.position = self.blocks[0].position
            self.blocks.pop(0)
 
    size = property(getSize)
    position = property(getPos)

files = []
spaces = []
with open('AoC 2024/Input/Day9Data.txt') as file:
    map = file.read().strip()

    id = 0
    position = 0
    for i,c in enumerate(map):
        c = int(c)
        blocks = []
        if i % 2 == 0:
            for b in range(c):
                blocks.append(Block(id,position))
                position += 1
            files.append(File(id,blocks))
            id += 1
        else: 
            for b in range(c):
                blocks.append(Block(None, position))
                position += 1
            if len(blocks) > 0: spaces.append(Space(blocks))

files.sort(key=lambda fb: fb.ID, reverse=True)
spaces.sort(key=lambda sb: sb.position)

for f in files:
    for s in spaces:
        if (s.size >= f.size) and (f.position > s.position): 
            s.fill(f)
            if s.size == 0: 
                spaces.remove(s)
            break

checksum = 0
for file in files:
    for block in file.blocks:
        checksum += (block.position * block.ID)

print(checksum)
spaces.sort(key=lambda f: f.position)