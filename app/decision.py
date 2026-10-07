from app.models import AgentDecision, JobAnalysis


def decide(analysis: JobAnalysis) -> AgentDecision:
    if analysis.match_score >= 80:
        return AgentDecision(
            decision="APPLY",
            reason="La vacante tiene un nivel de compatibilidad alto.",
        )

    if analysis.match_score >= 60:
        return AgentDecision(
            decision="REVIEW",
            reason="La vacante tiene compatibilidad suficiente para revisarla.",
        )

    return AgentDecision(
        decision="REJECT",
        reason="La compatibilidad con el perfil es demasiado baja.",
    )