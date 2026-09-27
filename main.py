import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .services.ai_service import recommend

app = FastAPI(title="PocketSmart AI")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recommend", response_class=HTMLResponse)
async def get_recommendation(
    request: Request,
    category: str = Form(...),
    budget: float = Form(...),
    preferences: str = Form("")
):
    result = await recommend(category, budget, preferences)
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": result, "category": category, "budget": budget, "preferences": preferences}
    )
