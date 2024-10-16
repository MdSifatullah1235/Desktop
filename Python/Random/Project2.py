import random
while True:
    user_choice = input("Enter a choice (rock/paper/scissors) :")

    choices = ["rock","paper","scissors"]
    sys_choice = random.choice(choices)
    
    print(f"You chose {user_choice} System Chose {sys_choice}")

    if user_choice == sys_choice:
        print(f"You Both Chose {user_choice} It's A Tie")

    elif user_choice == "rock":
        if sys_choice == "scissors":
            print("Rock Beats Scissors You Win")
        else:
            print("Paper Beats Rock You Lose")

    elif user_choice == "paper":
        if sys_choice == "rock":
            print("Paper Beats Rock You Win")
        else:
            print("Scissors beat Paper You Lose")

    elif user_choice == "scissors":
        if sys_choice == "paper":
            print("Scissors Beat Paper You Win")
        else:
            print("Rock Beats Scissors You Lose")

    play_again = input("Wanna Play Again (y/n):")
    if play_again == "n":
        print("Oh.. Ok")
        break
    else:
        print("Let's Play Again")