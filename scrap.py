# get all
import requests
from bs4 import BeautifulSoup

url = "https://www.bestwordlist.com/5letterwords.htm"
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful
soup = BeautifulSoup(response.text, 'html.parser')

# Find all spans with class "mt"
mt_spans = soup.find_all("span", class_="mt")

# Collect text unless it is also inside a span with class "rd"
result_texts = []
for mt_span in mt_spans:
    if not mt_span.find_parent("span", class_="rd"):  # Exclude if within "rd"
        result_texts.append(mt_span.get_text())

url = "https://www.bestwordlist.com/5letterwordspage{}.htm"
for i in range(2, 27):
    response = requests.get(url.format(i))
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    mt_spans = soup.find_all("span", class_="mt")
    for mt_span in mt_spans:
        if not mt_span.find_parent("span", class_="rd"):
            result_texts.append(mt_span.get_text())

f = open("all-words.txt", "w+")
for each in result_texts:
    f.write(each)
f.close()

# get latest from rock paper shot gun
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