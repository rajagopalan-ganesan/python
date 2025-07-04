"""num=int(input("Enter a number:"))
for i in range(1,num,2):
    print(" "*((num-i)//2),"*"*i)
for i in range(num,0,-2):
    print(" "*((num-i)//2),"*"*i)"""

num=int(input("Enter a number:"))
for i in range(1,2*num,2):
    if (i<=num):
        print(" "*((num-i)//2),"*"*i)
    else:
        j=2*num-i
        print(" "*((num-j)//2),"*"*j)
        

    

