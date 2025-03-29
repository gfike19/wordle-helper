from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Word
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/wordle-helper', echo=True)

f = open('all-words.txt', 'r')
all_words = []

for line in f.readlines():
    temp = line.split()
    for each in temp:
        all_words.append(each)

f.close()

url = "https://beebom.com/past-wordle-answers/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
table_rows = soup.find_all('tr')
tr_regex = r"^(\d+)([A-Za-z]+\s+\d{1,2},\s+\d{4})([A-Za-z]+)$"
row_list = []
used_words = []
for i in range(1, len(table_rows)):
    row = table_rows[i].text
    match = re.match(tr_regex, row)
    if match:
        number, date, word = match.groups()
        row_list.append({word : (number, date)})
        used_words.append(word)

engine = create_engine('postgresql+psycopg2://postgres:password@localhost/wordle-helper', echo=True)
Word.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

for each in all_words:
    if each in used_words:
        index = used_words.index(each)
        dit = row_list[index]
        num = dit[each][0]
        date_str = dit[each][1]
        date = datetime.strptime(date_str, '%y/%m/%d')
        new_word = Word.Word(word_val=each, wordle_num=num,date_used=date)
    else:
        new_word = Word.Word(word_val=each)
    session.add(new_word)
    session.commit()

session.close()