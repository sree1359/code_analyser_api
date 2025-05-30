# cli/run_analysis.py
import sys
from app.services.analyzer import analyze_repository
from app.core.logger import setup_logger

logger = setup_logger("cli")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python run_analysis.py <repo_url>")
        sys.exit(1)

    url = sys.argv[1]
    logger.info(f"🔍 Starting CLI analysis for: {url}")
    analyze_repository(url)
