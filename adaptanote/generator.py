"""Utility functions to generate adapted educational activities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Question:
    """Represents an activity question."""

    prompt: str
    options: List[str]
    answer: str
    visuals: Dict[str, str]


@dataclass
class Instructions:
    """Holds optional instructions for student and educator."""

    student: str
    educator: str


@dataclass
class Activity:
    """Full activity payload."""

    topic: str
    level: int
    summary: str
    questions: List[Question]
    instructions: Instructions | None


def _base_summary(topic: str) -> str:
    return (
        f"O tema é {topic}. Vamos aprender as ideias principais de forma simples e prática."
    )


def _level_templates(level: int) -> Dict[str, str]:
    if level == 1:
        return {
            "summary": (
                "Explicação curta com palavras do dia a dia e foco em uma ideia principal."
            ),
            "question_type": "múltipla escolha",
            "student_instruction": "Leia e marque a resposta correta.",
            "educator_instruction": (
                "Incentive o aluno a ler em voz alta e oferecer apoio apenas quando necessário."
            ),
        }
    if level == 2:
        return {
            "summary": "Texto mínimo com apoio visual para cada conceito importante.",
            "question_type": "associação",
            "student_instruction": "Observe as figuras e una com uma linha a resposta.",
            "educator_instruction": (
                "Aponte para as imagens enquanto lê a pergunta, garantindo compreensão passo a passo."
            ),
        }
    return {
        "summary": "Linguagem objetiva usando poucas palavras e imagens claras.",
        "question_type": "sim/não",
        "student_instruction": "Aponte a imagem certa ou responda com sim ou não.",
        "educator_instruction": (
            "Mostre cada imagem, espere a indicação do aluno e confirme a resposta com gestos ou palavras simples."
        ),
    }


def _generate_questions(topic: str, level: int) -> List[Question]:
    visuals = {
        "Sol": "imagem de um sol amarelo",
        "Chuva": "imagem de nuvem com gotas",
        "Planta": "ilustração de planta verde",
        "Água": "ícone de gota d'água",
    }

    if level == 1:
        return [
            Question(
                prompt=f"Qual opção está ligada ao tema {topic}?",
                options=["Sol", "Chuva", "Planta"],
                answer="Planta",
                visuals={option: visuals.get(option, "") for option in ["Sol", "Chuva", "Planta"]},
            ),
            Question(
                prompt="Qual palavra mostra algo que o tema usa?",
                options=["Água", "Bola", "Gato"],
                answer="Água",
                visuals={"Água": visuals.get("Água", "")},
            ),
        ]

    if level == 2:
        return [
            Question(
                prompt=f"Ligue a palavra ao desenho sobre {topic}.",
                options=["Planta", "Sol", "Água"],
                answer="Planta",
                visuals={option: visuals.get(option, "") for option in ["Planta", "Sol", "Água"]},
            ),
            Question(
                prompt="Circule a imagem que ajuda o tema.",
                options=["Sol", "Chuva"],
                answer="Sol",
                visuals={option: visuals.get(option, "") for option in ["Sol", "Chuva"]},
            ),
        ]

    return [
        Question(
            prompt=f"{topic}. Sol?",
            options=["Sim", "Não"],
            answer="Sim",
            visuals={"Sim": visuals.get("Sol", "imagem de um sol"), "Não": "X vermelho"},
        ),
        Question(
            prompt=f"{topic}. Água?",
            options=["Sim", "Não"],
            answer="Sim",
            visuals={"Sim": visuals.get("Água", "ícone de água"), "Não": "X vermelho"},
        ),
    ]


def generate_activity(topic: str, level: int, include_instructions: bool = True) -> Activity:
    """Generate an adapted activity for the given topic and level."""
    if not topic or not topic.strip():
        raise ValueError("topic must not be empty")

    if level not in {1, 2, 3}:
        raise ValueError("level must be 1, 2, or 3")

    templates = _level_templates(level)

    instructions = None
    if include_instructions:
        instructions = Instructions(
            student=templates["student_instruction"],
            educator=templates["educator_instruction"],
        )

    summary = f"{_base_summary(topic)} {templates['summary']}"

    return Activity(
        topic=topic,
        level=level,
        summary=summary,
        questions=_generate_questions(topic, level),
        instructions=instructions,
    )


def format_activity(activity: Activity) -> str:
    """Create a human-readable representation of an activity."""
    lines: List[str] = []
    lines.append(f"Tema: {activity.topic}")
    lines.append(f"Nível: {activity.level}")
    lines.append("")
    lines.append("Resumo:")
    lines.append(activity.summary)
    lines.append("")

    for index, question in enumerate(activity.questions, start=1):
        lines.append(f"Pergunta {index}: {question.prompt}")
        for option in question.options:
            visual = question.visuals.get(option, "")
            visual_text = f" (visual: {visual})" if visual else ""
            lines.append(f"  - {option}{visual_text}")
        lines.append(f"Resposta sugerida: {question.answer}")
        lines.append("")

    if activity.instructions:
        lines.append("Instruções para o aluno:")
        lines.append(activity.instructions.student)
        lines.append("")
        lines.append("Instruções para o aplicador/professor:")
        lines.append(activity.instructions.educator)

    return "\n".join(lines)
