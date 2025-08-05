from requesttypes import ProjectResponse, ProjectRequest
from typing import List, Dict


def return_project_topic(number: int) -> str:
    topics = {
        0: "Web Development",
        1: "Desktop i CLI",
        2: "Mobile",
        3: "Game Development",
        4: "AI / Machine Learning",
        5: "Data Science",
        6: "Cyberbezpieczeństwo",
        7: "Elektronika i Systemy Wbudowane",
        8: "Telekomunikacja i Teleinformatyka",
        9: "Fizyka i Symulacje Inzynierskie",
        10: "Inne",
    }
    return topics.get(number, "Unknown Topic")


def return_project_level(number: int) -> str:
    levels = {
        0: "Początkujący",
        1: "Średniozaawansowany",
        2: "Zaawansowany",
    }
    return levels.get(number, "Unknown Level")


def generate_prompt(data: ProjectRequest) -> str:
    tag_str = ", ".join(data.tags)
    return (
        f"Wygeneruj 3 pomysły na projekt programistyczny w języku {data.language}, którego ogólna tematyka to {return_project_topic(data.topic)}, o poziomie trudności: {return_project_level(data.level)}, o cechach: {tag_str}. "
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
