from fastapi import FastAPI
from dotenv import load_dotenv

# Load environment variables BEFORE importing routes
load_dotenv()

from routes import flowchart

app = FastAPI(title="Flowchart Generator API")

@app.get("/")
async def root():
    return {"message": "Flowchart Generator API is running"}

app.include_router(flowchart.router, prefix="/flowchart")







