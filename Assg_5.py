angle=int(input('Enter Angle:'))
base=int(input('Enter base length:'))
in_rad=angle*(3.14)/180
def fac(a):
    factorial=1
    for i in range(1,a+1):
        factorial=factorial*i
    return factorial
def cos(b):
    x=0
    p=1
    for i in range(10):
        x=x+((b**((2*i)))/fac((2*i))*p)
        p=p*(-1)
    return x
f=base/cos(in_rad)
g=((f**2)-(base**2))**(0.5)
print('Hypotenuse is:',f)
print('Perpendicular height is:',g)

