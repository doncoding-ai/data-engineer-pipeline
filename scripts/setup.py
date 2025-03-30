import os

# Define project structure
project_structure = {
    "graphql_data_pipeline": [
        "data_ingestion/sftp_client.py",
        "data_ingestion/process_data.py",
        "data_ingestion/__init__.py",
        "api/schema.py",
        "api/app.py",
        "api/__init__.py",
        "config/settings.py",
        "tests/test_pipeline.py",
        "tests/test_api.py",
        "scripts/setup.sh",
        "scripts/setup.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "docker-compose.yml",
        "main.py"
    ]
}

def create_project_structure():
    """Creates the project directories and files."""
    for base, files in project_structure.items():
        for file_path in files:
            file_dir = os.path.dirname(file_path)
            full_dir = os.path.join(base, file_dir)
            full_path = os.path.join(base, file_path)

            # Create directories if they don't exist
            if file_dir and not os.path.exists(full_dir):
                os.makedirs(full_dir)

            # Create empty files
            with open(full_path, 'w') as f:
                pass

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
