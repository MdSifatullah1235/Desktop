print("Enter a amount of numbers:")
n = int(input("Enter the amount:"))

count = 1

for i in range(1):
    for j in range(i + 1):
        print("{} ".format(count), end="")
        count +=1
    print()