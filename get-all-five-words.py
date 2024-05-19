def returnFirstWord(str):
    return str.split(' ', 1)[0]

f = open('oed.txt', 'r+', encoding="utf8")
fiveLetterOnly = open('only-five-letters.txt', 'a+')

for line in f.readlines():
    firstWord = returnFirstWord(line)
    firstWord.strip()

    if len(firstWord) == 5:
        fiveLetterOnly.write(firstWord + "\n")