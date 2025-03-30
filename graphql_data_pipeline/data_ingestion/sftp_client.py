import paramiko
import os

# Import credentials
from config import SFTP_HOST, SFTP_PORT, SFTP_USER, SFTP_PASS

# Local folder to store downloaded files
DOWNLOAD_FOLDER = r"C:\Users\Admin\Desktop\PROJECTS\DATA ENGINEERING\Data Engineer Assessment\Sample_data"

def connect_sftp():
    """Establish SFTP connection and return the client."""
    try:
        transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
        transport.connect(username=SFTP_USER, password=SFTP_PASS)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print("✅ Connected to SFTP successfully!")
        return sftp
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def download_files():
    """Fetch files from SFTP and save them locally."""
    sftp = connect_sftp()
    if sftp:
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        files = sftp.listdir('.')
        
        for file in files:
            local_path = os.path.join(DOWNLOAD_FOLDER, file)
            sftp.get(file, local_path)
            print(f"📥 Downloaded: {file}")
        
        sftp.close()
    else:
        print("❌ Unable to download files.")

if __name__ == "__main__":
    download_files()
