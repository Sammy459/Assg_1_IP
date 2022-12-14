n=int(input('Enter number:'))
for i in range(n-1):
    print('*'*(i+1)+' '*(2*n-1-2*(i+1))+'*'*(i+1))
print("*"*(2*n-1))