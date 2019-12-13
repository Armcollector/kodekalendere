class Robot:
    
    def __init__(self, priority):
        self.position = (0,0)
        self.priority = priority
        self.steps = 0
        self.log = set([])
        self.dir = { 'syd': (1,0), 'aust': (0,1), 'nord': (-1,0), 'vest' : (0,-1) }
        self.stack = []
    
    def halted(self):
        return self.position == (499,499)
    
    def been(self, i):
        dy,dx = self.dir[i]
        y,x = self.position
        newposition = (y+dy,x+dx)
        return newposition in self.log
    
    def blocked(self, i):
        y,x = self.position
        return rooms[y][x][i]

    
    def move(self):
        for i in self.priority:
            if self.been(i):
                continue
            if self.blocked(i):
                continue
            dy,dx = self.dir[i]
            y,x = self.position
            self.position = (y+dy,x+dx)
            self.log.add(self.position)
            self.stack.append(self.position)
            self.steps +=1
            return
        
        self.stack.pop()
        self.position = self.stack[-1]
    
        
    def __repr__(self):
        y,x = self.position
        return f"robot pos={self.position} room= {rooms[y][x]}"
        
arthur = Robot(['syd', 'aust', 'vest', 'nord'])
while not arthur.halted():
    arthur.move()
print("arthur", arthur.steps)

isaac = Robot(["aust", "syd", "vest", "nord"])
while not isaac.halted():
    isaac.move()
print("isaac", isaac.steps)

print(len(isaac.log) - len(arthur.log))
