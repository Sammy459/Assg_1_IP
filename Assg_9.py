import math
def D(p):
    return math.e**(10-1.05*p)
def S(p):
    return math.e**(1+1.06*p)
i=1
while i<=10:
    e=D(i)
    f=S(i)
    i=i+0.01
    if e<f:
        print('Equilbrium price is:',i)
        print('Items being bought are:',e)
        print('Items being produced are:',f)
        break
    else:
        continue