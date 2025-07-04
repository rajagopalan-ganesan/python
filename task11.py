'''val=int(input("Enter a value:"))
for i in range(1,val):
    print(str(i)*i)'''    
val=int(input("Enter a value:"))
for i in range(0,val+1):
    for j in range(0,i+1):
        print(str(i)*j,sep=" ")
