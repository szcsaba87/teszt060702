from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client

import requests
from bs4 import BeautifulSoup

app = FastAPI()

#origins = ["*"]

origins = [
    "https://teszt260701.onrender.com",
    "http://localhost:5173"
]

url = "https://gvdoqepfoqlwlkdrplzv.supabase.co"
key = "sb_publishable_DbqVd2S52mKdqEIziWS2-w_tNL0wM-T"  # use env vars in real code, don't hardcode

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
TIMEOUT = 300


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



@app.get("/api/scraper")
def get_scraper():
    url = 'https://www.transfermarkt.com/ferencvarosi-tc/rekordabgaenge/verein/279/saison_id/'
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return {"statusz": "success", "data" : response}