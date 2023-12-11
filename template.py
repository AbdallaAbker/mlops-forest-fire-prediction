import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format = "[%(asctime)s: %(levelname)s: %(filename)s: %(module)s: %(message)s]")

project_name = "forest_fire_prediction"
list_of_files = [
                    ".github/workflows/.gitkeep",
                    f"src/{project_name}/__init__.py", #constructor file to consider as local package
                    # f"src/{project_name}/components/__init__.py",
                    # f"src/{project_name}/utils/__init__.py",
                    # f"src/{project_name}/utils/common.py",
                    f"src/{project_name}/logging/__init__.py",
                    # f"src/{project_name}/config/configuration.py",
                    f"src/{project_name}/pipeline/__init__.py",
                    # f"src/{project_name}/entity/__init__.py",
                    # f"src/{project_name}/constants/__init__.py",
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