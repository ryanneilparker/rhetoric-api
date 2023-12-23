from fastapi import FastAPI

app = FastAPI()

@app.post("/generate")
async def generate():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
