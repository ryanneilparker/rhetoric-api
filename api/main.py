import uvicorn

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from models.payload import Payload
from utils.prompt import generate_prompt
from utils.gemini import gemini_text, convert_markdown_to_html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(payload: Payload, response: Response):
    """
    Generates blog content using Gemini and returns it as HTML.
    """

    prompt = generate_prompt(payload)
    generated_content = gemini_text(prompt)
    return {"generatedContent": convert_markdown_to_html(generated_content)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
