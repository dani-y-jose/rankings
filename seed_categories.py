import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

DEFAULT_CATEGORIES = [
    "Restaurante",
    "Salteñeria",
    "Heladeria",
    "Food Truck",
    "Cafe",
    "Bar",
    "Comida Callejera",
]

rows = [{"name": name} for name in DEFAULT_CATEGORIES]
response = supabase.table("categories").insert(rows).execute()
print(f"✅ Inserted {len(response.data)} categories.")
