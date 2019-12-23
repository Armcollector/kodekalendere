import numpy

# stjålet, veldig rask implemtasjon av sieve
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    arr = primesfrom2to_np(n)
    return [int(i) for i in arr]


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

    
    
  

def sumdig(n):
    sumdig = 0
    while n > 0:
        sumdig += n % 10
        n = n // 10
    return sumdig


def harshadprimtall(n,ps):
    s = sumdig(n)
    return n%s == 0 and s in ps


if __name__ == '__main__':
    ps = set(primesfrom2to(98765432+1))

    c = 0
    for i in range(1,98765432+1):
        if i%10000 == 0:
            print(i)
        if harshadprimtall(i,ps):
            c += 1
    print(c)
    