from fastapi import FastAPI

app = FastAPI()

# health checker

@app.get("/health", status_code=200 )
async def root():
    return {"message": "I am healthy"}

# Basic crud operations

