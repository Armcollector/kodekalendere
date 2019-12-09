def is_krampus2(n):
    p = str(n**2)
    for i in range(1,len(p)):
        a = int(p[:i])
        b = int(p[i:])
        if a and b and a+b == n:
            #print(f"{n} is a krampus because {a} + {b} = {n}")
            return True
    return False


def is_krampus(n):
    p = n**2

    i = 1
    c = 0
    while c < p and c >= 0:
        i *=10
        c = n *i - p%i *(i - 1)
        if c == n**2:
            return True
        
        
    return False


assert is_krampus(45)
#assert not is_krampus(100)

with open(r"C:\git\kodekalendere\knowit\Dag9\krampus.txt","r") as f:
    k = f.read()
    

import time
s_time = time.time()    
print(sum([int(i) for i in k.splitlines() if is_krampus(int(i))]))
print(time.time()-s_time)


