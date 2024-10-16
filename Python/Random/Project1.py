import random
number = input("Enter a number:")
play = True
guess = str(random.randint(10,20))

print("I will generate a number from 10 to 20 Try to guess it!")

while play:
    if number == guess:
        print("You guessed it!")
        print("The Number Was",number)
        break
    else:
        print("Try Again")
