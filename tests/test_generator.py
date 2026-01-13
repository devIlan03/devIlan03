"""Tests for the AdaptaNote generator."""
from adaptanote.generator import generate_activity, format_activity


def test_generate_activity_level_range():
    activity = generate_activity("Ciclo da Água", 1)
    assert activity.topic == "Ciclo da Água"
    assert activity.level == 1
    assert len(activity.questions) == 2
    assert activity.instructions is not None


def test_generate_activity_invalid_level():
    try:
        generate_activity("Ciclo da Água", 4)
    except ValueError as exc:
        assert "level" in str(exc)
    else:
        raise AssertionError("Expected ValueError for invalid level")


def test_format_activity_includes_instructions():
    activity = generate_activity("Fotossíntese", 2, include_instructions=True)
    formatted = format_activity(activity)
    assert "Instruções para o aluno" in formatted
    assert "Fotossíntese" in formatted
