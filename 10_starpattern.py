n = int(input("Enter the number of lines :"))
for i in range(n):
    print("*" * (i+1))

#second type of pattern
for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (2*i-1),end="")
    print(" " * (n-i-1))