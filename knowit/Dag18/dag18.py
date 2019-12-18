from itertools import accumulate
import operator



with open(r'C:\git\kodekalendere\knowit\dag18\names.txt','r') as file:
    navn = file.read()
    
malefirst, femalefirst, last1, last2 = [  i.splitlines() for i in navn.split('---') ]
femalefirst = [i for i in femalefirst if i]
last1 = [i for i in last1 if i]
last2 = [i for i in last2 if i]


def splitlast(name):
    l = len(name)
    if l%2 == 0:
        return name[:l//2], name[l//2:]
    else:
        return name[:l//2+1], name[l//2+1:]

assert splitlast('Joha') == ('Jo','ha')
assert splitlast('Johan') == ('Joh','an')
    
def pick(firstname, lastname, gender):
    
    n = sum( ord(i) for i in firstname)
    s = ""
    if gender == 'M':
        s+= malefirst[n%len(malefirst)]
    else:
        s+= femalefirst[n%len(femalefirst)]
    
    e1,e2 = splitlast(lastname)
    n2= sum( ord(i) - ord('A')+1 for i in e1.upper() )
    s += " " + last1[n2%len(last1)]
    
    n2 = list(accumulate((ord(i) for i in e2) , operator.mul))[-1]
    
    if gender == 'M':
        n2*= len(firstname)
    else:
        n2*= (len(firstname)+len(lastname))
    
    s+= last2[int("".join(sorted(str(n2), reverse=True)))%len(last2)]
        
    return s

assert pick('Jan','Johannsen','M') == 'Poe Lightverse'

with open(r'C:\git\kodekalendere\knowit\dag18\ansatt.csv','r') as file:
    ansatt = file.read()

from collections import Counter

Counter([ pick(*i.split(',')) for i in ansatt.splitlines()]).most_common()

assert Counter([ pick(*i.split(',')) for i in ansatt.splitlines()]).most_common()[0][0] == 'Malkili Deathfire'