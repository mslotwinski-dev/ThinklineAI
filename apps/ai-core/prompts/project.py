from typing import Dict, Any

BASE_PROMPT = """
You are a professional AI assistant specializing in generating clear and concise project documentation.
Your task is to generate text based on the provided input data and a specific task description.

Your response MUST adhere to the following rules:
- Your response MUST be in English.
- Generate only the requested text. Do not include any conversational introductions, summaries, or concluding remarks (e.g., "Here is the summary...", "I hope this helps!").
- Use clear, and objective language.
- DO NOT USE emojis and DO NOT USE formatting. Even simple formatting like bullet points or bold text are not allowed. Only exception is enter sign.
- DO NOT USE project ID in response.
"""

DETAILED_TEMPLATES = {
    "summary": "Write a concise summary for the project. Include purpose, key features, and main goal. Max 80 words.",
    "long_desc": "Generate a detailed project description including everything you should know about the project. Should be around 250 words.",
    "inspirations": "List inspirations and references that influenced the project. PROVIDE A JSON ARRAY with 1-3 names of REAL PROJECTS FROM GITHUB you can reference.",
    "target": "Describe the target audience. Max 35 words.",
    "notes": "Provide important notes, dependencies, or special instructions about the project. Max 45 words.",

    "basic_functions": "Explain the basic functions and operations of the project. Everything to know about the project's functionality. Around 120 words.",
    "extensions": "Suggest possible extensions, new features, or improvements for the project. Around 120 words.",
    "integrations": "List potential integrations with external services, APIs, or tools and explain their usefulness. Around 50 words.",
    "roadmap": "Create a roadmap including phases, milestones, priorities, and estimated timelines. Max 135 words.",
    "interface": "Describe the UI and UI theme. Max 35 words.",

    "stack": "Explain the technology stack including frontend, backend, database, libraries, etc. Around 150 words.",
    "tools": "List tools and utilities supporting the project. Around 120 words.",
    "architecture": "Describe overall architecture and folder structure of project. Around 80 words.",
    "deployment": "Explain deployment strategies, environments, and configurations. Max 40 words.",

    "usecases": """Provide 3-4 possible use cases. Use cases should be array of objects in JSON format. UseCase object should look like that:
        {
            name: string
            actor: string
            goal: string
            flow: string[] // 3-4 short steps
        }
    """,
    "patterns": "List relevant design patterns and best practices, and how each is applied. Around 60 words.",
    "testing": "Explain testing strategies, including unit, integration, and end-to-end tests. Around 40 words.",
    "scalability": "Describe how the project can scale, including performance considerations and potential bottlenecks. Around 40 words.",

    "monetization": "Suggest monetization strategies including revenue streams and pricing models. Around 250 words.",
    "market": "Provide market analysis, audience insights, competitors, and trends. Don't hesitate to criticize me if my product has poor market prospects. Around 90 words.",
    "social_impact": "Describe social impact, ethical considerations, and community benefits. Around 40 words.",

    "threats": "List potential threats, risks, and challenges. Max 220 words.",
    "monitoring": "Explain monitoring, logging, and observability strategies including key metrics. Max 60 words.",
    "data_security": "Describe data security measures including encryption, authentication, and best practices. Max 90 words.",
    "access": "Explain user access controls, roles, and permissions. Max 40 words.",

    "acquired_skills": "List skills and knowledge acquired by working on the project. Around 180 words.",
    "further_development": "Suggest how I can further develop and what future projects I can implement to grow. Around 180 words.",
}


class PromptBuilder:
    """
    A class to construct precise, well-structured prompts from templates.
    """

    def __init__(self, base_prompt: str, templates: Dict[str, str]):
        self.base_prompt = base_prompt
        self.templates = templates

    def build(self, field: str, data: Dict[str, Any]) -> str:
        task_template = self.templates.get(field)
        if not task_template:
            raise ValueError(f"No template found for field '{field}'")

        data_str = "\n".join(
            [f"- {key}: {value}" for key, value in data.items()])

        full_prompt = f"""{self.base_prompt.strip()}

------------------------------------
TASK:
{task_template.strip()}
------------------------------------
INPUT DATA:
{data_str}
------------------------------------
"""
        return full_prompt


def project_prompt(field: str, data: Dict[str, Any]) -> str:
    builder = PromptBuilder(base_prompt=BASE_PROMPT,
                            templates=DETAILED_TEMPLATES)

    return builder.build(field, data)
