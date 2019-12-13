from collections import  deque
from itertools import permutations

class IntCoder:

    def __init__(self, x, inputs = [], name = None, subroutine= None):
        self.x = x + [0]*10**6
        self.ops = {1: self.add,
                    2: self.mul,
                    3: self.inp,
                    4: self.out,
                    5: self.jump_if_true,
                    6: self.jump_if_false,
                    7: self.less_than,
                    8: self.equals,
                    9: self.adjust_relative
                    }
        self.inputs = deque(inputs)
        self.outputs = []
        self.i = 0
        self.halted = False
        self.name = name
        self.relative_base=0
        if subroutine:
            self.subroutine = subroutine
            self.subroutine.attach_machine(self)

    def parameter(self, pnr, ps,assignment=False):
        if not assignment:        
            if ps[pnr-1] == 0:
                return self.x[self.x[self.i + pnr]]
            if ps[pnr-1] == 1:
                return self.x[self.i+pnr]
            if ps[pnr-1] == 2:
                return self.x[self.x[self.i + pnr]+self.relative_base]
        else:
            if ps[pnr-1] == 0:
                return self.x[self.i+pnr]
            if ps[pnr-1] == 1:
                return self.x[self.i+pnr]
            if ps[pnr-1] == 2:
                return self.x[self.i + pnr]+self.relative_base

    def jump_if_true(self,i, ps=[0,0,0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)

        return p2 if p1 else i+3

    def adjust_relative(self,i, ps=[0,0,0]):
        p1 = self.parameter(1,ps)

        self.relative_base += p1

        return self.i + 2


    def jump_if_false(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)

        return i+3 if p1 else p2

    def less_than(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)
        p3 = self.parameter(3,ps,True)

        self.x[p3] = 1 if p1 < p2 else 0

        return i + 4

    def equals(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)
        p3 = self.parameter(3,ps,True)

        self.x[p3] = 1 if p1 == p2 else 0

        return i + 4


    def add(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)
        p3 = self.parameter(3,ps,True)
        self.x[p3] = p1 + p2
        return i + 4

    def mul(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        p2 = self.parameter(2,ps)
        p3 = self.parameter(3,ps,True)
        self.x[p3] = p1 * p2
        return i + 4

    def inp(self, i, ps=[0, 0, 0]):
        if self.inputs:
            _in = self.inputs.popleft()
        elif self.subroutine:
            _in = self.subroutine()
        else:
            _in = int(input("Enter input: "))
            
        
        p1 = self.parameter(1,ps,True)
        self.x[p1] = _in
        return i + 2

    def out(self, i, ps=[0, 0, 0]):
        p1 = self.parameter(1,ps)
        self.outputs.append(p1)
        return i + 2

    def popout(self):
        return self.outputs.pop()

    def parameters(self, opcode):
        p = []
        opcode //= 100
        for _ in range(3):
            p.append(opcode % 10)
            opcode //= 10
        return p

    def intcode(self):
        while True:
            opcode = self.x[self.i]
            op = opcode % 100
            ps = self.parameters(opcode)

            if op == 99:
                self.halted = True
                break

            self.i = self.ops[op](self.i,ps)

        return self.x

    def produce_output(self):
        while not self.outputs:
            opcode = self.x[self.i]
            op = opcode % 100
            ps = self.parameters(opcode)

            if op == 99:
                self.halted = True
                break

            self.i = self.ops[op](self.i,ps)

    def add_input(self,_inp):
        self.inputs.append(_inp)


if __name__ == '__main__':
    
    pass