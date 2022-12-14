n=list(input('Enter number:'))
n=[eval(i) for i in n]
z=['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
x=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
if len(n)==1 and n[0]==0:
    print('Zero')
elif len(n)==1:
    print(x[n[0]-1])       
elif len(n)==2 and n[0]==1:
    if n[1]==0:
        print('Ten')
    elif n[1]==1:
        print('Eleven')
    elif n[1]==2:
        print('Twelve')
    elif n[1]==3:
        print('Thirteen')
    elif n[1]==4:
        print('Fourteen')
    elif n[1]==5:
        print('Fifteen')
    elif n[1]==6:
        print('Sixteen')
    elif n[1]==7:
        print('Seventeen')
    elif n[1]==8:
        print('Eighteen')
    elif n[1]==9:
        print('Nineteen')
elif len(n)==2 and n[1]==0:
    print(z[n[0]-2])
elif len(n)==2 and n[1]!=0 and n[0]>1:
    print(z[n[0]-2]+' '+x[n[1]-1])


    