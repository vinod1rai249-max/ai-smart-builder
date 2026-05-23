import os
from typing import Optional
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

class VertexService:
    def __init__(self, project_id: Optional[str] = None, location: str = "us-central1"):
        # Force use of Project Number for Vertex AI foundation model resolution
        self.project_id = "1051385917818"
        self.location = location
        vertexai.init(project=self.project_id, location=self.location)
        # Use the specific Gemini 2.0 Flash Lite ID
        self.model = GenerativeModel("gemini-2.0-flash-lite-preview-001")

    def get_completion(self, prompt: str) -> str:
        """
        Sends a redacted prompt to Vertex AI Gemini and returns the response.
        """
        # Safety settings to ensure clinical safety
        safety_settings = [
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            SafetySetting(
                category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
        ]

        try:
            response = self.model.generate_content(
                prompt,
                safety_settings=safety_settings
            )
            return response.text
        except Exception as e:
            print(f"Vertex AI call failed: {e}")
            return f"Error: Failed to generate response from AI model. {e}"
