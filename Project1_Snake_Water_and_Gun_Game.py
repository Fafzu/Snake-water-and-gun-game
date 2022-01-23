import random


def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

# Check for all possibilities when Computer chose "s"
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

# Check for all possibilities when Computer chose "w"
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

# Check for all possibilities when Computer chose "g"
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


print("Comp turn: Snake(s) Water (w) or Gun(g)? .....?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

you = input("Your turn:- Snake(s) Water)(w) or gun(g)")
a = gameWin(comp, you)
print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("Congratulations!")
    print("You won this game")
    print("You will receive 25000 Rupees as you award")
    print("Your award will be directly sent to your vault")
    print("Thanks!")
else:
    print("You lose!")
