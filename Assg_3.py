x=x0=int(input('X coordinate:'))
y=y0=int(input('Y coordinate:'))
i=1
c=0
while i>0:
    a=int(input('Distance moved:'))
    c=c+a
    i=a
    if 1<=a<=25:
        y=y+a
    elif 26<=a<=50:
        y=y-a
    elif 51<=a<=75:
        x=x+a
    elif a>=76:
        x=x-a
print('Final coordinates are:',str(x)+','+str(y))
print('Total distance travelled is:',c)
print('Net displacement is:',(((x-x0)**2)+((y-y0)**2))**(0.5))