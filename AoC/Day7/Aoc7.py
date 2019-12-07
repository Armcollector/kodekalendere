from itertools import permutations

class IntCoder:

    def __init__(self, x, inputs = []):
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
        self.inputs = list(reversed(inputs))
        self.outputs = []
        self.i = 0
        self.halted = False

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
            _in = self.inputs.pop()
        self.x[self.x[i + 1]] = _in
        return i + 2

    def out(self, i, ps=[0, 0, 0]):
        p1 = self.x[i + 1] if ps[0] else self.x[self.x[i + 1]]
        self.outputs.append(p1)
        return i + 2

    def popout(self):
        return self.outputs.pop()

    def parameters(self, opcode):
        p = []
        opcode //= 100
        for i in range(3):
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

        return self.outputs.pop() if self.outputs else None


def test_day7_part1():
    comp = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
    phases =[3,1,2,4,0]
    _mx = 0
    for ph in permutations(phases):
        _input = 0
        for p,e in zip(ph,['A','B','C','D','E']):
            A = IntCoder(comp,[p,_input])
            A.intcode()
            _input = A.outputs.pop()
        _mx = max(_mx,_input)
    assert _mx == 30940

def test_day2_part1():
    comp = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0]
    comp[1]= 12
    comp[2]= 2

    machine = IntCoder(comp)
    machine.intcode()

    assert machine.x[0] == 3058646




def day7_part2():
    
    phases =[5,6,7,8,9]
    _mx = 0
    #for ph in permutations(phases):


    comp = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    ph = [9,7,8,5,6]

    # initialize machines:
    amplifiers = [IntCoder(comp, [p] ) for p in ph]

    active_machine = 0
    _input = 0
    while not amplifiers[active_machine].halted:
        amplifiers[active_machine].inputs.append(_input)
        _output = amplifiers[active_machine].produce_output()

        if _output == None:
            print(input)
            break
        else:
            _input=_output
            active_machine = (active_machine +1)%5

    print(active_machine, _input)


if __name__ == '__main__':

    comp = [3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]

    test_day7_part1()
    test_day2_part1()


   
