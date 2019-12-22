import numpy as np

with open(r"C:\git\kodekalendere\knowit\dag22\forest.txt", "r") as f:
    x = f.read()

antall, hoyde = len(x), len(x.splitlines())
forest = np.zeros( antall )

for i,c in enumerate(x):
    if c == '#':
        forest[i]= 1
    else: 
        forest[i] = 0

r = forest.reshape(hoyde,-1).transpose()

_mx = 0
top = []
for c in r:
    for i, t in enumerate(c):
        if t == 1:
            _mx = max(_mx, r.shape[1] - i)
            break
    else:
        top.append(_mx)
        _mx = 0

sum([int(i*0.2*200) for i in top])