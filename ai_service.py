import os
import httpx

async def recommend(category: str, budget: float, preferences: str) -> str:
    enabled = os.getenv("AI_ENABLED", "false").lower() == "true"
    api_key = os.getenv("GEMINI_API_KEY", "")
    model = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    if enabled and api_key:
        prompt = (
            f"You are a budget recommendation assistant. "
            f"Category: {category}. Budget: {budget}. Preferences: {preferences}. "
            f"Give practical options within the budget and explain the selection briefly."
        )
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                r = await client.post(url, json=payload)
                r.raise_for_status()
                data = r.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            pass

    pref = preferences.strip() or "general use"
    return (
        f"Budget recommendation for {category}: budget ₹{budget:,.0f}. "
        f"Priority: {pref}. Start by comparing products within the budget, "
        f"checking essential features, warranty and total cost before purchase."
    )
