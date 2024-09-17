inp = int(input("Enter a number : "))

power = inp ** inp

for b in range(inp): 
    power += b
    print("Power :", power)


print("Total Power :", power)