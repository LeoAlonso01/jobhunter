import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from app.models import Job, JobAnalysis, Profile


load_dotenv()


def analyze_job(profile: Profile, job: Job) -> JobAnalysis:
    token = os.getenv("HF_TOKEN")

    if not token:
        raise RuntimeError("HF_TOKEN no encontrado")

    client = InferenceClient(
        api_key=token,
        provider="auto",
    )

    prompt = f"""
Analiza esta oferta de trabajo en relación con el perfil del candidato.

PERFIL DEL CANDIDATO:
{profile.model_dump_json(indent=2)}

OFERTA DE TRABAJO:
{job.model_dump_json(indent=2)}

Evalúa:

1. Qué tan adecuado es el puesto para el candidato.
2. Qué habilidades coinciden.
3. Qué habilidades faltan.
4. Las principales fortalezas del candidato para este puesto.
5. Las principales preocupaciones o desventajas.
6. Una recomendación final.

Responde únicamente con un objeto JSON válido con esta estructura:

{{
    "match_score": 0,
    "recommendation": "",
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "concerns": [],
    "reasoning": ""
}}

El campo match_score debe ser un número entero entre 0 y 100.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response.choices[0].message.content

    if not content:
        raise RuntimeError("El modelo no devolvió contenido")

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:]

    if content.endswith("```"):
        content = content[:-3]

    content = content.strip()

    return JobAnalysis.model_validate_json(content)