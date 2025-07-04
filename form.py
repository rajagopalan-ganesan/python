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
try:
    affirmation=input("Type yes or no:").lower()
    if affirmation not in ["yes","no"]:
        print('Entered value cant be taken.Try again with a valid one')
    elif affirmation=="yes":
        print("You have joined your course thankyou XD")
    else:
        print("No Pressure take care...")

finally:
    print("Thank You")    
    

    
   
