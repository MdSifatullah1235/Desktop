a = int(input("Enter a number for the value (a): "))
b = int(input("Enter a number for the value (b): "))
c = int(input("Enter a number for the value (c): "))

if a == b and a == c:
    print("a, b, and c are equal")

elif a == b:
    if a > c:
        print("a and b are equal, but c is lower")
        
    else:
        print("a and b are equal, but c is greater")

elif b == c:
    if b > a:
        print("b and c are equal, but a is lower")

    else:
        print("b and c are equal, but a is greater")

elif a == c:
    if a > b:
        print("a and c are equal, but b is lower")

    else:
        print("a and c are equal, but b is greater")

else:
    if a > b and a > c:
        print("a is greater than b and c")

    elif b > a and b > c:
        print("b is greater than a and c")

    elif c > a and c > b:
        print("c is greater than a and b")