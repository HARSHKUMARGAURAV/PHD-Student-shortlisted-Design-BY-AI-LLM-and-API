import re
from config import ELIGIBILITY_PATTERNS

def is_eligible(text):
    text = text.lower()

    for pattern in ELIGIBILITY_PATTERNS:
        if re.search(pattern, text):
            return False

    return True
