def aggregate_authors(papers):
    author_map = {}

    for p in papers:
        for a in p["authors"]:
            aff = " ".join(a.get("affiliations", []))
            key = f"{a['name'].lower()}_{aff.lower()}"

            if key not in author_map:
                author_map[key] = {
                    "name": a["name"],
                    "affiliation": aff,
                    "papers": []
                }

            author_map[key]["papers"].append({
                "title": p["title"],
                "url": p.get("url"),
                "year": p.get("year")
            })

    return list(author_map.values())
