# filename: google_scholar_scraper.py

import requests
from bs4 import BeautifulSoup

def get_top_papers(query, num_papers=10):
    url = "https://scholar.google.com/scholar?q=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    papers = soup.select('.gs_ri')
    top_papers = []
    for paper in papers[:num_papers]:
        title = paper.select_one('.gs_rt a').text
        author = paper.select_one('.gs_a').text
        link = paper.select_one('.gs_rt a')['href']
        top_papers.append({
            'title': title,
            'author': author,
            'link': link
        })
    return top_papers

def print_papers(papers):
    for i, paper in enumerate(papers, start=1):
        print(f"{i}. {paper['title']} by {paper['author']}")
        print(f"   Link: {paper['link']}\n")

if __name__ == "__main__":
    papers = get_top_papers("prompt engineering")
    print_papers(papers)