from typing import Dict, Any

BASE_PROMPT = """
You are a professional AI assistant specializing in generating clear and concise project documentation.
Your task is to generate text based on the provided input data and a specific task description.

Your response MUST adhere to the following rules:
- Your response MUST be in English.
- Generate only the requested text. Do not include any conversational introductions, summaries, or concluding remarks (e.g., "Here is the summary...", "I hope this helps!").
- Use clear, professional, and objective language.
- DO NOT USE emojis. Use simple formatting like bullet points or bold text only when it enhances readability and structure.
"""

DETAILED_TEMPLATES = {
    "summary": """
    Write a concise project summary (max 100 words).
    Structure the response as follows:
    1.  **Project Mission:** A single sentence explaining the core purpose.
    2.  **Key Features:** A bulleted list of the 3-5 main features.
    3.  **Core Value:** A concluding sentence on the primary problem it solves for users.
    """,
    "long_desc": """
    Generate a comprehensive project description.
    Divide the response into the following sections using bold headers:
    - **Introduction:** A brief overview of the project and its purpose.
    - **Scope & Features:** A detailed, bulleted list of all major functionalities.
    - **Technology Stack Overview:** A high-level summary of the technologies used.
    - **Target Audience:** A description of the ideal users.
    - **Expected Outcomes:** The primary goals and measurable results of the project.
    """,
    "inspirations": """
    List the inspirations and key references that influenced this project.
    For each item, provide a brief explanation of its relevance and impact.
    Format as a bulleted list:
    - **[Inspiration Name/Source]:** [Brief explanation of its influence].
    """,
    "target": """
    Create a detailed description of the target audience.
    Include these sections with bold headers:
    - **Primary Audience:** Describe the main user group, their needs, and technical proficiency.
    - **User Personas:** Provide 1-2 brief examples of typical users, including their goals and pain points.
    - **Project Goals for Users:** List the key objectives the project helps users achieve.
    """,
    "notes": """
    Provide a list of important notes, dependencies, or special instructions for the project.
    Categorize them if possible (e.g., Technical Notes, Setup Instructions, API Keys).
    """,
    "basic_functions": """
    Explain the basic functions and core operations of the project in a step-by-step manner.
    Focus on the main user workflow from start to finish. Use a numbered list.
    """,
    "extensions": """
    Suggest three potential extensions, new features, or improvements for the project.
    For each suggestion, provide a brief rationale explaining the value it would add.
    Format as a bulleted list:
    - **[Feature Name]:** [Rationale].
    """,
    "integrations": """
    List potential integrations with external services, APIs, or tools.
    For each integration, explain its purpose and benefits in the context of this project.
    - **[Service/API Name]:** [Purpose and benefit].
    """,
    "roadmap": """
    Create a high-level project roadmap.
    Structure it by phases, including the objective, key deliverables, and an estimated timeline for each.
    Example Format:
    - **Phase 1: MVP (Months 1-3)**
        - **Objective:** Launch a core, functional product.
        - **Key Deliverables:** [List 3-4 key features].
    - **Phase 2: Feature Expansion (Months 4-9)**
        - **Objective:** Enhance user experience and add secondary features.
        - **Key Deliverables:** [List 3-4 key features].
    """,
    "interface": """
    Describe the User Interface (UI) and User Experience (UX) design.
    Cover the following points:
    - **Layout & Navigation:** How is the interface structured?
    - **Design Philosophy:** What are the core principles (e.g., minimalist, data-driven, mobile-first)?
    - **Key UI Components:** Mention any unique or critical interface elements.
    """,
    "stack": """
    Detail the project's technology stack.
    For each category below, list the technologies and provide a brief (1-sentence) rationale for its selection:
    - **Frontend:**
    - **Backend:**
    - **Database:**
    - **DevOps/Infrastructure:**
    - **Key Libraries/Frameworks:**
    """,
    "tools": """
    List the development tools, utilities, and platforms that support the project.
    Group them by category:
    - **Version Control:**
    - **Project Management:**
    - **CI/CD:**
    - **Communication:**
    """,
    "architecture": """
    Describe the system's software architecture.
    Your response should cover:
    1.  **Architectural Pattern:** Name the primary pattern used (e.g., Monolithic, Microservices, MVC, Serverless).
    2.  **Core Components:** List the main modules/services and their responsibilities.
    3.  **Data Flow:** Briefly explain how data moves through the system for a key use case.
    """,
    "deployment": """
    Explain the project's deployment strategy.
    Address the following points:
    - **Environments:** (e.g., Development, Staging, Production).
    - **Deployment Process:** How is new code deployed (e.g., CI/CD pipeline, manual deployment)?
    - **Hosting Platform:** Where is the application hosted (e.g., AWS, Vercel, on-premise)?
    """,
    "usecases": """
    Provide a list of key use cases and user scenarios.
    For each use case, define the actor, the action, and the expected outcome.
    Format:
    - **Use Case:** [Brief name, e.g., User Registration].
        - **Actor:** [e.g., New User].
        - **Action:** [e.g., Fills out the registration form and submits it].
        - **Outcome:** [e.g., A user account is created and a confirmation email is sent].
    """,
    "patterns": """
    List relevant design patterns and best practices applied in the project.
    For each pattern, briefly explain where and why it was used.
    Example:
    - **Singleton Pattern:** Used for managing the database connection pool to ensure only one instance exists.
    """,
    "testing": """
    Explain the project's testing strategy.
    Describe the purpose of each type of test within this project:
    - **Unit Tests:**
    - **Integration Tests:**
    - **End-to-End (E2E) Tests:**
    - **Key Testing Libraries/Tools:**
    """,
    "scalability": """
    Describe how the project is designed to scale.
    Include the following aspects:
    - **Scalability Strategy:** (e.g., Horizontal scaling of servers, database read replicas).
    - **Potential Bottlenecks:** Identify 1-2 areas that might become performance issues under heavy load.
    - **Performance Metrics:** List key metrics used to monitor performance.
    """,
    "monetization": """
    Suggest potential monetization strategies for the project.
    Provide at least two distinct models and briefly describe them.
    - **Model 1:** [e.g., Subscription-based (SaaS) with tiered pricing].
    - **Model 2:** [e.g., Freemium with optional paid features].
    """,
    "market": """
    Provide a brief market analysis.
    Structure the response with these headers:
    - **Target Market:** A summary of the market size and segment.
    - **Key Competitors:** List 2-3 main competitors and their key weakness.
    - **Competitive Advantage:** What makes this project unique or better?
    """,
    "social_impact": """
    Describe the project's potential social impact and any ethical considerations.
    - **Positive Impact:** How can the project benefit the community or society?
    - **Ethical Considerations:** Are there any data privacy, bias, or other ethical issues to consider?
    """,
    "threats": """
    Identify potential threats and risks for the project.
    List 2-3 examples for each category:
    - **Technical Risks:** (e.g., security vulnerabilities, data loss).
    - **Business Risks:** (e.g., low user adoption, market competition).
    - **Operational Risks:** (e.g., loss of key personnel, budget overruns).
    """,
    "monitoring": """
    Explain the monitoring, logging, and observability strategy.
    - **Key Metrics to Monitor:** (e.g., API response time, error rate, CPU utilization).
    - **Logging Strategy:** What information will be logged?
    - **Tools:** What tools will be used (e.g., Prometheus, Grafana, Sentry)?
    """,
    "data_security": """
    Describe the data security measures implemented in the project.
    Cover these areas:
    - **Data Encryption:** (e.g., at rest and in transit).
    - **Authentication & Authorization:** How are users authenticated?
    - **Best Practices:** Mention any specific security practices followed (e.g., OWASP Top 10).
    """,
    "access": """
    Explain the user access control model.
    - **User Roles:** List the different user roles (e.g., Admin, Editor, Viewer).
    - **Permissions:** Describe what actions each role is permitted to perform.
    """,
    "acquired_skills": """
    List the key skills and knowledge that can be acquired by working on this project.
    Group them into categories:
    - **Technical Skills:** (e.g., specific languages, frameworks, cloud services).
    - **Soft Skills:** (e.g., project management, teamwork, problem-solving).
    """,
    "further_development": """
    Suggest directions for the project's future development.
    Provide a list of 3-5 high-level ideas for future versions or related projects that could build upon this one.
    """,
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
