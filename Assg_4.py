import math
a=int(input('Start time:'))
b=int(input('End time:'))
def vel(a):
    c=(2000*(math.log(140000/(140000-2100*a))))-(9.8*a)
    return c
dist=0
d=(b-a)*4
for i in range(d):
    e=a+0.25*i
    f=b-0.25*(d-1-i)
    dist=dist+(((vel(e)+vel(f))/2)*0.25)
print('Distance travelled is:',dist)
