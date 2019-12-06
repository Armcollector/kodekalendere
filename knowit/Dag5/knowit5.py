s=input()
l=len(s)
q=l//2
print("".join(s[l-6-3*((i+q)%l//3)+[4,3,0,8,5,4][(i+q)%6]] for i in range(l)))