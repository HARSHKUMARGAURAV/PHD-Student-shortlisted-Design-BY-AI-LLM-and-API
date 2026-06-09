import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_batch(student, authors):
    results = []

    for a in authors:
        papers = [p["title"] for p in a["papers"][:2]]

        prompt = f"""
        Student: {student['keywords']}
        Professor: {a['name']}
        Papers: {papers}

        Write specific why_match.
        """

        res = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        results.append(res["choices"][0]["message"]["content"])

    return results
