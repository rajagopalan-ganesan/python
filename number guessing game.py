import random
def num_gss():
    num="1234567890"
    while True:
        C_gss=random.choice(num)
        H_gss=input("Enter a number between 0 and 9 that might be a computer's guess: ")
        if H_gss==C_gss:
            print("YOU WON YOUR GUESS MATCHES THE COMPUTER's GUESS")
            break
        else:
            print("BETTER LUCK NEXT TIME...")
num_gss()            
