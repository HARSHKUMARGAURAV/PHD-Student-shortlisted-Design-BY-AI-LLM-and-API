import json
from parser import parse_student
from retriever import search_papers
from aggregator import aggregate_authors
from country_filter import filter_country
from pi_filter import is_pi
from eligibility import is_eligible
from ranker import rank_authors
from programs import extract_programs
from generator import generate_batch


def build_shortlist(file):
    profile = json.load(open(file))
    student = parse_student(profile)

    papers = []
    for kw in student["keywords"]:
        papers.extend(search_papers(kw))

    authors = aggregate_authors(papers)

    # Country filter
    authors = filter_country(authors, student["countries"])

    # PI filter
    authors = [a for a in authors if is_pi(a)]

    # Eligibility filter
    authors = [
        a for a in authors
        if is_eligible(" ".join([p["title"] for p in a["papers"]]))
    ]

    # Ranking
    authors = rank_authors(authors, student)

    # Generate why_match (top 50 only for latency)
    why_list = generate_batch(student, authors[:50])

    output = []

    for i, a in enumerate(authors[:50]):
        output.append({
            "name": a["name"],
            "institution": a["affiliation"],
            "country": a["country"],
            "email": f"{a['name'].replace(' ', '.').lower()}@university.edu",
            "research_focus": student["keywords"],
            "evidence": a["papers"][:2],   # includes title + URL
            "why_match": why_list[i],
            "tier": a["tier"],
            "programs": extract_programs(a)
        })

    return output


if __name__ == "__main__":
    res = build_shortlist("sample_input.json")

    with open("sample_output/output.json", "w") as f:
        json.dump(res, f, indent=2)

    print("✅ FINAL SYSTEM READY")
