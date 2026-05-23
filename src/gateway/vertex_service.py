import os
from typing import Optional
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting

class VertexService:
    def __init__(self, project_id: Optional[str] = None, location: str = "us-central1"):
        self.project_id = project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
        self.location = location
        vertexai.init(project=self.project_id, location=self.location)
        # Try to find a valid model alias
        model_names = ["gemini-1.5-flash-002", "gemini-1.5-flash-001", "gemini-1.5-flash"]
        for name in model_names:
            try:
                self.model = GenerativeModel(name)
                # Test the model with a tiny probe
                self.model.generate_content("ping")
                print(f"Successfully initialized model: {name}")
                break
            except Exception as e:
                print(f"Model {name} not available: {e}")
                continue
        else:
            # Fallback to the most basic if all else fails
            self.model = GenerativeModel("gemini-1.5-flash")

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
