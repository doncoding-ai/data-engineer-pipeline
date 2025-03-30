from fastapi import FastAPI, Query, Header, HTTPException
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

# Define API key from the environment file or directly
API_KEY = "b4018989fbdbe701b3fb87efe46021d0d971af833a4d324bf9753c8a1a08b519"
API_KEY_NAME = "X-API-Key"

# Helper function to validate API Key
def validate_api_key(api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")

# Helper functions for loading data
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
        return pd.read_csv(file_path, parse_dates=["effective_date", "due_date"])
    elif file_name.endswith(".parquet"):
        return pd.read_parquet(file_path)
    
    return None

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the Loan Data API!"}

# Files route to list available cleaned data files
@app.get("/files")
def list_cleaned_files():
    """List all available cleaned data files."""
    files = get_cleaned_files()
    return {"available_files": files}

# Data route with authentication and pagination
@app.get("/data")
def get_filtered_data(
    file: str = Query(None, description="Specify the filename"),
    start_date: str = Query(None, description="Filter start date (YYYY-MM-DD)"),
    end_date: str = Query(None, description="Filter end date (YYYY-MM-DD)"),
    cursor: int = Query(None, description="Pagination cursor (loan_id)"),
    limit: int = Query(10, description="Number of records per page"),
    api_key: str = Header(None)
):
    """Retrieve filtered loan data with pagination."""
    validate_api_key(api_key)  # Validate the API Key

    if file is None:
        return {"error": "Please specify a filename from /files endpoint"}

    df = load_cleaned_data(file)

    if df is None:
        return {"error": f"File '{file}' not found or unsupported format."}

    if "effective_date" not in df.columns or "due_date" not in df.columns:
        return {"error": "Missing required date columns in the dataset."}

    # Convert dates to datetime (if not already)
    df["effective_date"] = pd.to_datetime(df["effective_date"], errors="coerce")
    df["due_date"] = pd.to_datetime(df["due_date"], errors="coerce")

    # Apply date filters
    if start_date:
        df = df[df["effective_date"] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df["due_date"] <= pd.to_datetime(end_date)]

    # Apply cursor-based pagination
    if cursor is not None:
        df = df[df["loan_id"] > cursor]  # Fetch records after the cursor

    # Limit the results
    df = df.sort_values("loan_id").head(limit)

    # Get the next cursor (last loan_id in the current batch)
    next_cursor = df["loan_id"].max() if not df.empty else None

    return {
        "data": df.to_dict(orient="records"),
        "next_cursor": next_cursor
    }

# Table route with authentication
@app.get("/table", response_class=HTMLResponse)
def show_data_table(request: Request, file: str = Query(None, description="Specify the filename"), api_key: str = Header(API_KEY)):
    """Render the loan data as an HTML table."""
    validate_api_key(API_KEY)  # Validate the API Key

    if file is None:
        return {"error": "Please specify a filename from /files endpoint"}

    df = load_cleaned_data(file)

    if df is None:
        return {"error": f"File '{file}' not found or unsupported format."}

    df = df.replace([float("inf"), float("-inf")], pd.NA).fillna(0)

    return templates.TemplateResponse("index.html", {"request": request, "data": df.to_dict(orient="records")})

# Run the API using Uvicorn (only when executed directly)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
