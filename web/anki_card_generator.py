# filename: anki_card_generator.py

import requests
from bs4 import BeautifulSoup

url = "https://lightning.ai/docs/pytorch/stable/model/train_model_basic.html"

# Send a HTTP request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the code blocks and the corresponding explanations
code_blocks = soup.find_all('div', class_='highlight-python')
explanations = soup.find_all('p')

# Print the code blocks and the corresponding explanations
for i in range(min(len(code_blocks), len(explanations))):
    print(f"Code:\n{code_blocks[i].text}\nExplanation:\n{explanations[i].text}\n{'-'*50}")