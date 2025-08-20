from pydantic import BaseModel
from typing import List
from typing import Optional


class Project(BaseModel):
    ID: str
    name: str
    description: str
    tech_stack: List[str]
    difficulty: str
    tags: List[str]
    estimated_time: str
    summary: Optional[str] = None
    long_desc: Optional[str] = None
    target: Optional[str] = None
    inspirations: Optional[list[str]] = None
    notes: Optional[str] = None
    basic_functions: Optional[str] = None
    extensions: Optional[str] = None
    integrations: Optional[str] = None
    roadmap: Optional[str] = None
    interface: Optional[str] = None
    stack: Optional[str] = None
    tools: Optional[str] = None
    architecture: Optional[str] = None
    deployment: Optional[str] = None
    usecases: Optional[list[dict]] = None
    patterns: Optional[str] = None
    testing: Optional[str] = None
    scalability: Optional[str] = None
    monetization: Optional[str] = None
    market: Optional[str] = None
    social_impact: Optional[str] = None
    threats: Optional[str] = None
    monitoring: Optional[str] = None
    data_security: Optional[str] = None
    access: Optional[str] = None
    acquired_skills: Optional[str] = None
    further_development: Optional[str] = None
