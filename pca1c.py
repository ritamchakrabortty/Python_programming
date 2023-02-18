#3.Write a prog in python to calculate the Total salary for an employee from the folowing condition
    # hours     incentaive 
    # >=8        10 % of basic salary
    #>=10       20 % of basic salary
    #>=12       30 % of basic salary  
a=float(input("Enter basic salary: "))
b=float(input("Enter working hours: "))
if b>=8 and b<=10:
    print("Total salary :",a+a*0.1)
elif b>=10 and b<=12:
    print("Total salary :",a+a*0.2)
elif b>=12:
    print("Total salary :",a+a*0.3)
else:
    print("SYNTAX ERROR")


