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
    prompt1 = str('Enter letter number %s\nIf unknown leave blank: ')
    prompt2 = str('Correct position? (y/n)\nIf unknown leave blank:: ')
    userKnow = {}
    alpha = string.ascii_lowercase

    for i in range(0, 5):
        key = input(prompt1 % (str(i + 1)))
        val = input(prompt2).strip().lower()
        userKnow[key] = val
    
    wordsLeft = getWordsLeft()
    indexPattern = r''
    counter = 0
    usedLetters = ''
    for k,v in userKnow.items():
        if v == 'y':
            indexPattern += '.{' + str(counter) + "}" + k
            alpha = alpha.replace(k, '')
    guesses = []
    usedLetters += input("Enter letters that aren't in the word: ").strip().lower()
    for each in usedLetters:
        alpha = alpha.replace(each, '')
    usedPattern = r'['

    for each in wordsLeft:
        match = re.match(indexPattern, each)
        if not match:
            wordsLeft.remove(each)
    
    for each in usedLetters:
        usedPattern += '^' + each
    usedPattern += ']'
    for each in wordsLeft:
        match = re.match(usedPattern, each)
        guesses.append(each)
    print(f"Matching words: {guesses}")      
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