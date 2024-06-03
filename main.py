import secrets

def StarterWord():
    getAnother = "y"
    while getAnother == "y":
        f = open("words-left.txt", "r+")
        wordsLeft = f.readlines()
        f.close()
        randomWord = secrets.choice(wordsLeft)
        print(randomWord)
        getAnother = input("Get another word (y/n)? ").lower()
    MainMenu()

# def RemoveWord():
            # how to clear text in file
        # f.truncate(0)

def MainMenu():
    mainMenuChoice = int(input("""
    Welcome to Wordle Helper!
    1) Get a starter word
    2) Get possible guesses
    3) Remove word from list of possibles
    4)Exit program\n"""))

    if mainMenuChoice == 1:
        StarterWord()
    if mainMenuChoice == 2:
        Guesses()
    if mainMenuChoice == 3:
        RemoveWord()
    else:
        exit()

MainMenu()