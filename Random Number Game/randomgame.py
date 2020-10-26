import random
randomnumber=random.randint(0,100)
count=5
print("Total attempts is ",count)
def WinningSection():
    print("Voila!! you won the game.\n")

def LosingSection():
    print("ohh!!! You Lose The Game :( ")
while count != 0:
    Guess=input("Enter Your Guess: ")
    if randomnumber == int(Guess):
        WinningSection()
        a=input("Do you wanna continue, give your answer only yes or no: ")
        if a =='yes' :
            randomnumber=random.randint(0,100)
            count=5
            continue
        else :
            exit()
    elif randomnumber > int(Guess) :
        print("OOPS!! your guess is low.")
        count-=1
        print(count,"attempts remain")
    elif randomnumber < int(Guess) :
        print("OOPS!! your guess is high")
        count-=1
        print(count,"attempts remain")
    if count == 1:
        ask=input("You wanna some help, give your answer only yes or no: ")
        if ask == 'yes':
            answer=100+randomnumber
            print("your answer behind number",answer)
        else:
            continue
    elif count == 0:
        LosingSection()
        a=input("Do you wanna Try Again, give your answer only yes or no: ")
        if a =='yes' :
            randomnumber=random.randint(0,100)
            count=5
            continue
        else :
            exit()
