val=int(input("Enter Number:"))
n=1
for i in range(1,val+1):
    print(" "*(val-i),end="")
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()

