# Username generator like reddit
import random

with open("wordlist.txt", "r") as f:
    words = f.read().split("\n")

def user_gen(usernames_number = 1):
    """ Generates a random username (reddit style) """
    for i in range(usernames_number):
        name1 = random.choice(words).title()
        name2 = random.choice(words).title()
        str_number = str(random.randint(1, 100))    
        print(f"{name1}{name2}{str_number}")

user_gen(10) # Specify the number of usernames you want with *usernames_number* arg
