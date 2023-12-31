# File to create project structure
import os
from pathlib import Path
import logging

# setting the log format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Chicken_Disease_Classification"

list_of_files = [
    ".github/workflows/.gitkeep", #stores the main.yaml file that contains CI/CD commands
    f"src/{project_name}/__init__.py", # creates a package (constructor)
    f"src/{project_name}/components/__init__.py", #components of the pipeline
    f"src/{project_name}/utils/__init__.py", #commmonly used functions (utility functions)
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", #configuration functions
    f"src/{project_name}/pipeline/__init__.py", #pipeline stages
    f"src/{project_name}/entity/__init__.py", #configuration classes
    f"src/{project_name}/constants/__init__.py", #constants
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml", #model hyperparameters
    "requirements.txt", #dependencies
    "setup.py",
    "research/trials.ipynb", #experiments are performed before writing components
    "templates/index.html" #front-end interface
] 

for filepath in list_of_files:
    filepath = Path(filepath) # converts path to Windows format
    filedir, filename = os.path.split(filepath)

    # checking if no file directory is specified
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # checking if folder/file already exists or contains some data to prevent overwriting
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filepath} already exists")