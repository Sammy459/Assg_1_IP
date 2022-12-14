cost=int(input('Cost of laptop is:'))
allowance=int(input('Allowance per month is:'))
sf=float(input('Fraction of allowance saved is:'))
r=float(input('Rate of interest is:'))
sum=allowance*sf
t=1
while sum<cost:
    sum=sum*(1+(r/100))
    sum=sum+allowance*sf
    t=t+1
print('Number of months needed are',t)
print('Amount left is',sum-cost)