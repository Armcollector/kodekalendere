with open(r"C:\git\kodekalendere\knowit\dag16\fjord.txt", "r") as f:
    x = f.read()

#with open(r"C:\git\kodekalendere\knowit\dag16\testfjord.txt", "r") as f:
#    x = f.read()

antall, hoyde = len(x), len(x.splitlines())
print(hoyde)
import numpy as np

fjord = np.zeros( antall )


for i,c in enumerate(x):
    if c == '#':
        fjord[i]= 1
    elif c == 'B':
        fjord[i]= 2
    else: 
        fjord[i] = 0
    



a = fjord.reshape(hoyde,-1).transpose()

x,y = np.argwhere(a == 2)[0]
print(x,y)

for r in a:
    for i, c in enumerate(r):
        if c == 1:
            continue
        if i >= 2 and r[i-2] == 1:
            r[i] = 3
        if i < len(r)-2 and r[i+2] == 1:
            r[i] = 4

direction = [-1, 1]
n = True
turn = False
#from PIL import Image

#Image.fromarray(a*80).show()


s = 1
for e in range(x+1, len(a)):
    comment = ''
    
    
    if not turn:
        if n:
            x = e, 
            y = y-1
        else:
            x = e,
            y = y+1
    else:
        x = e
        y = y
        turn = False

    if n and (a[x,y-1] == 3 or a[x,y]==3):
        n = not n
        s+=1
        comment = 'prepare to turn south'
        turn = True
    elif not n and (a[x, y+1] == 4 or a[x, y] == 4) :
        s+=1
        n = not n
        comment = 'prepare to turn north'
        turn = True

    a[x,y] = 2

    print(e, "".join( [' ', '#', '/' if n else '\\','3','4'][int(i)] for i in a[x]), comment)

print(s)