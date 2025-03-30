import schedule
import time
from sftp_client import download_files

def job():
    """Scheduled task to fetch new data from SFTP."""
    print("🚀 Running data fetch job...")
    download_files()
    print("✅ Job completed!")

# Schedule to run every day at midnight
schedule.every().day.at("00:00").do(job)

print("📅 Data Fetcher Running. Press CTRL+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)
