import secrets
# TODO add quit at any time

def RemoveWord():
    validInputList = {"y", "n"}
    f = open("words-left.txt", "r+", encoding='utf-8')
    wordsLeft = f.readlines()
    validInput = True
    getAnother = ""
    while validInput:
        removeWord = input("Enter word to remove: ") + "\n"
        quitCheck(removeWord)
        if removeWord not in wordsLeft:
            print("Word has already been removed. Try again.")
        else:
            wordsLeft.remove(removeWord)
            print('Word was succesfully removed!')
            getAnother = input("Remove another (y/n)? ").lower()
            quitCheck(getAnother)
            if getAnother == "n":
                validInput = False
            elif getAnother not in validInputList:
                getAnother = input("Invalid input. Type 'y' to try again or 'n' to return to the main menu: ").lower
                quitCheck(getAnother)
            
    # how to clear text in file
    f.truncate(0)
    f.writelines(wordsLeft)
    f.close()
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
    mainMenuChoice = int(input('''
    Welcome to Wordle Helper!
    1) Get a starter word
    2) Get possible guesses
    3) Remove word from list of possibles
    4) Exit program
    Press q at any time to quit\n>>> '''))

    if mainMenuChoice == 1:
        StarterWord()
    if mainMenuChoice == 2:
        Guesses()
    if mainMenuChoice == 3:
        RemoveWord()
    else:
        exit()

def quitCheck(userIput):
    if userIput.lower() == "q":
        exit()

MainMenu()