val=int(input("Enter a number:"))
for i in range(val,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
