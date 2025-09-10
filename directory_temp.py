import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "app/__init__.py",
    "app/config.py",
    "app/main.py",
    "app/models/__init__.py",
    "app/models/vector_store.py",
    "app/services/__init__.py",
    "app/services/llm_service.py",
    "app/services/storage_service.py",    
    "app/static/style.css",
    "app/templates/index.html",
    "data/data.py",
    "pyproject.toml",
    "Dockerfile",
    "requirements.txt",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
