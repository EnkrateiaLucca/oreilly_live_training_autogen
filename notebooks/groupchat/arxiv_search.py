# filename: arxiv_search.py

import arxiv
import datetime

# Search query
query = "gpt-4"

# Get the papers from the last month
papers = arxiv.query(query=query, max_results=100)

# Sort the papers by date
papers = sorted(papers, key=lambda paper: paper['published'], reverse=True)

# Get the most recent paper
recent_paper = papers[0]

# Print the details of the paper
print("Title: ", recent_paper['title'])
print("Authors: ", ", ".join(recent_paper['authors']))
print("Summary: ", recent_paper['summary'])
print("URL: ", recent_paper['arxiv_url'])