import random

userWins = 0
computerWins = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:
    userInput = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    if userInput == "q":
        break

    if userInput not in options:
        print("Type a valid option!")
        continue

    randomNumber = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computerPick = options[randomNumber]
    print("Computer picked " +computerPick+".")

    if userInput == "rock" and computerPick == "scissors":
        print("You win!")
        userWins +=1
        continue
    elif userInput == "paper" and computerPick == "rock":
        print("You win!")
        userWins +=1
        continue
    elif userInput == "scissors" and computerPick == "paper":
        print("You win!")
        userWins +=1
        continue
    elif userInput == computerPick:
        print("It's a draw!")
        draws +=1
        continue
    else:
        print("You lose!")
        computerWins +=1

print("You won", userWins, "times.")
print("Computer won", computerWins, "times.")
print("Draws: " +str(draws)+".")
print("Goodbye!")