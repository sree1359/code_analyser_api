from fastapi import APIRouter, Form, HTTPException
from app.core.logger import setup_logger
from app.services.analyzer import analyze_repository

logger = setup_logger("routes")
router = APIRouter()

@router.post("/analyze")
def analyze(repo_url: str = Form(...)):
    logger.info(f"🔍 Api Execution")
    try:
        result = analyze_repository(repo_url)
        return {"success": True, "insights": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
