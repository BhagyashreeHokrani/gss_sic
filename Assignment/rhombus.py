n = int(input("Enter size: "))

for i in range(n):
    # print spaces first (to shift stars like a rhombus)
    print(" " * (n - i - 1), end="")
    
    # then print stars
    print("* " * n)
