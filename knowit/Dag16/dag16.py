with open(r"C:\git\kodekalendere\knowit\dag16\fjord.txt", "r") as f:
    x = f.read()

antall, hoyde = len(x), len(x.splitlines())

import numpy as np

fjord = np.zeros( antall )


for i,c in enumerate(x):
    if c == '#':
        fjord[i]= 1
    elif c == 'B':
        fjord[i]= 2
    else: 
        fjord[i] = 0
    



import PIL
%matplotlib inline
import matplotlib.pyplot as plt

a = fjord.reshape(hoyde,-1).transpose()

from PIL import Image

im = Image.fromarray(a)
plt.imshow(im)

y,x = np.argwhere(a == 2)[0]


