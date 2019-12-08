from collections import deque

x = """PLUSS101, OPP7, MINUS9, PLUSS101
TREKK1FRAODDE, MINUS1, MINUS9, PLUSS1TILPAR
PLUSS1TILPAR, PLUSS4, PLUSS101, MINUS9
MINUS9, PLUSS101, TREKK1FRAODDE, MINUS1
ROTERODDE, MINUS1, PLUSS4, ROTERALLE
GANGEMSD, PLUSS4, MINUS9, STOPP
MINUS1, PLUSS4, MINUS9, PLUSS101
PLUSS1TILPAR, MINUS9, TREKK1FRAODDE, DELEMSD
PLUSS101, REVERSERSIFFER, MINUS1, ROTERPAR
PLUSS4, GANGEMSD, REVERSERSIFFER, MINUS9""".replace(' ','')

m = [deque(i.split(',')) for i in x.splitlines()]

m


def msd(n):
    n = abs(n)
    return int(str(n)[0])

def roterodde(n):
    for i in range(1,len(m),2):
        m[i].rotate(-1)
    return n

def trekk1fraodde(n):
    return int("".join(str(int(i) -1) if i != '-' and int(i)%2 else i for i in str(n)))

assert trekk1fraodde(123) == 22
assert trekk1fraodde(-1234) == -224

def pluss1tilpar(n):
    return int("".join(str(int(i)+1) if int(i)%2==0 else i for i in str(n)))

def opp7(n):
    while abs(n)%10 != 7:
        n+=1
    return n

assert opp7(-13) == -7

def roteralle(n):
    for i in m:
        i.rotate(-1)
    return n

def roterpar(n):
    for i in range(0,len(m),2):
        m[i].rotate(-1)
    return n


op = {'MINUS1' : lambda x: x-1,
      'GANGEMSD': lambda x: x*msd(x),
      'PLUSS4' : lambda x: x+4,
      'MINUS9' : lambda x: x -9,
      'ROTERODDE': roterodde,
      'TREKK1FRAODDE' : trekk1fraodde,
      'PLUSS1TILPAR' : pluss1tilpar,
      'PLUSS101' : lambda x:  x+101,
      'OPP7': opp7,
      'REVERSERSIFFER' : lambda x: int(str(n)[::-1]) if n >= 0 else -1*int(str(abs(n))[::-1]),
      'ROTERALLE': roteralle,
      'DELEMSD': lambda x: x // msd(x),
      'ROTERPAR': roterpar,
      'STOPP' : lambda x: x
}

for s in range(1,11):
    m = [deque(i.split(',')) for i in x.splitlines()]
    n = s
    print(f"running {s} coins")
    while True:
        c = n%10
        #print(f"Fra hjul {c}, operasjon {m[c][0]}")
        n = op[m[c][0]](n)
        if m[c][0] == 'STOPP':
            break
        m[c].rotate(-1)
    
    print(s,n)