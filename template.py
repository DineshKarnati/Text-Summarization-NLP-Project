import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
                 
project_name = "End-to-End-Text_Summarisation_using_CI-CD_Pipeline"

list_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
   "config/config.yaml",
   "params.yaml" ,
   "app.py",
   "main.py",
   "Dockerfile",
   "requirements.txt",
   "setup.py",
   "research/trails.ipynb",
]

for file_path in list_files:
    #path library can take care of back slash(windows_) and front slash(linux)
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path) #split return directory and file name
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0): #checking size so that it will replace onlu when it is empty
        with open(file_path,'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    
    else:
        logging.info(f"{filename} is already exists")
        
        
        
    
     