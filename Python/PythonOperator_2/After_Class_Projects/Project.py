a = 10
b = 10
c = 10

if a > b and a > c:
    print("a is greater than b and c")

elif b > a and b > c:
    print("b is greater than a and c")

elif c > a and c > b:
    print("c is greater than a and b")

elif a == b and a == c:
    print("a, b and c are equals")

elif a == b and a > c:
    print("a and b are equals but c is lower")

elif b == c and b > a:
    print("b and c are equals but a is lower")

elif a == c and a > b:
    print("a and c are equals but b is lower")

elif a == b and a < c:
    print("a and b are equals but c is greater")

elif b == c and b < a:
    print("b and c are equals but a is greater")

elif a == c and a < b:
    print("a and c are equals but b is greater")