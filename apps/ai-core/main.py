from helpers import extract_json_from_text
from requesttypes import ProjectRequest, ProjectResponse
from prompt_builder import generate_prompt, regenerate_prompt
from openrouter import ask_openrouter
from fastapi import FastAPI, HTTPException

from typing import List, Dict
import json


app = FastAPI()


@app.post("/generate", response_model=Dict[str, List[ProjectResponse]])
async def generate_idea(data: ProjectRequest):
    prompt = generate_prompt(data)
    try:
        raw_json = await ask_openrouter(prompt)
        print(f"Raw response: {raw_json}")

        try:
            json_str = extract_json_from_text(raw_json)
            ideas = json.loads(json_str)
        except json.JSONDecodeError as je:
            raise HTTPException(
                status_code=500, detail=f"JSON decode error: {str(je)}\nRaw response: {raw_json}")
        except ValueError as ve:
            raise HTTPException(
                status_code=500, detail=f"JSON extraction error: {str(ve)}\nRaw response: {raw_json}")

        return {"ideas": ideas}

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}")


@app.post("/regenerate", response_model=Dict[str, List[ProjectResponse]])
async def regenerate_idea(data: ProjectRequest):
    prompt = regenerate_prompt(data)
    try:
        raw_json = await ask_openrouter(prompt)
        ideas = json.loads(raw_json)
        return {"ideas": ideas}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
