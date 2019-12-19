def is_palindrome(i):
    return str(i) == str(i)[::-1]

def hid_pal(i):
    n =  i + int(str(i)[::-1]) 
    return is_palindrome(n)


assert hid_pal(38)
assert not hid_pal(49)
sum( i for i in range(1,123454321+1) if  hid_pal(i) and not is_palindrome(i) )