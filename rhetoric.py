from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key

@app.post("/generate_blog")
async def generate_blog(prompt: str):
    # DEBUG
    newPrompt = prompt + " > +1 magic ai dust"
    return {"debug": newPrompt}

    # async with httpx.AsyncClient() as client:
    #     response = await client.post(
    #         "https://api.openai.com/v1/engines/davinci/completions",
    #         headers={
    #             "Authorization": f"Bearer {OPENAI_API_KEY}",
    #             "Content-Type": "application/json",
    #         },
    #         json={
    #             "prompt": prompt,
    #             "max_tokens": 500  # Adjust the token limit as needed
    #         },
    #     )
    #     if response.status_code == 200:
    #         return {"blog_content": response.json()["choices"][0]["text"]}
    #     else:
    #         raise HTTPException(status_code=response.status_code, detail="Failed to generate blog content")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
