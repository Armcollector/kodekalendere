import numpy as np
from numpy import array



def chunks(lst, num_elements):
    for i in range(0, len(lst), num_elements):
        yield lst[i:i + num_elements]

def vol(mesh):
    s = 0
    for t in mesh:
        s += np.dot( t[0], np.cross(t[1],t[2]))/6
    return s

def cal_mesh(_inp):
    mesh = []

    for t in _inp.splitlines():
        l = [float(i) for i in t.split(',')]
        points  = [ np.array(list(p))  for p in chunks(l,3) ]
        mesh.append(points)
    return mesh


with open(r"C:\git\kodekalendere\knowit\dag15\model.csv", "r") as f:
    x= f.read()
    print(vol(cal_mesh(x))/1000)