n = int(input("Enter number of rows: "))

for i in range(n):
    num = 1
    print(" " * (n - i), end="")   # spaces for alignment
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)   # formula for next value in row
    print() 
