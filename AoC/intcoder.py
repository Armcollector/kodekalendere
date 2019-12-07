from collections import  deque
from itertools import permutations

class IntCoder:

    def __init__(self, x, inputs = [], name = None):
        self.x = x
        self.ops = {1: self.add,
                    2: self.mul,
                    3: self.inp,
                    4: self.out,
                    5: self.jump_if_true,
                    6: self.jump_if_false,
                    7: self.less_than,
                    8: self.equals
                    }
        self.inputs = deque(inputs)
        self.outputs = []
        self.i = 0
        self.halted = False
        self.name = name

    def jump_if_true(self,i, ps=[0,0,0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]

        if p1 != 0:
            return p2
        else:
            return i+3

    def jump_if_false(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]

        if p1 == 0:
            return p2
        else:
            return i + 3

    def less_than(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]
        p3 = self.x[i + 3]

        self.x[p3] = 1 if p1 < p2 else 0

        return i + 4

    def equals(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]
        p3 = self.x[i + 3]

        self.x[p3] = 1 if p1 == p2 else 0

        return i + 4


    def add(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]
        p3 = self.x[i + 3]
        self.x[p3] = p1 + p2
        return i + 4

    def mul(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        p2 = self.x[i + 2] if ps[1] else self.x[self.x[i + 2]]
        p3 = self.x[i + 3]
        self.x[p3] = p1 * p2
        return i + 4

    def inp(self, i, ps=[0, 0, 0]):
        if not self.inputs:
            _in = int(input("Enter input: "))
        else:
            _in = self.inputs.popleft()
        print(self.name, "uses input:", _in)
        self.x[self.x[i + 1]] = _in
        return i + 2

    def out(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        self.outputs.append(p1)
        print(p1)
        return i + 2

    def popout(self):
        print(self.name, "outputs", self.outputs[-1])
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
        print(self.name, "receives", _inp)
        self.inputs.append(_inp)

    


if __name__ == '__main__':


    comp = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,32,43,225,101,68,192,224,1001,224,-160,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1001,118,77,224,1001,224,-87,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,5,19,225,1102,74,50,224,101,-3700,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1102,89,18,225,1002,14,72,224,1001,224,-3096,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1101,34,53,225,1102,54,10,225,1,113,61,224,101,-39,224,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,31,61,224,101,-92,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1102,75,18,225,102,48,87,224,101,-4272,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,23,92,225,2,165,218,224,101,-3675,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,8,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,226,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,344,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,359,1001,223,1,223,7,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,464,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1108,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,659,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
    machine = IntCoder(comp, [1])
    machine.intcode()

    comp = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    comp = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    ph = [9,8,7,6,5]
    _mx = 0

    #for ph in permutations(ph):

    print(ph)
    names = 'ABCDE'

    
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

    _mx = max(_mx, E_output)    
        
    print(_mx)

    # active_machine = 0
    # _input = 0
    # while not amplifiers[active_machine].halted:
    #     amplifiers[active_machine].inputs.append(_input)
    #     _output = amplifiers[active_machine].produce_output()

    #     if _output == None:
    #         print(input)
    #         break
    #     else:
    #         _input=_output
    #         active_machine = (active_machine +1)%5

    # print(active_machine, _input) 