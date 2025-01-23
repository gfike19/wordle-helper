import secrets
import string
import re

while True:
    # Get all words
    f = open('all-words.txt', 'r')
    lines = f.readlines()
    f.close()
    allWords = []
    for line in lines:
        words = line.split()
        allWords.extend(words)
    # Get test word
    testWord = secrets.choice(allWords)
    print('test word is: ', testWord)
    allWords.remove(testWord)
    # f = open('test-word.txt', 'w+')
    # f.write(testWord)
    # f.close()
    # Get word to guess with
    guessWord = secrets.choice(allWords)
    allWords.remove(guessWord)
    print('Guess word is ', guessWord)
    # create dictionary with letter and if it's in the right spot
    posDict = {}
    # create string of used characters
    alpha = string.ascii_uppercase
    usedLetters = ''
    i = 0
    for char in guessWord:
        if char in testWord:
            if guessWord[i] == testWord[i]:
                posDict[char] = 'y'
            else:
                posDict[char] = 'n'
        else:
            alpha = alpha.replace(char, '')
            if 'null' in posDict.keys():
                posDict['null' + str(i)] = 'null'
            else:
                posDict['null'] = 'null'
        i += 1
    print('Position dictionary is ', posDict)
    print('Characters not present ', usedLetters)
    # regex set up
    stringSet = ''
    alpha = ('[' + alpha + ']')
    for k,v in posDict.items():
        if v == 'y':
            stringSet += k
        else:
            stringSet += alpha
    wordPattern = r''.join(stringSet)
    print('Regex is: ', wordPattern)
    guesses = []
    for word in allWords:
        wordMatch = re.match(wordPattern, word)
        if wordMatch:
            guesses.append(word)
    print(guesses)
    repeat = input('Again? (y/n): ')
    if repeat == 'n':
        break