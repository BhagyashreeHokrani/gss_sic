
# Check if a number is Perfect Square

User_input = int(input("Enter a number: "))

if User_input >= 0:
    # Take integer square root
    sqrt_val = int(User_input ** 0.5)
    
    if sqrt_val * sqrt_val == User_input:
        print(f"{User_input} is a perfect square.")
    else:
        print(f"{User_input} is not a perfect square.")
else:
    print("Please enter a non-negative number.")

        