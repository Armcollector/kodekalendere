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

    def parameters(self, opcode):
        p = []
        opcode //= 100
        for i in range(3):
            p.append(opcode % 10)
            opcode //= 10
        return p

    def intcode(self):
        i = 0
        while True:
            opcode = self.x[i]
            op = opcode % 100
            ps = self.parameters(opcode)

            if op == 99:
                break

            i = self.ops[op](i,ps)

        return self.x


if __name__ == '__main__':

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

    print(_mx)