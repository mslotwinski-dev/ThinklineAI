from requesttypes import ProjectResponse, ProjectRequest
from typing import List, Dict


def generate_prompt(data: ProjectRequest) -> str:
    tag_str = ", ".join(data.tags)
    return (
        f"Wygeneruj 3 pomysły na projekt programistyczny w języku {data.language}, o poziomie trudności: {data.level}, o cechach: {tag_str}. "
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


def regenerate_prompt(data: ProjectRequest) -> str:
    tag_str = ", ".join(data.tags)
    previous_projects = data.previous_projects
    return (
        f"Poprzednio wygenerowane projekty mi się nie spodobały, więc chciałbym spróbować ponownie. "
        f"Oto poprzednie projekty: {previous_projects}. "
        f"Wygeneruj 3 inne pomysły na projekt programistyczny w języku {data.language}, o poziomie trudności: {data.level}, o cechach: {tag_str}. "
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
