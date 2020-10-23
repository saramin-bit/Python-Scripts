"""
Program for a matchstick game being played between the computer and a user. Your program should ensure that the 
computer always wins. Rules for the game are as follows:
- There are 21 matchsticks.
- The computer asks the player to pick 1, 2, 3, or 4 matchsticks.
- After the person picks, the computer does its picking.
- Whoever is forced to pick up the last matchstick loses the game.
"""
ms = 21
n = 0

print("\n\t\t\tMATCHSTICK GAME")

print("\nRULES")
print("- There are 21 matchsticks.")
print("- The computer asks the player to pick 1, 2, 3, or 4 matchsticks.")
print("- After the person picks, the computer does its picking.")
print("- Whoever is forced to pick up the last matchstick loses the game.\n")

print("Pick 1, 2, 3, or 4 matchsticks : ")

while(ms>1):
    print("\nUser Pick       : ", end="")
    n = int(input())
    if(n>=1 and n<=4 and ms>=1):
        print("Computer pick   : ",5-n)
        ms-=5
        print("Matchstick left : ",ms)
    else:
        print("Invalid Selection")

while(ms>0):
    print("\nUser Pick       : ", end="")
    n = int(input())
    if(n==1):
        print("You lost the game...  :(")
        ms-=1
    else:
        print("Invalid Selection :(")
