from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def similarity(student, papers):
    s = model.encode(" ".join(student), convert_to_tensor=True)

    scores = []
    for p in papers:
        emb = model.encode(p["title"], convert_to_tensor=True)
        scores.append(util.cos_sim(s, emb).item())

    return max(scores) if scores else 0
