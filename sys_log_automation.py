import os 

from datetime import datetime 

LOG_DIR = "system_logs"
CURRENT_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
FILE_PATH = os.path.join(LOG_DIR, f"log_{CURRENT_TIME}.txt")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    print(f"📁 Directory '{LOG_DIR}' created successfully")

with open(FILE_PATH, "w") as file:
    file.write("=== CLOUD SYSTEM HEALTH REPORT ===\n")
    file.write(f"Timestamp: {datetime.now()}\n")
    file.write(f"Executed By: Engineer Mendoza\n")
    file.write("Status: ALL SYSTEMS OPERATIONAL\n")

    print(f"✅ Generated Log File: {FILE_PATH}")
