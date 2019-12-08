with open(r'C:\git\kodekalendere\AoC\Day8\day8_input.txt','r') as f:
    x = f.read()

x = [int(i) for i in x]

import numpy as np 

a = np.array(x)


a = a.reshape(-1,25,6)
_cz = 100000
val = 0

for i in range(a.shape[0]):
    cz = np.sum(a[i,:,:]==0)
    if cz < _cz:
       val =  np.sum(a[i,:,:]==1)*np.sum(a[i,:,:]==2)
       _cz = cz
        
print(_cz,val)



with open(r'C:\git\kodekalendere\AoC\Day8\day8_input.txt','r') as f:
    x = f.read()

#x = '0222112222120000'    
    
x = [int(i) for i in x]

import numpy as np 

a = np.array(x)

s1 = 6
s2 = 25

a = a.reshape(-1,s1,s2)
_cz = 100000
val = 0

m = np.zeros((s1,s2), dtype=int)
m.fill(2)

for i in range(a.shape[0]):
    #m = np.minimum(a[i,:,:],m)
    x = a[i,:,:]
    for c in range(s1):
        for d in range(s2):
            if m[c,d] > 1:
                m[c,d] = a[i,c,d]
    
m*=255    
print(m)

from PIL import Image


Image.fromarray(m).show()

