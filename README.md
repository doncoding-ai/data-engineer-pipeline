# Data Engineering: Data Pipeline and API Challenge

## Overview
This project involves the development of a scalable data pipeline that ingests data from an SFTP location, processes it for analytical use, and exposes it through a secure API with date-based filtering and cursor-based pagination.

## Background
The project is designed for an on-premise server environment and aims to:
- Ingest data from an SFTP location.
- Process and clean the data for consistency and structure.
- Expose an API for external clients to access the processed data with support for date filtering and cursor-based pagination.

## Requirements

### 1. Data Ingestion
- Retrieve data files from an SFTP location.
- Support various data formats (CSV & JSON).
- Implement error handling for failed transfers and generate alerts.

### 2. Data Processing
- Flatten and clean the ingested data for business consumption.
- Apply data quality measures to ensure consistency.

### 3. API Development
- Develop an API for external clients to access processed data.
- Implement date filtering and cursor-based pagination.
- Ensure basic security and rate limiting.

## Deliverables

### 1. Working Data Pipeline
- A script or automated process to ingest data from the SFTP location.
- A robust pipeline capable of handling data inconsistencies.
- Curated datasets ready for business consumption.

### 2. API with Documentation
- A functional API enabling data retrieval with filtering and pagination.
- Detailed API documentation covering authentication, endpoints, and rate limits.

## Implementation

### Data Ingestion
- Uses Paramiko to securely connect to an SFTP server and retrieve files.
- Supports both CSV and JSON formats.
- Logs all operations and raises alerts for failures.

### Data Processing
- Cleans and flattens ingested data using Pandas.
- Converts relevant fields to appropriate formats (e.g., date parsing).
- Stores curated datasets in a structured format for easy access.

### API Development
- Built using FastAPI for high performance.
- Implements date filtering and cursor-based pagination.
- Secured with API key authentication.

## API Usage

### Endpoints

| Endpoint   | Method | Description                            |
|------------|--------|----------------------------------------|
| `/files`   | GET    | List available cleaned data files.    |
| `/data`    | GET    | Retrieve filtered loan data with pagination. |
| `/table`   | GET    | Render data as an HTML table.        |

### Authentication
All API requests require an API Key (`X-API-Key`) in the request header.

### Example Request (Using curl)
```sh
curl -H "X-API-Key: your_api_key" "http://127.0.0.1:8000/data?file=data.csv&start_date=2016-01-01&end_date=2016-12-31&limit=10"
```

## Assumptions
- A simulated SFTP server is used for data ingestion.
- Sample loan data is used to demonstrate functionality.
- The API is hosted locally (`127.0.0.1:8000`).

## Deployment
### Clone the repository and install dependencies:
```sh
git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt
```

### Run the FastAPI server:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Version Control
This project follows an iterative development approach using GitHub/GitLab/BitBucket.

## Conclusion
This project successfully implements a data pipeline and API to manage and serve processed data efficiently. The pipeline ensures data consistency and quality, while the API provides structured access with filtering and pagination capabilities.

**Happy Coding! 🚀**
