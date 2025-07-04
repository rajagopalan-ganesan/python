#Employee:
c_name=input("Enter company name:")
e_name=input("Enter employee's name:")
e_ID=int(input("Enter employee ID:"))
print("Company name:",c_name)
print("Employee's name:",e_name)
print("Employee's ID:",e_ID)
c_use=input()
if(c_use== "there"):
    print("page loading...")
else:
    print("Sorry unathorised user")
a=int(input("Enter employee's no. of working days:"))
print("ok")
b=int(input("Enter salary per day of the employee:"))
print("ok")
c=int(input("ESI fund in percentge:"))
print("ok")
sal_wo_esi= a*b
sal_esi= sal_wo_esi-((c/100)*sal_wo_esi)
print("datas taken..")
print("Here is your salary form")
print("Company name:",c_name)
print("Employee's name:",e_name)
print("Employee's ID:",e_ID)
print("No. of working days:",a)
print("Salary per day:",b)
print("ESI fund:",c)
print("Total salary of employee",e_name,"of",c_name,"company is:",sal_esi)

    
