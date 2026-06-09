import requests
from config import SEMANTIC_API

def search_papers(keyword):
    url = f"{SEMANTIC_API}/paper/search"

    params = {
        "query": keyword,
        "limit": 25,
        "fields": "title,url,authors,year,venue,authors.affiliations"
    }

    res = requests.get(url, params=params)
    return res.json().get("data", [])
