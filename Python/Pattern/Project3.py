n = int(input("Enter a amount :"))

for i in range(1 , n + 1):
    for j in range(n - i):
        print(" " , end="")
    
    for k in range(1 , 2 * 1):
        print("*" , end="")
print()