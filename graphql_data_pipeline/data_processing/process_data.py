from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import pandas as pd
import os

# Initialize FastAPI app
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Folder containing cleaned data
OUTPUT_FOLDER = r"C:\Users\Admin\Desktop\PROJECTS\DATA ENGINEERING\Data Engineer Assessment\Cleaned_data"

def get_cleaned_files():
    """Retrieve available cleaned files in the output folder."""
    if not os.path.exists(OUTPUT_FOLDER):
        return []
    return [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith((".csv", ".parquet"))]

def load_cleaned_data(file_name: str):
    """Load cleaned data from the selected file."""
    file_path = os.path.join(OUTPUT_FOLDER, file_name)

    if not os.path.exists(file_path):
        return None

    if file_name.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_name.endswith(".parquet"):
        return pd.read_parquet(file_path)
    
    return None

@app.get("/")
def home():
    return {"message": "Welcome to the Loan Data API!"}

@app.get("/files")
def list_cleaned_files():
    """List all available cleaned data files."""
    files = get_cleaned_files()
    return {"available_files": files}

@app.get("/table", response_class=HTMLResponse)
def show_data_table(request: Request, file: str = Query(None, description="Specify the filename")):
    """Render the loan data as an HTML table."""
    if file is None:
        return {"error": "Please specify a filename from /files endpoint"}

    df = load_cleaned_data(file)

    if df is None:
        return {"error": f"File '{file}' not found or unsupported format."}

    df = df.replace([float("inf"), float("-inf")], pd.NA).fillna(0)

    return templates.TemplateResponse("index.html", {"request": request, "data": df.to_dict(orient="records")})

