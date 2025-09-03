

Name_of_employee = input( "Enter your Name:")
EmpID = input(" Enter your Employee ID :")
Basic_monthly_salary = int(input("Enter your basiv monthly salary :"))
Special_Allowanace = int(input("Enter your monthly special allowanance :"))
Bonus_percentage = int(input("Enter your Annual Bonus as % of Gross Salary :" ))
Gross_monthly_salary = Basic_monthly_salary + Special_Allowanace
Anual_gross_salary = (Gross_monthly_salary * 12) + Bonus_percentage


print( f'The Name of the Employee is : {Name_of_employee}')
print(f' The Employee ID is : {EmpID}')
print(f' Employee Gross monthly salary is  : {Gross_monthly_salary}')
print ( f' Employee anual gross salary is :  {Anual_gross_salary}')

