import secrets

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
        f = open("words-left.txt", "r+", encoding="utf-8")
        wordsLeft = f.readlines()
        f.close()
        randomWord = secrets.choice(wordsLeft)
        print(randomWord)
        getAnother = input("Get another word (y/n)? ").lower()
        quitCheck(getAnother)
    MainMenu()

def MainMenu():
    mainMenuChoice = int(input('''
    Welcome to Wordle Helper!
    1) Get a starter word
    2) Get possible guesses
    3) Remove word from list of possibles
    4) Exit program
    Press 'qq' at any time to quit\n>>> '''))

    if mainMenuChoice == 1:
        StarterWord()
    if mainMenuChoice == 2:
        Guesses()
    if mainMenuChoice == 3:
        RemoveWord()
    else:
        exit()

def quitCheck(userIput):
    if userIput.lower() == "qq":
        exit()

def Guesses():
    correctPosPhrase = "Is the letter in the correct position (y/n)? " 
    getNextLetterPhrase = "Enter letter number {num}. Leave blank if no letter is known: "
    userGuess = {}
    for i in range(1, 6):
        posDict = {"y": True, "n": False}
        char = input(str.format(getNextLetterPhrase, i)).lower
        quitCheck(char)
        validPos = input(correctPosPhrase).lower
        quitCheck(char)
        userGuess[char] = posDict.get(validPos)
    f = open("words-left.txt", "r+", encoding='utf-8')    
    # wordsLeft = f.readlines()
    f.close()


MainMenu()