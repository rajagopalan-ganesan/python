"""num=int(input("Enter a number:"))
for i in range(num,0,-1):
    print(" "*(i-1),"*"*(num-i+1))"""
num=int(input("Enter a number:"))
for i in range(1,num):
    print(" "*(num-i),"*"*(i-1))
