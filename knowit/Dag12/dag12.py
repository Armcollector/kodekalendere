def f(x):
    if not x or x == 6174:
        return 0
    a = int("".join(sorted(f"{x:04}", reverse=True)))
    b = int("".join(sorted(f"{x:04}", reverse=False)))
    
    return f(a-b)+1


( f(i) for i in range(1000,10000)).count(7)