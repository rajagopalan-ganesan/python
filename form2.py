try:

    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    p_num=int(input("Enter your Phone Number:"))
    loc=input("Enter your location:")
    course=input("Enter your desired course:")
    if course=="EEE":
        print("Your fee for the selected course is 120000 INR")
    elif course=='ECE':
        print("Your fee for the selected course is 450000 INR")
    elif course=="CSC":
        print("Your fee for the selected course is 600000 INR")   

except ValueError:

    print("Not a prop Value given")

except:

    print("Unknown Error")
    

finally:
    print("Thank You")    
    

    
   
