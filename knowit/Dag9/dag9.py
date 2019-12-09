def is_krampus(n):
    p = str(n**2)
    for i in range(1,len(p)):
        a = int(p[:i])
        b = int(p[i:])
        if a and b and a+b == n:
            print(f"{n} is a krampus because {a} + {b} = {n}")
            return True
    return False

assert is_krampus(45)
assert not is_krampus(100)

with open(r"C:\git\kodekalendere\knowit\Dag8\krampus.txt","r") as f:
    k = f.read()
    
sum([int(i) for i in k.splitlines() if is_krampus(int(i))])