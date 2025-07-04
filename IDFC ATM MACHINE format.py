#IDFC BANK
print("             IDFC BANK")
print("1.Cash Withdraw    2.Balance Enquiry")
print("3.Deposit amount   4.Statement")

opt=int(input("Select option:"))
if opt==1:
     A_num=input("Enter your account number:")
     if len(A_num)in range(10,16):
        A_pass=input("Enter your account password:")
        if len(A_pass)==4:
             amnt=int(input("Enter the amount that you want to with draw without comma's:"))
             if(amnt<=50000):
                  print("Amount withdrawen:",amnt , "\nMain Balance:",50000-amnt,"\n   THANK YOU   ")
        
             else:
                   print("Insufficient Bank Balance")
    
        
   
        else:
            print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
            A_pass=input("Enter your account password again:")
            if len(A_pass)==4:
             amnt=int(input("Enter the amount that you want to with draw without comma's:"))
             if(amnt<=50000):
                  print("Amount withdrawen:",amnt , "\nMain Balance:",50000-amnt,"\n   THANK YOU   ")
        
             else:
                   print("Insufficient Bank Balance")
    
            else:
                 print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
                 A_pass=input("Enter your account password again:")
                 if len(A_pass)==4:
                        amnt=int(input("Enter the amount that you want to with draw without comma's:"))
                        if(amnt<=50000):
                            print("Amount withdrawen:",amnt , "\nMain Balance:",50000-amnt,"\n   THANK YOU   ")
                        else:
                            print("Insufficient Bank Balance")     
        
          
                 
            
    
                 else:
                       print("YOUR ACCOUNT IS BLOCKED.Aproach your nearest bank imedietly to unblock. If not done within 48 hours? \n YOUR ACCOUT WILL BE TERMINATED")
                       A_pass=input("Enter your account password again:")      
          
     else:
         print("INVALID ACCOUNT NUMBER. TRY AGAIN WITH VALID ONE.")
        
            
            
    
elif opt==2:
    A_num=input("Enter your account number:")
    if len(A_num)in range (10,16):
        A_pass=input("Enter your account password:")
        if len(A_pass)==4:
              print("You have Rs",50000,"in your Bank account")
              print("             THANK YOU                   ")
        else:
            print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
            A_pass=input("Enter your account password again:")
            if len(A_pass)==4:
              print("You have Rs",50000,"in your Bank account")
              print("             THANK YOU                   ")
            else:
                 print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
                 A_pass=input("Enter your account password again:")
                 if len(A_pass)==4:
                        print("You have Rs",50000,"in your Bank account")
                        print("             THANK YOU                   ")
                 else:
                       print("YOUR ACCOUNT IS BLOCKED.Aproach your nearest bank imedietly to unblock. If not done within 48 hours? \n YOUR ACCOUT WILL BE TERMINATED")
                            
          
    else:
        print("INVALID ACCOUNT NUMBER. TRY AGAIN WITH VALID ONE.")
        
            
            
                

  
elif opt==3:
    A_num=input("Enter your account number:")
    if len(A_num)in range (10,16):
        A_pass=input("Enter your account password:")
        if len(A_pass)==4:
             d_amnt=int(input("Enter the amount that you want to deposit without comma's:"))
             print("Amount deposited:",d_amnt , "\nMain Balance:",50000+d_amnt,"\n   THANK YOU   ")
        else:
            print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
            A_pass=input("Enter your account password again:")
            if len(A_pass)==4:
                d_amnt=int(input("Enter the amount that you want to deposit without comma's:"))
                print("Amount deposited:",d_amnt , "\nMain Balance:",50000+d_amnt,"\n   THANK YOU   ")
                
             
            else:
                 print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
                 A_pass=input("Enter your account password again:")
                 if len(A_pass)==4:
                       d_amnt=int(input("Enter the amount that you want to deposit without comma's:"))
                       print("Amount deposited:",d_amnt , "\nMain Balance:",50000+d_amnt,"\n   THANK YOU   ")
                 else:
                       print("YOUR ACCOUNT IS BLOCKED.Aproach your nearest bank imedietly to unblock. If not done within 48 hours? \n YOUR ACCOUT WILL BE TERMINATED")
                       A_pass=input("Enter your account password again:")      
          
    else:
        print("INVALID ACCOUNT NUMBER. TRY AGAIN WITH VALID ONE.")
        
            
    
elif opt==4:
    A_num=input("Enter your account number:")
    if len(A_num)in range (10,16):
        A_pass=input("Enter your account password:")
        if len(A_pass)==4:
               print("    ...STATEMENT PRINTING...     ")
        else:
            print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
            A_pass=input("Enter your account password again:")
            if len(A_pass)==4:                
                print("    ...STATEMENT PRINTING...     ")
            else:
                 print("Incorect password try again..\n WARNING!! If entered wrong for the 3rd time your account will be blocked")
                 A_pass=input("Enter your account password again:")
                 if len(A_pass)==4:
                         print("    ...STATEMENT PRINTING...     ")
                 else:
                       print("YOUR ACCOUNT IS BLOCKED.Aproach your nearest bank imedietly to unblock. If not done within 48 hours? \n YOUR ACCOUT WILL BE TERMINATED")
                       A_pass=input("Enter your account password again:")      
          
    else:
        print("INVALID ACCOUNT NUMBER. TRY AGAIN WITH VALID ONE.")
        
   
else:
    print("Invalid Value selected. Try again")
    
    
    
    
