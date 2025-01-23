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
        rawDict = {}
        alpha = string.ascii_lowercase
        
        for i in range(0, 5, 1):
            inputStr1 = f'Enter letter number {str(i + 1)}.\nIf unknown enter "null": '
            k = input(inputStr1)
            v = input(prompt2)
            if k == 'null':
                if 'null' not in rawDict.keys():
                    rawDict['null' + str(i)] = 'null'
                else:
                    rawDict['null'] = 'null'
            else:
                rawDict[k] = v

        invalidLetters = input('Enter any letters that are NOT in the word: ')

        for char in invalidLetters:
            alpha = alpha.replace(char, '')
        
        # remove words that contain any of the invalid characters
        wordsLeft = []
        f = open('all-words.txt', 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            words = line.split()
            for word in words:
                wordsLeft.append(word.lower())

        invalidRegex = rf"^(?!.*[{re.escape(invalidLetters)}]).*"
        guesses = [s for s in wordsLeft if re.match(invalidRegex, s)]

        # set up variables to create regex to match characters where the index is known and not
        first = ""
        second = ''
        third = ""
        fourth = ""
        fifth = ""
        i = 1
        userKnown = ""
        alpha = '[' + alpha + ']'

        for k,v in rawDict.items():
            if i == 1:
                if v == 'y':
                    first = k
                else:
                    first = alpha + ''
                    if v != "null":
                        userKnown += k
            if i == 2:
                if v == 'y':
                    second = k
                else:
                    second = alpha + ''
                    if v != 'null':
                        userKnown += k
            if i == 3:
                if v == 'y':
                    third = k
                else:
                    third = alpha + ''
                    if v != 'null':
                        userKnown += k
            if i == 4:
                if v == 'y':
                    fourth = k
                else:
                    fourth = alpha + ''
                    if v != 'null':
                        userKnown += k
            if i == 5:
                if v == 'y':
                    fifth = k
                else:
                    if v != 'null':
                        userKnown += k
            i += 1

        posRegex = rf'^{first}{second}{third}{fourth}{fifth}$'
        guessesCopy = guesses.copy()
        guesses = [s for s in guessesCopy if re.match(posRegex, s)]
        print("current guesses are: ", guesses)
        userKnownRegex = rf"^(?=.*[{re.escape(userKnown)}]).*"
        print("userKnownRegex is: ", userKnownRegex)
        guessesCopy = guesses.copy()
        guesses = [s for s in guessesCopy if re.match(userKnownRegex, s)]
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