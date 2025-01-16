from WordleHelper import getWordsLeft
from WordleHelper import Guesses
import secrets
import string

while True:
    f = open('words-left.txt', 'r')
    wordsLeft = f.readlines()
    f.close()
    testWord = secrets.choice(wordsLeft)
    f = open('test-word.txt', 'w')
    f.write(testWord)
    f.close()
    userWord = secrets.choice(wordsLeft)
    print('User word is: ',userWord)
    posInfo = {}
    alpha = string.ascii_lowercase
    for each in testWord:
        alpha.replace(each, '')
    usedLetters = ''
    i = 0
    for each in userWord:
        if each in testWord:
            if userWord[i] == testWord[i]:
                print(i, ') Letter IS in correct spot')
                posInfo[i] = 'y'
            else:
                print(i, ') Letter is NOT in correct spot')
                posInfo[i] = 'n'
        else:
            print(i, ') Letter is not present at all')
            posInfo[i] = 'n'
            usedLetters += userWord[i]
        i += 1
        print('Leter %s was removed' + each)
        alpha.replace(each, '')

    alphaLenLeft = len(alpha)
    print(posInfo)
    rNum = secrets.randbelow(alphaLenLeft)
    for i in range(rNum):
        letter = secrets.choice(alpha)
        if letter not in userWord:
            usedLetters += letter
        else:
            letter = secrets.choice(alpha)
    print("Used letters are: ", usedLetters)
    Guesses()
    repeat = input("Repeat? (y/n): ")
    if repeat == 'n':
        exit()