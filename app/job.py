import json
from pathlib import Path

from app.models import Job


JOB_PATH = Path("data/job_example.json")


def load_job() -> Job:
    with JOB_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return Job.model_validate(data)