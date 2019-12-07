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

    def add_input(self,_inp):
        self.inputs.append(_inp)