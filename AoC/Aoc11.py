
from AoC.intcoder import IntCoder
from collections import deque

class Robot:

    def __init__(self,x):
        self.direction = deque([(0,1),(1,0),(0,-1),(-1,0)])
        self.position = (0,0)
        self.program = IntCoder(x)
        self.log = set({})
        self.panels = {}

    def turn(self, c):
        if c == 1:
            self.direction.rotate(-1)
        else:
            self.direction.rotate(1)

    def facing(self):
        return self.direction[0]

    def move_forward(self):
        x,y = self.position
        dx,dy = self.facing()

        self.position = (x + dx, y +dy)

    def floor(self):
        if self.position in self.panels:
            return self.panels[self.position]
        else:
            return 0

    def paint_floor(self):

        self.panels[self.position] = floor()
        self.log.add(self.position)

    def step(self):
        
        self.paint_floor()
        
        pass


d = {}

rob = Robot([3,8,1005,8,339,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,2,1108,11,10,1,1,20,10,2,107,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,62,1006,0,29,1006,0,12,1,1101,5,10,1,2,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,99,1006,0,30,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1001,8,0,124,1006,0,60,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,149,2,1007,2,10,1,1105,10,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,178,1,1108,15,10,1,1101,5,10,1,109,8,10,1006,0,20,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,215,1006,0,61,1006,0,16,2,1105,15,10,1006,0,50,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,250,1,1003,10,10,1,9,19,10,2,1004,6,10,2,1106,2,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,289,1,1103,13,10,2,105,17,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,318,101,1,9,9,1007,9,1086,10,1005,10,15,99,109,661,104,0,104,1,21101,0,825599304340,1,21101,356,0,0,1106,0,460,21101,0,937108545948,1,21102,1,367,0,1106,0,460,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,21628980315,1,21101,0,414,0,1105,1,460,21101,0,3316673539,1,21101,425,0,0,1106,0,460,3,10,104,0,104,0,3,10,104,0,104,0,21102,988753428840,1,1,21102,1,448,0,1106,0,460,21102,825544569700,1,1,21102,459,1,0,1106,0,460,99,109,2,21202,-1,1,1,21102,1,40,2,21102,491,1,3,21102,481,1,0,1105,1,524,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,486,487,502,4,0,1001,486,1,486,108,4,486,10,1006,10,518,1101,0,0,486,109,-2,2105,1,0,0,109,4,2102,1,-1,523,1207,-3,0,10,1006,10,541,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21102,560,1,0,1106,0,565,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,588,2207,-4,-2,10,1006,10,588,22101,0,-4,-4,1105,1,656,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,1,607,0,1106,0,565,22102,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,626,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,648,21202,-1,1,1,21101,0,648,0,105,1,523,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0])
rob.program.add_input(0)
