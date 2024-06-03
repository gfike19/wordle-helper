import secrets
# TODO add quit at any time
# TODO actually remove word from list and rewrite file

def RemoveWord():
    getAnother = "y"
    f = open("words-left.txt", "r+")
    wordsLeft = f.readlines()
    f.close()
    while getAnother == "y":
        removeWord = input("Enter word to remove: ")
        if not [s.lstrip().rstrip() for s in wordsLeft if removeWord in s]:
            print(wordsLeft.count(removeWord))
            print("Invalid input. Try again.")
        else:
            wordsLeft.remove(wordsLeft.index(s))
            getAnother = input("Remove another (y/n)? ").lower()
        # how to clear text in file
        # f.truncate(0)
    MainMenu()

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

def MainMenu():
    mainMenuChoice = int(input("""
    Welcome to Wordle Helper!
    1) Get a starter word
    2) Get possible guesses
    3) Remove word from list of possibles
    4) Exit program\n>>> """))

    if mainMenuChoice == 1:
        StarterWord()
    if mainMenuChoice == 2:
        Guesses()
    if mainMenuChoice == 3:
        RemoveWord()
    else:
        exit()

MainMenu()