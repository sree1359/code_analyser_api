from app.core.logger import setup_logger
from app.services.repo_cloner import clone_repo
from app.services.file_loader import collect_source_files, read_files
from app.services.chunker import chunk_code
from app.services.extractor import extract_insights
import json
import os
import shutil

logger = setup_logger("analyser")

def analyze_repository(repo_url: str):
    CLONE_DIR = clone_repo(repo_url)
    try:
        source_files = collect_source_files(CLONE_DIR)
        files = read_files(source_files)

        results = []
        for f in files:
            for idx, chunk in enumerate(chunk_code(f['code'])):
                insight = extract_insights(chunk)
                results.append({
                    'file': f['path'],
                    'chunk_index': idx,
                    'insight': insight
                })

        OUTPUT_FILE = 'code_knowledge_output.json'
        logger.info(f"Writing output to: {OUTPUT_FILE}")
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
            json.dump(results, out, indent=2)

        logger.info(f"✅ Extraction complete. JSON saved to {OUTPUT_FILE}")
        return results

    finally:
        logger.info(f"[🧹] Cleaning up: {CLONE_DIR}")
        try:
            shutil.rmtree(CLONE_DIR)
        except Exception as e:
            logger.info(f"[⚠️] Cleanup skipped due to error: {e}")
