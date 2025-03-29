from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import Word
import requests
from bs4 import BeautifulSoup
import re
import secrets
# engine = create_engine('postgresql+psycopg2://postgres:password@localhost/wordle-helper', echo=True)

# f = open('all-words.txt', 'r')
# lst = []

# for line in f.readlines():
#     temp = line.split()
#     for each in temp:
#         lst.append(each)

# f.close()

url = "https://beebom.com/past-wordle-answers/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
table_rows = soup.find_all('tr')
tr_regex = r"^(\d+)([A-Za-z]+\s+\d{1,2},\s+\d{4})([A-Za-z]+)$"
row_list = []
for i in range(1, len(table_rows)):
    row = table_rows[i].text
    match = re.match(tr_regex, row)
    if match:
        number, date, word = match.groups()
        row_list.append({word : (number, date)})

for i in range(0,5):
    print(secrets.choice(row_list))
# Word.Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# for each in lst:
#     new_word = Word.Word(word_val=each)
#     session.add(new_word)
#     session.commit()

# session.close()