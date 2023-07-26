import random

topOfRange = input("Type a number: ")

if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    
    if topOfRange <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type an actual number.")
    quit()

randomNumber = random.randint(1,topOfRange)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Make a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    elif userGuess <= 0:
        print("Please type a number greater than 0.")
        continue
    else:
        print("Please type an actual number.")
        continue

    if userGuess == randomNumber:
        print("You guessed it!")
        break
    elif userGuess > randomNumber:
        print("You guessed ABOVE the number!")
    else:
        print("You guessed BELOW the number!")

print("You guessed it in", guesses, "tries!")