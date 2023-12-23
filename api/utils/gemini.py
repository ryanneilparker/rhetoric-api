import os
import markdown2
from dotenv import load_dotenv
import google.generativeai as genai

def gemini_text(prompt: str) -> str:
    """Generates text with Gemini model, returns plain text."""

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    return model.generate_content(prompt).text


def convert_markdown_to_html(markdown: str) -> str:
    """Converts Markdown to HTML using markdown2 library."""
    return markdown2.markdown(markdown)
