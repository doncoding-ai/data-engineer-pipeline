#!/bin/bash

echo "🚀 Setting up the Data Engineering Environment..."

# Update package list
echo "🔄 Updating package list..."
sudo apt update -y && sudo apt upgrade -y

# Install Python and required packages
echo "🐍 Installing Python and dependencies..."
sudo apt install -y python3 python3-pip python3-venv

# Create virtual environment
echo "📂 Creating virtual environment..."
python3 -m venv env
source env/bin/activate

# Install Python dependencies
echo "📦 Installing required Python packages..."
pip install --upgrade pip
pip install \
    pandas \
    paramiko \
    pysftp \
    Flask \
    fastapi \
    uvicorn \
    SQLAlchemy \
    psycopg2-binary \
    mysql-connector-python \
    bcrypt \
    PyJWT \
    fastapi-limiter \
    requests \
    watchgod \
    redis \
    pytest \
    docker-compose

# Install PostgreSQL (if not installed)
if ! command -v psql &> /dev/null; then
    echo "🐘 Installing PostgreSQL..."
    sudo apt install -y postgresql postgresql-contrib
    sudo systemctl start postgresql
    sudo systemctl enable postgresql
fi

# Install Docker (optional for containerization)
if ! command -v docker &> /dev/null; then
    echo "🐳 Installing Docker..."
    sudo apt install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    sudo usermod -aG docker $USER
    echo "⚠️ Please log out and log back in to apply Docker permissions!"
fi

# Install Git (if not installed)
if ! command -v git &> /dev/null; then
    echo "🔧 Installing Git..."
    sudo apt install -y git
fi

echo "✅ Installation complete! Activate the virtual environment using:"
echo "   source env/bin/activate"
