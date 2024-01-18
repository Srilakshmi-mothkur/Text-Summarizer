import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/(textSummarizer)/__init__.py",
    f"src/(textSummarizer)/components/__init__.py",
    f"src/(textSummarizer)/utils/__init__.py",
    f"src/(textSummarizer)/utils/common.py",
    f"src/(textSummarizer)/logging//__init__.py",
    f"src/(textSummarizer)/config/__init__.py",
    f"src/(textSummarizer)/config/configuration.py",
    f"src/(textSummarizer)/pipeline/__init__.py",
    f"src/(textSummarizer)/entity/__init__.py",
    f"src/(textSummarizer)/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating emtpty file: {filepath}")

    
    else:
        logging.info(f"{filename} already exists")
