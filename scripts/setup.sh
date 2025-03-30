#!/bin/bash

echo "🔧 Setting up the GraphQL Data Pipeline project..."

# Install required libraries
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn paramiko pandas pyarrow sqlalchemy psycopg2-binary graphene

# Define directories
dirs=(
    "graphql_data_pipeline"
    "graphql_data_pipeline/data_ingestion"
    "graphql_data_pipeline/api"
    "graphql_data_pipeline/config"
    "graphql_data_pipeline/tests"
    "graphql_data_pipeline/scripts"
)

# Create directories
echo "📂 Creating project structure..."
for dir in "${dirs[@]}"; do
    mkdir -p "$dir"
done

# Create files
touch graphql_data_pipeline/data_ingestion/{sftp_client.py,process_data.py,__init__.py}
touch graphql_data_pipeline/api/{schema.py,app.py,__init__.py}
touch graphql_data_pipeline/config/settings.py
touch graphql_data_pipeline/tests/{test_pipeline.py,test_api.py}
touch graphql_data_pipeline/scripts/{setup.sh,setup.py}
touch graphql_data_pipeline/{requirements.txt,README.md,.gitignore,docker-compose.yml,main.py}

echo "✅ Setup complete! Your project is ready."
