#manual slicing of strings:
string=input("Enter the sentence that you want to slice:")
start=int(input("Enter the starting value:"))
End=int(input("Enter the ending value:"))
skip=int(input("Enter how much times you want to increament or skip:"))
print("Your string have been sliced in the terms of how u wanted it:")
if End>len(string):
    print("Give a valid ending of the slicing")
print(string[start:End:skip])
print("                     THANK YOU")
