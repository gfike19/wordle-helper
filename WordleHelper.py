import secrets
import re
import string
import sys

def exit_cli():
    print("Exiting...")
    sys.exit()

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
        if removeWord not in wordsLeft:
            print("Word has already been removed. Try again.")
        else:
            wordsLeft.remove(removeWord)
            print('Word was succesfully removed!')
            getAnother = input("Remove another (y/n)? ").lower()
            if getAnother == "n":
                validInput = False
            elif getAnother not in validInputList:
                getAnother = input("Invalid input. Type 'y' to try again or 'n' to return to the main menu: ").lower

            
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
    while True:
        # get what info the user knows about the word presently
        prompt2 = str('Correct position? (y/n)\nIf unknown enter "null": ')
        posDict = {}
        alpha = string.ascii_lowercase
        
        for i in range(0, 5, 1):
            inputStr1 = f'Enter letter number {i}.\nIf unknown enter "null": '
            k = input(inputStr1)
            v = input(prompt2)
            if k == 'null':
                if 'null' not in posDict.keys():
                    posDict['null' + str(i)] = 'null'
                else:
                    posDict['null'] = 'null'
            else:
                posDict[k] = v

        invalidLetters = input('Enter any letters that are NOT in the word: ')

        for char in invalidLetters:
            alpha = alpha.replace(char, '')
        
        # remove words that contain any of the invalid characters
        wordsLeft = getWordsLeft
        invalidRegex = rf"^(?!.*[{re.escape(invalidLetters)}]).*"
        guesses = [s for s in wordsLeft if re.match(invalidRegex, s)]
        # set up variables to create regex to match characters where the index is known and not
        userKnown = ''
        posRegex = r''

        for k,v in posDict.items():
            if v == 'y':
                posRegex.join(v)
            elif v == 'null':
                posRegex.join(('[' + alpha + ']'))
            elif v == 'n':
                userKnown += k
        
        # check for words that contains letters in wrong index
        userKnownRegex = rf"^(?=.*[{re.escape(userKnown)}]).*"
        guesses = [s for s in guesses if re.match(userKnownRegex, s)]
        
        # finally check for words that match the index/es the user knows
        guesses = [s for s in guesses if re.match(posRegex, s)]
        print("Guesses are: ", guesses)
        repeat = input('Repeat? (y/n): ')
        
        if repeat == 'n':
            break
    
    MainMenu()
    
def MainMenu():
    while True:
        mainMenuChoice = input('''
        Welcome to Wordle Helper!
        1) Get a starter word
        2) Get possible guesses
        3) Remove word from list of possibles
        4) Exit program
        Press q at any time to quit\n>>> ''')

        if mainMenuChoice == 'q':
            exit_cli()
        if mainMenuChoice == '1':
            StarterWord()
        if mainMenuChoice == '2':
            Guesses()
        if mainMenuChoice == '3':
            RemoveWord()
        
if __name__ == "__main__":
    MainMenu()