
print("Welcome to my Quiz!")

gamePlay = input("Do you want to play? ").lower()

if gamePlay == "yes" or gamePlay == "y":
    print("okaaay, let's go!")
else:
    print("not ok :(")

score = 0

answer1 = input("What does PSU stand for? ").lower()
if answer1 == "power supply unit":
    print("That's correct!")
    score +=1
else:
    print("Wrong!!")

answer2 = input("What does USB stand for? ").lower()
if answer2 == "universal serial bus":
    print("That's correct!")
    score +=1
else:
    print("Wrong!!")

answer3 = input("What does AMD stand for? ").lower()
if answer3 == "advanced micro devices":
    print("That's correct!")
    score +=1
else:
    print("Wrong!!")

answer4 = input("What does SSD stand for? ").lower()
if answer4 == "solid state drive":
    print("That's correct!")
    score +=1
else:
    print("Wrong!!")

answer5 = input("What does HDD stand for? ").lower()
if answer5 == "hard disk drive":
    print("That's correct!")
    score +=1
else:
    print("Wrong!!")


print("You answered " + str(score) + " questions correctly!")
percentage = score/5*100
if percentage < 50:
    print("Not so good, that's " + str(score/5*100) + "%.")
elif percentage >= 50:
    print("Great! That's " + str(score/5*100) + "%!")
