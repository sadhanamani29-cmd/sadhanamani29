# PocketSmart AI

FastAPI + Jinja2 budget recommendation assistant.

## Python
Use Python 3.13 (64-bit).

## Windows
Run `run.bat`, then open http://127.0.0.1:8000

## Manual
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install --only-binary=:all: -r requirements.txt
copy .env.example .env
python -m uvicorn app.main:app --reload

## Gemini
Edit `.env` and set GEMINI_API_KEY and AI_ENABLED=true.
If Gemini is not configured, local fallback mode is used.
