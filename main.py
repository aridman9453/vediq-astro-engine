from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import router as auth_router
from astrology import router as astrology_router
from birth_chart import router as birth_chart_router
from swisseph_router import router as swisseph_router
from palm_router import router as palm_router
from ai_astrologer_router import router as ai_astrologer_router
from astrologer_router import router as astrologer_router
app = FastAPI(title="vedIQ Astro Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(astrology_router)
app.include_router(birth_chart_router)
app.include_router(swisseph_router)
app.include_router(palm_router)
app.include_router(ai_astrologer_router)
app.include_router(astrologer_router)

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
