def list_sum(x):
    sum=0
    for i in x:
        sum=sum+i
    return sum
pop=[50,1450,1400,1700,1500,600,1200]
n=int(input('Enter number of years:'))
r=2.5
tot_sum=list_sum(pop)
c=0
total_pop=0
if n==1:
    print('The population in year 1 is:',tot_sum)
else:
    print('The population in year 1 is:',tot_sum)
    for i in range(n):
        total_pop=tot_sum
        for j in range(7):
            pop[j]=pop[j]*(1+(r-0.4*j)/100)
        tot_sum=list_sum(pop)
        print('The population in year',str(i+2),'is:',tot_sum)
        if total_pop<tot_sum:
            c=tot_sum
        r=r-0.1
if n<13:
    print('The max population has not been reached')
else:
    print('The max population is',c)
    print('The max population has reached after 13 years')
