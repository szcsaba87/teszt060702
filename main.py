from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# --- CORS BEÁLLÍTÁS ---
# Ide írd be a Render-en futó React oldalad pontos URL-jét!
# Teszteléshez a ["*"] is működik (mindenkit engedélyez), de élesben jobb a pontos URL.

origins = [
    "https://teszt260701.onrender.com",
    "http://localhost:5173"
]

#origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Minden HTTP metódust engedélyez (GET, POST, stb.)
    allow_headers=["*"], # Minden fejlécet engedélyez
)

@app.get("/api/adatok")
def get_adatok():
    # Itt van az a részed, ami lekéri a külső adatot
    # Példa egy fiktív külső API-val:
    # kulso_adat = requests.get("https://api.example.com/data").json()
    
    kulso_adat = {"uzenet": "Szia! Ez az adat a Python backendről jön!", "statusz": "sikeres"}
    return kulso_adat