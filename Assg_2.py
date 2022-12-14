def y3(x):
    return 200-4*x
M=int(input('Enter value of M:'))
l=0
k=0
n=0
z=0
l1=[]
for i in range(100000):
    y1=200-4*i
    y2=120-2*i
    if y1==0 or y2==0:
        l=i
        break
    elif y1==y2:
        k=i
    elif i==0:
        n=min(y1,y2)
l2=[[0,0],[l,0],[k,y3(k)],[0,n]]
for i in l2:
    if i[0]<=M and i[1]<=M:
        z=90*i[0]+25*i[1]
        l1.append(z)
    elif i[0]<=M and i[1]>=M:
        z=90*i[0]+(i[1]-M)*30+M*25
        l1.append(z)
    elif i[0]>=M and i[1]<=M:
        z=(i[0]-M)*100+M*90+i[1]*25
        l1.append(z)
    elif i[0]>=M and i[1]>=M:
        z=(i[0]-M)*100+M*90+(i[1]-M)*30+M*25
        l1.append(z)
print('Maximum profit is:',max(l1))
print('No of tables prodcued are:',l2[l1.index(max(l1))][0])
print('No of chairs produced are:',l2[l1.index(max(l1))][1])

        
