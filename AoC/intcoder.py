from collections import  deque
from itertools import permutations

class IntCoder:

    def __init__(self, x, inputs = [], name = None):
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
        if not self.inputs:
            _in = int(input("Enter input: "))
        else:
            _in = self.inputs.popleft()
        
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


def day7():
    
    comp = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    #comp = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    comp = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    
    phases = [7,9,8,5,6]
    _mx = 0
    _mx_ph = 0
    #for ph in permutations(ph):
    names = 'ABCDE'

    
    
    for ph in permutations(phases):
        print(ph)
        # initialize machines:
        amplifiers = [IntCoder(comp, [p], name ) for p,name in zip(ph,names)]
        assert len(amplifiers) == 5


        _input = 0 
        E_output = 0

        while not any(a.halted for a in amplifiers):
        
            for m in amplifiers:
                m.add_input(_input)
                m.produce_output()
                if not m.halted:
                    _input = m.popout()
                    if m.name == 'E':
                        E_output = _input
        if E_output > _mx:
            _mx = max(_mx, E_output)    
            _mx_ph = ph
        
    print(_mx, _mx_ph)




if __name__ == '__main__':
    
    day7()