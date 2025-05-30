# server.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router  # This is the actual APIRouter instance
from app.core.logger import setup_logger

logger = setup_logger("fastapi")
logger.info("🚀 Starting Code Analyzer API...")

app = FastAPI(title="Code Analyzer API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],  # or ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# ✅ Corrected: router is already an APIRouter
app.include_router(router)
