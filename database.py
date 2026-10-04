from dotenv import load_dotenv
import os
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


def save_data(name, question, answer):
    data = {
        "name": name,
        "question": question,
        "answer": answer
    }

    supabase.table("questions").insert(data).execute()

    return "Saved to Supabase!"


def get_data():
    response = supabase.table("questions").select("*").execute()
    return response.data