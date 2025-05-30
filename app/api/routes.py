from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel

from app.core.logger import setup_logger
from app.services.analyzer import analyze_repository

logger = setup_logger("routes")
router = APIRouter()

class AnalyzeRequest(BaseModel):
    repo_url: str

@router.post("/analyze")
def analyze(repo_url: str = Form(...)):
    logger.info(f"🔍 Api Execution")
    try:
        result = analyze_repository(repo_url)
        return {"success": True, "insights": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/analyseJson")
def analyze_json(payload: AnalyzeRequest):
    logger.info(f"🔍 JSON Route Received: {payload.repo_url}")
    try:
        result = analyze_repository(payload.repo_url)
        return {"success": True, "insights": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))