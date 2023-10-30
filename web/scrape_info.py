# filename: scrape_info.py

import requests
from bs4 import BeautifulSoup

URL = "https://www.smoothcomp.com/en/event/..."  # replace with actual URL

def scrape_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print all the text on the page
    print(soup.get_text())

scrape_info(URL)