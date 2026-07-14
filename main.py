from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from supabase_client import supabase

app = FastAPI(title="vedIQ Astro Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "vedIQ Astro Engine"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/supabase-test")
def supabase_test():
    try:
        response = supabase.table("profiles").select("*").limit(1).execute()

        return {
            "status": "connected",
            "database": "ok",
            "rows_returned": len(response.data)
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
