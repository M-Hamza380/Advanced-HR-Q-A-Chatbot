import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)s : %(message)s ]"
)

Project_Name = "hr_qna_bot"

list_of_file = [
    f"src/{Project_Name}/__init__.py",
    f"src/{Project_Name}/backend/static/main.css",
    f"src/{Project_Name}/backend/errors/500.html",
    f"src/{Project_Name}/backend/templates/index.html",
    f"src/{Project_Name}/backend/templates/layout.html",
    f"src/{Project_Name}/backend/templates/change_password.html",
    f"src/{Project_Name}/backend/templates/dashboard.html",
    f"src/{Project_Name}/backend/templates/login.html",
    f"src/{Project_Name}/backend/templates/register.html",
    f"src/{Project_Name}/backend/templates/reset_request.html",
    f"src/{Project_Name}/backend/templates/reset_token.html",
    f"src/{Project_Name}/backend/templates/creat_mcqs.html",
    f"src/{Project_Name}/backend/users/main/__init__.py",
    f"src/{Project_Name}/backend/users/main/routes.py",
    f"src/{Project_Name}/backend/users/forms/__init__.py",
    f"src/{Project_Name}/backend/users/forms/user_forms.py",
    f"src/{Project_Name}/backend/users/database/__init__.py",
    f"src/{Project_Name}/backend/users/database/models.py",
    f"src/{Project_Name}/backend/config.py",
    f"src/{Project_Name}/backend/views.py",
    f"src/{Project_Name}/backend/main.py",
    f"src/{Project_Name}/rag/__init__.py",
    f"src/{Project_Name}/rag/components/__init__.py",
    f"src/{Project_Name}/rag/components/prompt.py",
    f"src/{Project_Name}/rag/components/data_ingestion.py",
    f"src/{Project_Name}/rag/components/data_validation.py",
    f"src/{Project_Name}/rag/components/vector_embeddings.py",
    f"src/{Project_Name}/rag/components/llm_model.py",
    f"src/{Project_Name}/rag/constants/__init__.py",
    f"src/{Project_Name}/rag/pipeline/__init__.py",
    f"src/{Project_Name}/rag/pipeline/llm_pipeline.py",
    f"src/{Project_Name}/rag/app.py",
    f"src/{Project_Name}/utils/__init__.py",
    f"src/{Project_Name}/utils/logger.py",
    f"src/{Project_Name}/utils/exception.py",
    f"src/{Project_Name}/utils/common.py",
    f"src/{Project_Name}/notebook/exp.ipynb",
    "Makefile",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "docker-compose.yml",
]

for file_path in list_of_file:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_name} is already exists.")