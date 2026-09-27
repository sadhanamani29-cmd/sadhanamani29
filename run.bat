@echo off
py -3.13 -m venv .venv
call .venv\Scripts\activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install --only-binary=:all: -r requirements.txt
if not exist .env copy .env.example .env
python -m uvicorn app.main:app --reload
