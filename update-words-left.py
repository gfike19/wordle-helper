import requests
from bs4 import BeautifulSoup

def updateWordsLeft():
    url = "https://www.rockpapershotgun.com/wordle-past-answers"  
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    searchText = "All Wordle answers"
    headerTag = soup.find('h2', string= searchText)
    uiList = headerTag.find_next_sibling()
    listItems = uiList.find_all('li')

    f = open('words-left.txt', 'r')
    wordsLeft = f.readlines()
    f.close()

    for li in listItems:
        tempText = li.get_text(strip=True).lower() + '\n'
    if tempText in wordsLeft:
        print(tempText)
        wordsLeft.remove(tempText)

    f = open('words-left.txt', "r+", encoding='utf-8')
    f.truncate(0)
    f.writelines(wordsLeft)
    f.close()