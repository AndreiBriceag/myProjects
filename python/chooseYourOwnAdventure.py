
name = input("Type in your name: ")
print("Welcome to this adventure,", name+ "!")

answer1 = input("You were walking on a narrow path and have arrived at a crossway. You are forced to choose to go Left or Right. What do you choose? ").lower()

if answer1 == "left":
    answer2 = input("You come to a river. You can walk along the river to the nearest bridge or you can swim across it. (Type 'walk' or 'swim' to choose) ").lower()
    if answer2 == "walk":
        print("You walk along the river looking for a bridge to cross and you find a settlement.")
    elif answer2 == "swim":
        print("You try swimming across the river, but the current is too strong for you. You are dragged down the river and plunge to death in the waterfall!")
    else:
        print("You have to choose one of two the valid options!")
    
elif answer1 == "right":
    answer3 = input("You come to a cliff. You can go back to the river or you can try crossing on the rope bridge. (Type 'go back' or 'cross' to choose) ").lower()
    if answer3 == "go back":
        print("You go back to the river.")
    elif answer3 == "cross":
        answer4 = input("You cross the rope bridge and meet a stranger. Do you want to talk to the stranger? (Type 'yes' or 'no' to choose) ").lower()
        if answer4 == "yes":
            print("You talk to the stranger and he helps you get on the right track to civilisation!")
        elif answer4 == "no":
            print("You don't talk to the stranger. You get lost in the woods and you die!")
        else:
            print("You have to choose one of two the valid options!")
    else:
        print("You have to choose one of two the valid options!")
else:
    print("You have to choose one of two the valid options!")


print("Thank you for playing,", name+ "!")