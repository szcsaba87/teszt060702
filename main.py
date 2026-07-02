from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client

app = FastAPI()

#origins = ["*"]

origins = [
    "https://teszt260701.onrender.com",
    "http://localhost:5173"
]

url = "https://gvdoqepfoqlwlkdrplzv.supabase.co"
key = "sb_publishable_DbqVd2S52mKdqEIziWS2-w_tNL0wM-T"  # use env vars in real code, don't hardcode
supabase: Client = create_client(url, key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/adatok")
def get_adatok():
    # Itt van az a részed, ami lekéri a külső adatot
    # Példa egy fiktív külső API-val:
    # kulso_adat = requests.get("https://api.example.com/data").json()
    
    kulso_adat = {"uzenet": "Szia! Ez az adat a Python backendről jön!", "statusz": "sikeres"}
    return kulso_adat

@app.get("/api/sql")
def get_sql():

    response = (
        supabase.table("players")
        .select("*")
        .execute()
    )

    return {"statusz": "success", "data": response.data}