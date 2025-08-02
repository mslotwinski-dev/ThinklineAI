from requesttypes import ProjectResponse
from typing import List, Dict


def generate_prompt(language: str, level: str, tags: list[str]) -> str:
    tag_str = ", ".join(tags)
    return (
        f"Wygeneruj 3 pomysły na projekt programistyczny w języku {language}, o poziomie trudności: {level}, o cechach: {tag_str}. "
        f"Dla każdego pomysłu podaj odpowiedź w formacie JSON:\n"
        f"""\n[
  {{
    "name": "...",
    "description": "...",
    "tech_stack": ["..."],
    "difficulty": "...",
    "tags": ["..."],
    "estimated_time": "...",
  }}
]\n
Zwróć **tylko** poprawny JSON, bez komentarzy ani dodatkowego tekstu.
"""
    )


def regenerate_prompt(language: str, level: str, tags: list[str], previous_projects: Dict[str, List[ProjectResponse]]) -> str:
    tag_str = ", ".join(tags)
    return (
        f"Poprzednio wygenerowane projekty mi się nie spodobały, więc chciałbym spróbować ponownie. "
        f"Oto poprzednie projekty: {previous_projects}. "
        f"Wygeneruj 3 inne pomysły na projekt programistyczny w języku {language}, o poziomie trudności: {level}, o cechach: {tag_str}. "
        f"Dla każdego pomysłu podaj odpowiedź w formacie JSON:\n"
        f"""\n[
  {{
    "name": "...",
    "description": "...",
    "tech_stack": ["..."],
    "difficulty": "...",
    "tags": ["..."],
    "estimated_time": "...",
  }}
]\n
Zwróć **tylko** poprawny JSON, bez komentarzy ani dodatkowego tekstu.
"""
    )
