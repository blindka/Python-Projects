# beginner project for self learning - rock,paper and scissors

import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"] # options - variable, 3 index - rock, paper, scissors
while True:
    user_input = input("Choose one of options:\nRock\nPaper\nScissors\nor Q to quit:\n").lower()
    if user_input == "q":
        break #break from the if and ends the program
    
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    #0-2, 3 options: 0 - rock, 1 - paper, 2 - scissors
    computer_pick = options[random_number]
    print("The computer picked:", computer_pick + "." )

    if user_input == "rock" and computer_pick == "scissors":
        print("Rock beats scissors, You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("Paper beats rock, You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("Scissors beats paper, You won!")
        user_wins += 1
        continue
    else:
        print("",computer_pick+ "beats " ,user_input+ ", You Lost!")
        computer_wins += 1

print("You won:" ,user_wins, "times.")
print("Computer won:" ,computer_wins, "times.")

