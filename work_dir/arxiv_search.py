# filename: arxiv_search.py

import requests
import feedparser

# Define the base api query url
base_url = 'http://export.arxiv.org/api/query?'

# Define the search query
search_query = 'all:comparison AND all:human learning AND all:machine learning'

# Define the start index for the results
start_index = 0

# Define the maximum number of results to retrieve
max_results = 10

# Construct the query
query = f'{base_url}search_query={search_query}&start={start_index}&max_results={max_results}'

# Perform the GET request
response = requests.get(query)

# Parse the response
feed = feedparser.parse(response.content)

# Print the title and link of each paper
for entry in feed.entries:
    print(f'Title: {entry.title}\nLink: {entry.link}\n')