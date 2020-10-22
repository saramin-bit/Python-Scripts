"""
Both players are given the same string, S. Both players have to make substrings using the letters of the string S. Stuart has to make words starting with consonants. Kevin has to make words starting with vowels. The game ends when both players have made all possible substrings.
A player gets +1 point for each occurrence of the substring in the string S.

For Example

String S = BANANA Kevin's vowel beginning word = ANA Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. For better understanding, see the image below:
"""

"""
Input Format
A single line of input containing the string S. Note: The string S will contain only uppercase letters: [ A- Z ]

Constriants

0 < len(S) <= 10^6

Output Format
Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

"""


def Minion_Game(word):
    word = word.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    Player1 = len([word[i:n] for i in range(len(word))
                   if word[i] in vowels for n in range(len(word), i, -1)])
    Player2 = len([word[i:n] for i in range(
        len(word)) if word[i] not in vowels for n in range(len(word), i, -1)])
    if Player2 > Player1:
        return 'Player2 won with ' + str(Player2) + " Points"
    elif Player1 > Player2:
        return 'Player1 won with ' + str(Player1) + " Points"
    else:
        return 'Draw'


print(Minion_Game("banana"))  # Player2 won with 12 Points
