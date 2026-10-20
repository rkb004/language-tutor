
import os
import requests
from typing import List, Dict


class TeluguTutor:
    def __init__(self):
        self.model = os.getenv(
            "OLLAMA_MODEL", "llama3.1:8b"
        )
        self.base_url = os.getenv(
            "OLLAMA_URL",
            "http://localhost:11434"
        )

    def build_system_prompt(
        self,
        difficulty: str = "beginner"
    ) -> str:
        return f"""
You are a friendly, patient Telugu language tutor.

Your goal is to help English-speaking learners
become conversational in Telugu.

IMPORTANT RULES:
1. Write Telugu using English letters only.
2. Never use Telugu script.
3. Explain grammar concepts in simple English.
4. Correct mistakes politely.
5. Give practical, everyday examples.
6. Encourage the student to respond in Telugu.
7. Keep responses conversational and concise.

Current student level: {difficulty}

Difficulty guidelines:
- Beginner: Short sentences, basic vocabulary.
- Intermediate: Longer dialogues and grammar.
- Advanced: Natural conversation and idioms.

Response format:
1. Telugu response (Romanized)
2. English translation when useful
3. Brief correction or learning tip
4. One follow-up question

Example:

Student: How do I say "How are you?"

Tutor:
Telugu: Nuvvu ela unnava?
English: How are you?

Tip: "Nuvvu" is informal. Use "Meeru"
when speaking respectfully.

Try saying: "I am doing well."
"""

    def generate_response(
        self,
        message: str,
        history: List[Dict],
        difficulty: str = "beginner"
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": self.build_system_prompt(
                    difficulty
                )
            }
        ]

        for item in history[-12:]:
            messages.append({
                "role": item["role"],
                "content": item["content"]
            })

        messages.append({
            "role": "user",
            "content": message
        })

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "num_predict": 400
            }
        }

        response = requests.post(
            f"{self.base_url}/api/chat",
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["message"]["content"].strip()

