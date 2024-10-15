valid = False
x = int(input("Enter a Number :"))
try:
    while not valid:
        while x % 2 == 0:
            print("bye")
        valid = True
except ValueError:
    print("Invalid")
