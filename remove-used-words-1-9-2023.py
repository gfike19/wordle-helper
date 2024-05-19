dirtyFile = open('1-9-2023-words-left.txt', 'r')
dirtyLines = dirtyFile.readlines()
dirtyFile.close()

usedFile = open('used-words.txt', 'r')
usedLines = usedFile.readlines()
usedFile.close()

for line in usedLines:
    pos = usedLines.index(line)
    line.strip()
    line.lstrip()
    # cause strings are immutable *roll eyes*
    newLine = line.lower()
    usedLines[pos] = newLine

wordsLeft = open('words-left.txt', 'a+')

for line in dirtyLines:
    line.rstrip()
    line.lstrip()
    cleanLine = line.lower()

    if cleanLine not in usedLines:
        wordsLeft.write(cleanLine)

wordsLeft.close()