from pydantic import BaseModel


class WorkPreferences(BaseModel):
    remote: bool
    minimum_monthly_salary_usd: int


class Profile(BaseModel):
    name: str
    target_roles: list[str]
    work_preferences: WorkPreferences
    programming_languages: list[str]
    backend: list[str]
    frontend: list[str]
    databases: list[str]
    devops: list[str]
    other: list[str]

class Job(BaseModel):
    title: str
    company: str
    description: str
    remote: bool
    salary_min_usd: int | None = None
    salary_max_usd: int | None = None
    required_skills: list[str]

class JobAnalysis(BaseModel):
    match_score: int
    recommendation: str
    matching_skills: list[str]
    missing_skills: list[str]
    strengths: list[str]
    concerns: list[str]
    reasoning: str

class AgentDecision(BaseModel):
    decision: str
    reason: str