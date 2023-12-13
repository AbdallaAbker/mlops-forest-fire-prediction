import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format = "[%(asctime)s: %(levelname)s: %(filename)s: %(module)s: %(message)s]")

project_name = "forest_fire_prediction"
list_of_files = [
                    ".github/workflows/.gitkeep",
                    # "artifacts/dataset/raw/data.csv",
                    # "artifacts/dataset/processed/data.csv",
                    # "artifacts/model/model.pkl",
                    "src/__init__.py", #constructor file to consider as local package
                    "src/components/__init__.py",
                    "src/components/data_ingestion.py",
                    "src/components/data_transformation.py",
                    "src/components/model_trainer.py",
                    # "src/components/model_evalution.py",
                    # "src/config/configuration.py",
                    "src/pipeline/__init__.py",
                    "src/pipeline/train_pipeline.py",
                    "src/pipeline/predict_pipeline.py",
                    # "src/entity/__init__.py",
                    # "src/constants/__init__.py",
                    "src/logging/__init__.py",
                    "src/exception/__init__.py",
                    "src/utils/__init__.py",
                    "src/utils/common.py",
                    "config/config.yaml",
                    "params.yaml",
                    "app.py",
                    "main.py",
                    "Dockerfile",
                    "requirements.txt",
                    "setup.py",
                    "expirement/EDA.ipynb"
                ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #Check if the directory already exists
    if filedir is not None and filedir != "":
        os.makedirs(filedir, exist_ok= True)  # create a directory if it doesn't exist
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    #check if the file already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists in {filedir}")