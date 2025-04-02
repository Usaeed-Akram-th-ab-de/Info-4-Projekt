import openai
from fastapi import FastAPI

app = FastAPI()

# OpenAI API-Schlüssel
openai.api_key = "DEIN_OPENAI_API_KEY"

@app.get("/diagnose/{symptome}")
def diagnose(symptome: str):
    prompt = f"Ein Patient hat folgende Symptome: {symptome}. Was könnte die Diagnose sein?"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Du bist ein erfahrener Arzt."},
                  {"role": "user", "content": prompt}]
    )
    
    diagnose = response["choices"][0]["message"]["content"]
    return {"diagnose": diagnose}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
