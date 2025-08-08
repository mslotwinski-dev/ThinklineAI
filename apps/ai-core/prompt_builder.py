from requesttypes import ProjectResponse, ProjectRequest
from typing import List


def _create_prompt_template(language: str, topic: str, level: str, tags: str, previous_projects: List[str] = []) -> str:
    """Creates a robust, detailed prompt to guide the AI into generating valid JSON."""

    # Start with the core request for new projects.
    core_request = (
        f"Wygeneruj 3 nowe i unikalne pomysły na projekt programistyczny w języku {language}, "
        f"którego ogólna tematyka to {topic}, o poziomie trudności: {level}, o cechach: {tags}."
    )

    # If we are regenerating, change the core request to ask for different ideas.
    if previous_projects:
        core_request = (
            f"Poprzednio wygenerowane projekty mi się nie spodobały. Oto one: {previous_projects}. "
            f"Proszę, wygeneruj 3 **zupełnie inne** pomysły, trzymając się poniższych kryteriów.\n"
            f"Język: {language}, tematyka: {topic}, poziom: {level}, cechy: {tags}."
        )

    # Combine everything into the final, highly-detailed prompt.
    return (
        f"{core_request}\n\n"
        f"Twoja odpowiedź **musi** być **wyłącznie** tablicą JSON (JSON array) zawierającą 3 obiekty.\n"
        f"**Ściśle przestrzegaj poniższych zasad formatowania JSON:**\n"
        f"1. Upewnij się, że każdy obiekt w tablicy jest oddzielony przecinkiem (`,`), z wyjątkiem ostatniego.\n"
        f"2. Wewnątrz każdego obiektu, wszystkie pary klucz-wartość muszą być oddzielone przecinkami.\n"
        f"3. Wewnątrz tablic z wartościami (takich jak `tech_stack` i `tags`), wszystkie elementy (stringi) **muszą** być oddzielone przecinkami. To bardzo ważne!\n"
        f"4. Wszystkie klucze i wartości typu string muszą być w podwójnych cudzysłowach (`\"`). Nie używaj pojedynczych cudzysłowów.\n\n"
        f"Oto dokładny przykład wymaganej struktury dla jednego obiektu:\n"
        f"```json\n"
        f"[\n"
        f"  {{\n"
        f"    \"name\": \"Przykładowa Nazwa Projektu\",\n"
        f"    \"description\": \"Dokładny i szczegółowy opis projektu, który jest interesujący i unikalny.\",\n"
        f"    \"tech_stack\": [\"Technologia 1\", \"Technologia 2\", \"Framework 3\"],\n"
        f"    \"difficulty\": \"{level}\",\n"
        f"    \"tags\": [\"tag1\", \"inny-tag\", \"tag3\"],\n"
        f"    \"estimated_time\": \"X-Y tygodni\"\n"
        f"  }}\n"
        f"]\n"
        f"```\n\n"
        f"Przed zwróceniem odpowiedzi, zweryfikuj, czy wygenerowany JSON jest w 100% poprawny składniowo.\n"
        f"Zwróć **tylko i wyłącznie** kod JSON. Nie dodawaj żadnego tekstu, wyjaśnień, ani znaczników ```json przed lub po nim."
    )


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
    """Generates the initial prompt using the new robust template."""
    tag_str = ", ".join(data.tags)
    topic = return_project_topic(data.topic)
    level = return_project_level(data.level)
    return _create_prompt_template(data.language, topic, level, tag_str)


def regenerate_prompt(data: ProjectRequest) -> str:
    """Generates a regeneration prompt using the new robust template."""
    tag_str = ", ".join(data.tags)
    topic = return_project_topic(data.topic)
    level = return_project_level(data.level)
    return _create_prompt_template(
        data.language, topic, level, tag_str, previous_projects=data.previous_projects
    )
