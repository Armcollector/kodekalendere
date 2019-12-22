import numpy as np
from scipy.signal import find_peaks


with open(r"C:\git\kodekalendere\knowit\dag22\forest.txt", "r") as f:
    x = f.read()

antall, hoyde = len(x), len(x.splitlines())

r = np.array(list(x.replace(' ','0').replace('#','1').replace('\n','')),dtype=int).reshape(hoyde,-1).transpose()
r2 = r.shape[1]- np.argmax(r[~np.all(r == 0,axis = 1)],axis=1)
print(np.sum(r2[find_peaks(r2)[0]]*40))