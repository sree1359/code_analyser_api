# server.py
from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import setup_logger

logger = setup_logger("fastapi")
logger.info("🚀 Starting Code Analyzer API...")

app = FastAPI(title="Code Analyzer API")
app.include_router(router)
