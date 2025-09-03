#Check if a year is Leap year
'''To check if a year is a leap year, it must be divisible by 4,
 but not divisible by 100, unless it is also divisible by 400.'''

User_input = int(input("Enter a year: "))
if (User_input % 4 == 0 and User_input % 100 != 0) or (User_input % 400 == 0):
    print(f"{User_input} is a leap year.")

    

