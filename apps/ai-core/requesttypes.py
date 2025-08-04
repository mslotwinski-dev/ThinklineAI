from pydantic import BaseModel
from typing import List, Dict


class ProjectResponse(BaseModel):
    name: str
    description: str
    tech_stack: List[str]
    difficulty: str
    tags: List[str]
    estimated_time: str


class ProjectRequest(BaseModel):
    language: str
    locale: str
    level: int
    topic: int
    tags: List[str]
    previous_projects: Dict[str, List[ProjectResponse]] = []  # type: ignore
