#CAPTCHA:(Without random)
"""def CAPTCHA():
    CAPS={"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    SMAL={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    num={"0","1","2","3","4","5","6","7","8","9"}
    symbol={"@","!","#","$","&"}
    for a in CAPS:
        A=a
    for b in SMAL:
        B=b
    for c in num:
        C=c
    for d in symbol:
        D=d
    CAPTCHA= A+B+C+D
    print(CAPTCHA)
    CAP_VER=input("Re-write the above captcha in same way for authentication: ")
    if CAP_VER==CAPTCHA:
        print("Page loading..")
    else:
        print("Try again..")
        
CAPTCHA()"""



























#with random:
import random
def CAPTCHA():
        CAPS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        SMAL="abcdefghijklmnopqrstuvwxyz"
        num="1234567890"
        symbs="@#!$&"
        while True:
            a=random.choice(CAPS)
            b=random.choice(SMAL)
            c=random.choice(num)
            d=random.choice(symbs)
            c_list=[a,b,c,d]
            random.shuffle(c_list)
            CAPTCHA="".join(c_list)
            print(CAPTCHA)

            CAP_VER=input("Re-enter the above captcha for authentication:" )
            if CAP_VER==CAPTCHA:
                print("Page loading...")
                break
            else:
                print("Try again..generating new CAPTCHA")
CAPTCHA()        
        
    


































    
#




    
