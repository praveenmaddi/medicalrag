import json
from pathlib import Path

from config import PROCESSED_DATA_DIR


def load_documents():
    """
    Load preprocessed medical documents.
    """

    file_path = Path(PROCESSED_DATA_DIR) / "documents.json"

    with open(file_path, "r", encoding="utf-8") as f:
        documents = json.load(f)

    return documents