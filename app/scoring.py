from app.models import Job, Profile


def get_profile_skills(profile: Profile) -> set[str]:
    skills = []

    skills.extend(profile.programming_languages)
    skills.extend(profile.backend)
    skills.extend(profile.frontend)
    skills.extend(profile.databases)
    skills.extend(profile.devops)
    skills.extend(profile.other)

    return {skill.lower() for skill in skills}


def calculate_skill_match(
    profile: Profile,
    job: Job
) -> dict:

    profile_skills = get_profile_skills(profile)

    required_skills = {
        skill.lower()
        for skill in job.required_skills
    }

    matching = profile_skills & required_skills
    missing = required_skills - profile_skills

    score = (
        len(matching) / len(required_skills) * 100
        if required_skills
        else 0
    )

    return {
        "score": round(score),
        "matching_skills": sorted(matching),
        "missing_skills": sorted(missing)
    }