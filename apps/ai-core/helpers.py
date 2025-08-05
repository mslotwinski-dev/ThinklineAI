import re


def extract_json_from_text(text: str) -> str:
    match = re.search(r'\[\s*{.*?}\s*\]', text, re.DOTALL)
    if match:
        return match.group(0)
    else:
        raise ValueError("No valid JSON array found in the response.")
