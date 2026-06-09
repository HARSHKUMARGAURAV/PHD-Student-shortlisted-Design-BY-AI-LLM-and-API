def parse_student(profile):
    return {
        "keywords": profile.get("research_interests", []),
        "countries": [c.lower() for c in profile.get("target_countries", [])],
        "full_text": profile.get("raw_resume_text", "")
    }
