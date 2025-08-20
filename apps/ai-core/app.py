from fastapi import FastAPI, HTTPException
from typing import List, Dict
import json

from models.generate import ProjectRequest, ProjectResponse
from utility.json import extract_json_from_text
from models.project import Project
from prompts.generate import generate_prompt
from prompts.project import project_prompt
from services.openrouter import ask_openrouter


app = FastAPI()


@app.post("/generate", response_model=Dict[str, List[ProjectResponse]])
async def generate_idea(data: ProjectRequest):
    prompt = generate_prompt(data)
    try:
        raw_json = await ask_openrouter(prompt)
        print(f"Raw response from OpenRouter: {raw_json}")  # Nowe logowanie

        try:
            json_str = extract_json_from_text(raw_json)
            print(f"Extracted JSON string: {json_str}")  # Nowe logowanie
            ideas = json.loads(json_str)
        except json.JSONDecodeError as je:
            print(f"JSON decode error: {str(je)}")
            print(f"Full raw response: {raw_json}")
            raise HTTPException(
                status_code=500, detail=f"JSON decode error: {str(je)}\nRaw response: {raw_json}")
        except ValueError as ve:
            print(f"JSON extraction error: {str(ve)}")
            print(f"Full raw response: {raw_json}")
            raise HTTPException(
                status_code=500, detail=f"JSON extraction error: {str(ve)}\nRaw response: {raw_json}")

        return {"ideas": ideas}

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Unexpected error: {str(e)}")


@app.post("/project/{field}")
async def generate_field(field: str, data: Project):
    if field not in Project.model_fields.keys():
        raise HTTPException(status_code=400, detail=f"Nieznane pole: {field}")

    prompt = project_prompt(field, data.model_dump())

    try:
        raw_text = await ask_openrouter(prompt)
        try:
            parsed = json.loads(raw_text)
        except json.JSONDecodeError:
            parsed = raw_text.strip()
        return {field: parsed}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Błąd generowania pola {field}: {str(e)}"
        )
