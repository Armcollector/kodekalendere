import numpy 

def primesfrom2to_np(n):
    if n == 2:
        return [2]
    if 3 <= n <= 4:
        return [2, 3]
    if n == 5:
        return [2, 3, 5]

    sieve = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    arr = numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]
    return arr

ps = primesfrom2to_np(1000740+1)

alver = [1,0,0,0,0]
step = 1
i = 0

fremover = True

def one_smallest():
    _min = min(alver)
    return alver.count(_min) == 1

def neste():
    global i
    return (i+ [-1,1][fremover])%5

def rule1_valid():
    if step not in ps:
        return False
    if not one_smallest():
        return False
    
    return True

def rule1():
    global i
    _min = min(alver)
    i = alver.index(_min)
    alver[i] +=1
    #print(f"{i+1} does step {step}, rule 1")

def rule2_valid():
    if step % 28 == 0:
        return True
    return False
    
def rule2():
    global i, fremover
    fremover = not fremover
    i = neste()
    alver[i] += 1
    #print("rule 2")
    #print(f"{i+1} does step {step}, rule 2")

def rule3_valid():
    if step %2 == 1:
        return False
    neste_alv = neste()
    if alver[neste_alv] == max(alver) and alver.count(max(alver)) == 1:
        return True
    return False

def rule3():
    global i
    i = neste()
    i = neste()
    alver[i] += 1
    #print("rule 3")
    #print(f"{i+1} does step {step}, rule 3")
    
def rule4_valid():
    if step%7 == 0:
        return True
    return False

def rule4():
    global i
    i = 4
    alver[i] +=1
    #print("rule 4")
    #print(f"{i+1} does step {step}, rule 4")

def rule5():
    global i
    i = neste()
    alver[i]+=1
    #print("rule 5")
    #print(f"{i+1} does step {step}, rule 5")
    
    
while step < 1000740:
    step +=1
    
    #print(alver)
    
    if rule1_valid():
        rule1()
    elif rule2_valid():
        rule2()
    elif rule3_valid():
        rule3()
    elif rule4_valid():
        rule4()
    else:
        rule5()
    
   

max(alver)-min(alver)