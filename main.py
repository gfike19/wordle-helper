import secrets
import re
# TODO add quit at any time

def getWordsLeft():
    wordsLeft = []
    f = open('words-left.txt', 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        cleanWord = line.split()
        wordsLeft.append(cleanWord[0])
    
    return wordsLeft

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
        wordsLeft = getWordsLeft()
        randomWord = secrets.choice(wordsLeft)
        print(randomWord)
        getAnother = input("Get another word (y/n)? ").lower()
    MainMenu()

def Guesses():
    prompt1 = str('Enter letter number %s: ')
    prompt2 = str('Correct position? (y/n): ')
    userKnow = {}

    for i in range(0, 5):
        key = input(prompt1 %(str(i + 1)))
        val = input(prompt2)
        userKnow[key] = val
    
    usedLetters = input("Enter letters that aren't in the word: ")
    checkUsed = input('You entered %s.\nIs this correct? (y/n): ' %(usedLetters))
    if checkUsed.lower == 'y':
        usedLetters = input("Enter letters that aren't in the word: ")
    else:
        counter = 0
        knownIndex = {}
        outOfPlace = []
        for k,v in userKnow:
            if k != ' ' and v != 'n':
                knownIndex[counter] = k
            if k != ' ' and v == 'n':
                outOfPlace.append[k]
            else:
                knownIndex[counter] = '?'
            counter += 1
        prefix = "^start"  
        suffix = "end$"
        index = []
        outOfPlace = []
        for k,v in knownIndex:
            if v != '?':
                index.append(k)
            else:
                outOfPlace.append(v)
        index_checks = ''.join(f"(?=.{{{index}}}([{expected_chars}]))" for index in indexes)

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
        
if __name__ == "__main__":
    MainMenu()