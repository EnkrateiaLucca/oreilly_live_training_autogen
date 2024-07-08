# filename: latest_arxiv_llm.py

import requests
import feedparser
from datetime import date

def fetch_latest_arxiv_paper(query, max_results=1):
    base_url = "http://export.arxiv.org/api/query?"
    query_url = f"search_query={query}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    response = requests.get(base_url + query_url)
    
    if response.status_code == 200:
        feed = feedparser.parse(response.content)
        if feed.entries:
            return feed.entries[0]
    return None

if __name__ == "__main__":
    query = "open source LLM"
    latest_paper = fetch_latest_arxiv_paper(query)
    
    if latest_paper:
        print("Title:", latest_paper.title)
        print("Authors:", ", ".join(author.name for author in latest_paper.authors))
        print("Published Date:", latest_paper.published)
        print("Summary:", latest_paper.summary)
        print("Link:", latest_paper.link)
    else:
        print("No results found.")