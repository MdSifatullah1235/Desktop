inp = int(input("Enter your age :"))

if inp >= 10:
    if inp > 20:
        print("Your older than 20 you cannot enter")
        if inp >= 40:
            print("Also your very old ")

    else:
        print("You can enter")

else:
    print("Your too younger than 10 you cannot enter")
    if inp > 5:
        print("Also you are a little kid")