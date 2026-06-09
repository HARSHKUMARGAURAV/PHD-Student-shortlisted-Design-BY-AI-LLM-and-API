OPENAI_API_KEY = "your-key"

SEMANTIC_API = "https://api.semanticscholar.org/graph/v1"

# University → Country mapping (extendable)
UNIV_COUNTRY = {
    "stanford": "usa",
    "mit": "usa",
    "harvard": "usa",
    "oxford": "uk",
    "cambridge": "uk",
    "toronto": "canada"
}

ELIGIBILITY_PATTERNS = [
    r"uk only",
    r"eu only",
    r"home fees",
    r"residents only",
    r"citizenship required"
]
