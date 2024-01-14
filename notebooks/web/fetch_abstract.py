# filename: fetch_abstract.py

import requests
from bs4 import BeautifulSoup

def fetch_abstract(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    abstract = soup.find('blockquote', attrs={'class': 'abstract mathjax'}).text.strip()
    return abstract

url = "https://arxiv.org/abs/2308.08155"
print(fetch_abstract(url))