from app.profile import load_profile
from app.job import load_job
from app.analyzer import analyze_job


profile = load_profile()
job = load_job()

result = analyze_job(profile, job)

print("\n=== ANÁLISIS DE LA VACANTE ===")
print(f"Puntuación: {result.match_score}/100")
print(f"Recomendación: {result.recommendation}")

print("\nHabilidades coincidentes:")
for skill in result.matching_skills:
    print(f"- {skill}")

print("\nHabilidades faltantes:")
for skill in result.missing_skills:
    print(f"- {skill}")

print("\nFortalezas:")
for strength in result.strengths:
    print(f"- {strength}")

print("\nPreocupaciones:")
for concern in result.concerns:
    print(f"- {concern}")

print("\nRazonamiento:")
print(result.reasoning)