import json
from pathlib import Path

from app.models import Profile


PROFILE_PATH = Path("data/profile.json")


def load_profile() -> Profile:
    with PROFILE_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Profile.model_validate(data)