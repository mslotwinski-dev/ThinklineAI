from fastapi import FastAPI, HTTPException

from typing import List, Dict
import json

from openrouter import ask_openrouter
from prompt_builder import generate_prompt, regenerate_prompt
from requesttypes import ProjectRequest, ProjectResponse

app = FastAPI()


@app.post("/generate", response_model=Dict[str, List[ProjectResponse]])
async def generate_idea(data: ProjectRequest):
    prompt = generate_prompt(data)
    try:
        raw_json = await ask_openrouter(prompt)
        ideas = json.loads(raw_json)
        return {"ideas": ideas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/regenerate", response_model=Dict[str, List[ProjectResponse]])
async def regenerate_idea(data: ProjectRequest):
    prompt = regenerate_prompt(data)
    try:
        raw_json = await ask_openrouter(prompt)
        ideas = json.loads(raw_json)
        return {"ideas": ideas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
