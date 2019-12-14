a = [2,3,5,7,11]
index = 1
antall = 1
s = [2,2]

while len(s) < 217532235:
    t = s[antall]
    s += [a[index]]*t
    antall +=1
    index = (index +1)%len(a)
    
    
print(len(s))
print(s.count(7)*7)