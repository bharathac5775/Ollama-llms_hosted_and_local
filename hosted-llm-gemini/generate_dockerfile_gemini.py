from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices.
Only output the Dockerfile without explanation.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=PROMPT.format(language=language),
    )
    return response.text


if __name__ == "__main__":
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)

    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
