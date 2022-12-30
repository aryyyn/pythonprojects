import os

def check():
    global counter
    counter += 1
    if counter > 10:
        print("You have exceeded the maximum number of attempts. Game over.")
        return

    print("Enter any letter: ")
    letter = input()
    if len(letter) > 1:
        print("You cannot enter more than one letter! ")
        check()
    elif letter in word:
        print(letter + " is correct!")
        if all(char in guessed_letters for char in word):
            print("You won!")
            return
        else:
            check()
    else:
        print(letter + " is incorrect")
        draw_hangman(counter)
        check()

def draw_hangman(incorrect_guesses):
    hangman_diagrams = [
        """
          ________
          |      |
          |      
          |    
          |      
          |
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |    
          |      
          |
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |      |
          |      |
          |
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |     \|
          |      |
          |
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |     \|/
          |      |
          |
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |     \|/
          |      |
          |     /
        _ _ _
        """,
        """
          ________
          |      |
          |      O
          |     \|/
          |      |
          |     / \\
        _ _ _
        """
    ]
    print(hangman_diagrams[incorrect_guesses])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("For player 1")
word = input("Enter any word for player 2 to guess: ")
guessed_letters = []
counter = 0

clear()

print("For player 2")
check()
