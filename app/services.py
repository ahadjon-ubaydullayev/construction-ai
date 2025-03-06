import httpx
import asyncio
import json
import re


GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
GEMINI_API_KEY = "insert_api_key"


async def get_project_tasks(project_name:str):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{"text": (
                    f"Generate a JSON response listing essential construction tasks for {project_name}. Status is only 'pending' or 'completed'."
                    "Use the following format exactly:\n"
                    '    {"name": "Find land", "status": "completed"},\n'
                    '    {"name": "Get permits", "status": "pending"},\n'
                    '    {"name": "Hire architect", "status": "pending"}\n'
                    "  ]\n"
                )}]
            }],
        "generationConfig": {
            "maxOutputTokens": 600
        }
    }
    timeout=30
    async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.post(
                    GEMINI_API_URL, 
                    json=payload, 
                    headers=headers, 
                    params={"key": GEMINI_API_KEY}  
                )

    data = response.json()
    try:
        text_response = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as e:
        print(f"Error extracting response: {e}")
        return []

    json_text = re.sub(r"```json|```", "", text_response).strip()

    try:
        cleaned_tasks = json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []
    return cleaned_tasks

