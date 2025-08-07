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
