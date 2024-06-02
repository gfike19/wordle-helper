def StarterWord():
    f = open("words-left.txt", "r")
    wordsLeft = f.readlines()

def MainMenu():
    mainMenuChoice = int(input("""Welcome to Wordle Helper!\n1) Get a starter word\n2) Get possible guesses
    \n3) Remove word from list of possibles\n4)Exit program"""))

    if mainMenuChoice == 1:
        StarterWord()
    if mainMenuChoice == 2:
        Guesses()
    if mainMenuChoice == 3:
        RemoveWord()
    exit()