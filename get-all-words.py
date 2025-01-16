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