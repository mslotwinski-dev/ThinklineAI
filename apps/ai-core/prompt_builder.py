from requesttypes import ProjectRequest
from typing import List


def _create_prompt_template(language: str, topic: str, level: str, tags: str, previous_projects: List[str] = []) -> str:
    """Creates a robust, detailed prompt to guide the AI into generating valid JSON."""

    core_request = (
        f"Generate 3 new and unique project ideas in {language}, "
        f"with the general topic of {topic}, difficulty level: {level}, and features: {tags}."
    )

    if previous_projects:
        core_request = (
            f"I didn’t like the previously generated projects. Here they are: {previous_projects}. "
            f"Please generate 3 **completely different** ideas, while sticking to the following criteria.\n"
            f"Language: {language}, topic: {topic}, level: {level}, features: {tags}."
        )

    return (
        f"{core_request}\n\n"
        f"Your response **must** be **only** a JSON array containing 3 objects.\n"
        f"**Strictly follow the JSON formatting rules below:**\n"
        f"1. Make sure each object in the array is separated by a comma (`,`), except the last one.\n"
        f"2. Inside each object, all key-value pairs must be separated by commas.\n"
        f"3. Inside arrays (such as `tech_stack` and `tags`), all elements (strings) **must** be separated by commas. This is very important!\n"
        f"4. All keys and string values must be in double quotes (`\"`). Do not use single quotes.\n\n"
        f"Here is the exact example of the required structure for one object:\n"
        f"```json\n"
        f"[\n"
        f"  {{\n"
        f"    \"name\": \"Sample Project Name\",\n"
        f"    \"description\": \"A detailed and comprehensive project description that is interesting and unique.\",\n"
        f"    \"tech_stack\": [\"Technology 1\", \"Technology 2\", \"Framework 3\"],\n"
        f"    \"difficulty\": \"{level}\",\n"
        f"    \"tags\": [\"tag1\", \"another-tag\", \"tag3\"],\n"
        f"    \"estimated_time\": \"X-Y days / weeks\"\n"
        f"  }}\n"
        f"]\n"
        f"\n\n"
        f"Before returning your response, verify that the generated JSON is 100% syntactically correct.\n"
        f"Return **only and exclusively** the JSON code. Do not add any text, explanations, or ```json markers before or after it."
    )


def return_project_topic(number: int) -> str:
    topics = {
        0: "Web Development",
        1: "Desktop and CLI",
        2: "Mobile Development",
        3: "Game Development",
        4: "AI / Machine Learning",
        5: "Data Science",
        6: "Cybersecurity",
        7: "Electronics and Embedded Systems",
        8: "Telecommunications",
        9: "Physics and Engineering Simulations",
        10: "Other",
    }
    return topics.get(number, "Unknown Topic")


def return_project_level(number: int) -> str:
    levels = {
        0: "Beginner",
        1: "Intermediate",
        2: "Advanced",
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
