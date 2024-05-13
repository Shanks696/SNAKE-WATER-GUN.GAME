import random

print("Hello, welcome to snake water gun game")
print("you need to choose from (Snake, Water, Gun) :")
A = ("snake","water","gun")

for i in range(5):
    B = input("your choice : ")
    a = random.choice(A)
    while True:
        if B == "snake" and a == "water":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("You won,Snake drank water")
            break
        elif B == "water" and a == "gun":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("You won,Gun submerged in water")
            break
        elif B == "gun" and a == "snake":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("You won,Gun shot snake")
            break
        elif B == "water" and a == "snake":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("Try again, snake drank the water")
            break
        elif B == "snake" and a == "gun":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("Try again,Gun shot snake")
            break
        elif B == "gun" and a == "water":
            print("Computer choice :", a)
            print("Your choice :", B)
            print("Try again, gun submerged in water")
            break
        else:
            print("Computer choice :", a)
            print("Choose different from computer")
            break
