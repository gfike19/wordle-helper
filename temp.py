import secrets

f = open("words-left.txt", "r+")
wordsLeft = f.readlines()
f.close()

findWord = input("Enter a word: ")

print([s.lstrip().rstrip() for s in wordsLeft if findWord in s])