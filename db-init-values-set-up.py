from urllib import response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Word
import requests
from bs4 import BeautifulSoup

# engine = create_engine('postgresql+psycopg2://postgres:password@localhost/wordle-helper', echo=True)

# f = open('all-words.txt', 'r')
# lst = []

# for line in f.readlines():
#     temp = line.split()
#     for each in temp:
#         lst.append(each)

# f.close()

url = 'https://wordsrated.com/tools/wordsfinder/past-wordle-answers/' 
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
wordle_items = soup.find('div', class_="wordle-solutions-container")
print(wordle_items)
# Word.Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# for each in lst:
#     new_word = Word.Word(word_val=each)
#     session.add(new_word)
#     session.commit()

# session.close()