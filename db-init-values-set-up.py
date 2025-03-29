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

url = "https://beebom.com/past-wordle-answers/"
# response = requests.get(url)
html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
table_rows = soup.find_all('tr')

    # print(temp.append(tr.getText))
    # counter += 1
    # if counter == 3:
    #     temp = []
    #     counter = 0
# Word.Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# for each in lst:
#     new_word = Word.Word(word_val=each)
#     session.add(new_word)
#     session.commit()

# session.close()