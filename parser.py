def parse_student(profile):
    """
    Parse student JSON into structured format
    """

    # Extract research interests
    keywords = profile.get("research_interests", [])

    # Normalize countries (lowercase for matching)
    countries = [c.lower() for c in profile.get("target_countries", [])]

    # Combine all text for future use (optional)
    text_parts = []

    if "education" in profile:
        text_parts.append(str(profile["education"]))

    if "projects" in profile:
        text_parts.append(str(profile["projects"]))

    if "publications" in profile:
        text_parts.append(str(profile["publications"]))

    if "intro_call_summary" in profile:
        text_parts.append(profile["intro_call_summary"])

    if "raw_resume_text" in profile:
        text_parts.append(profile["raw_resume_text"])

    full_text = " ".join(text_parts)

    return {
        "keywords": keywords,
        "countries": countries,
        "full_text": full_text
    }
