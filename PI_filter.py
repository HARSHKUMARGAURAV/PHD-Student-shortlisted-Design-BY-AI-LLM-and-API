def is_pi(author):
    papers = author["papers"]

    if len(papers) < 10:
        return False

    years = [p["year"] for p in papers if p.get("year")]

    if years:
        if max(years) - min(years) < 5:
            return False

    aff = author["affiliation"].lower()

    if "student" in aff or "phd" in aff:
        return False

    return True
