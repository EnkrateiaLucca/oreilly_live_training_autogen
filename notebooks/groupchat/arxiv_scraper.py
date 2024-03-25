# filename: arxiv_scraper.py

import requests
from bs4 import BeautifulSoup
import time

def search_arxiv(query, max_results=10):
    base_url = "http://export.arxiv.org/api/query?"
    query = "all:" + query
    start = 0
    total_results = 1  # this is just to initialize the while loop
    papers = []

    while len(papers) < total_results and len(papers) < max_results:
        response = requests.get(base_url,
                                params={
                                    "search_query": query,
                                    "start": start,
                                    "max_results": max_results
                                })
        feed = BeautifulSoup(response.content, "html.parser")
        total_results_element = feed.feed.find('opensearch:totalresults')
        total_results = int(total_results_element.string) if total_results_element else 0
        entries = feed.find_all("entry")

        for entry in entries:
            paper = {
                "title": entry.title.string,
                "summary": entry.summary.string,
                "published": entry.published.string,
                "link": entry.id.string
            }
            papers.append(paper)

        start += len(entries)
        time.sleep(3)  # to avoid hitting the API rate limit

    return papers

papers = search_arxiv("GPT-4")
for paper in papers:
    print(f"Title: {paper['title']}")
    print(f"Summary: {paper['summary']}")
    print(f"Published: {paper['published']}")
    print(f"Link: {paper['link']}")
    print("\n")