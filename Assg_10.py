def val(x):
    return x**3-10.5*x**2+34.5*x-35
x0=float(input())
def dx(x):
    return 3*x**2-21*x+34.5
x=x0
while x0<=x:
    x=x0-val(x0)/dx(x0)
    if round(x0,2)==round(x,2):
        print(x)
        break    
    x0=x
        