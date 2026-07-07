from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore" / "chroma"

KAGGLE_DATASET_ID = "pythonafroz/medquad-medical-question-answer-for-ai-research"

OLLAMA_BASE_URL = "http://127.0.0.1:11434"
OLLAMA_MODEL = "gemma4:latest"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100
TOP_K = 5

# print(PROJECT_ROOT)
# print(DATA_DIR)
print(RAW_DATA_DIR)
print(PROCESSED_DATA_DIR)
# print(VECTORSTORE_DIR)
# print(KAGGLE_DATASET_ID)
# print(OLLAMA_BASE_URL)
# print(OLLAMA_MODEL)
# print(CHUNK_SIZE)
# print(CHUNK_OVERLAP)
# print(TOP_K)