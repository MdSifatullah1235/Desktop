try:
    num1 = int(input("Enter Your Age: "))

except ValueError:
    print("Wrong Value")

except:
    print("Wrong Input")

else:
    print("All Ok")
    