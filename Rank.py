from embeddings import similarity

def rank_authors(authors, student):
    scored = []

    for a in authors:
        sim = similarity(student["keywords"], a["papers"])
        score = sim + len(a["papers"]) * 0.02

        if score > 0.8:
            tier = "reach"
        elif score > 0.6:
            tier = "target"
        else:
            tier = "safety"

        a["score"] = score
        a["tier"] = tier

        scored.append(a)

    return sorted(scored, key=lambda x: x["score"], reverse=True)
