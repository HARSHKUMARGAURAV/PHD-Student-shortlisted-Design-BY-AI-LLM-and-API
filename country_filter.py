from config import UNIV_COUNTRY

def detect_country(affiliation):
    aff = affiliation.lower()

    for uni, country in UNIV_COUNTRY.items():
        if uni in aff:
            return country

    return None


def filter_country(authors, target_countries):
    result = []

    for a in authors:
        country = detect_country(a["affiliation"])

        if country and country in target_countries:
            a["country"] = country
            result.append(a)

    return result
