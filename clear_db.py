import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Delete in FK-safe order: children first, parents last
TABLES_IN_ORDER = [
    "stars",      # depends on reviews, features
    "reviews",    # depends on places, products, reviewers
    "features",   # depends on products
    "products",   # depends on categories
    "places",
    "reviewers",
    "categories",
]

print("⚠️  This will permanently delete ALL data from your Supabase database.")
confirm = input("Type 'yes' to confirm: ")
if confirm.strip().lower() != "yes":
    print("Aborted.")
    exit(0)

for table in TABLES_IN_ORDER:
    # Delete all rows by filtering on a column that always has a value (id >= 0)
    response = supabase.table(table).delete().gte("id", 0).execute()
    print(f"✅ Cleared: {table}")

print("\n🎉 All tables cleared successfully.")
