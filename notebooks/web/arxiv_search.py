# filename: arxiv_search.py

import arxiv

# Search for papers on 'prompt engineering'
search = arxiv.Search(
  query = "prompt engineering",
  max_results = 5,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

# Create a client
client = arxiv.Client()

# Print the top 5 latest papers
for result in client.results(search):
  print(f"Title: {result.title}\nAuthors: {', '.join(str(author) for author in result.authors)}\nAbstract: {result.summary}\nLink: {result.pdf_url}\n")