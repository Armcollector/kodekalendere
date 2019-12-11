


def f(s,terrain):
    ice = 0
    fjell = False
    
    
    for d,t in enumerate(terrain,1):
        
        if t == 'I':
            ice +=1
            s += ice*12
        else:
            ice = 0
        
        if t == 'G':
            s-= 27
        
        if t == 'A':
            s-= 59
            
        if t == 'S':
            s-= 212
        
        if t == 'F':
            if fjell:
                s+= 35
                fjell = False
            else:
                s-= 70
                fjell = True
        if s < 0:
            return d
            
        
            
    
assert f(300,'IIGGFFAIISGIFFSGFAAASS') == 11


with open(r'C:\git\kodekalendere\knowit\dag11\terreng.txt','r') as fi:
    te = fi.read()


f(10703437, te)