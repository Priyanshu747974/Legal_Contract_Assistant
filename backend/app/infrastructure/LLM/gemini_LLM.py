# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
import os
# pyrefly: ignore [missing-import]
from google import genai
from app.core.interfaces.llm_interface import LLMInterface

load_dotenv()

class GeminiLLM(LLMInterface):

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key is None:
            raise ValueError("Gemini API Key not found.")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text