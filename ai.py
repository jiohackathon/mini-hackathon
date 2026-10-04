from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


def get_ai_response(question):
    response = client.models.generate_content(
       model="Antigravity",
        contents=question
    )

    return response.text