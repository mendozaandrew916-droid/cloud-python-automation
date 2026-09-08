import os 
import time
import json
from datetime import datetime

LOG_DIR = "system_logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Simulated monitoring loop (Runs 4 times then stops)
def run_json_monitor(iterations=4, interval=3):

    print(f"Starting JSON Cloud Monitor ({iterations} checks every {interval}...\n)")

    for count in range (1, iterations + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #Created structured data using python dictionary like java hashmap
        log_data = {
            "check_id": count,
            "timestamp": str(datetime.now()),
            "environment": "production-simulation",
            "server_status": "ALL SYSTEMS GREEN",
            "engineer": "ANDREW MENDOZA",
            "metrics": {
                "cpu_usage_percent": 12.5,
                "memory_usage_percent": 41.2
            }
        }

        file_path = os.path.join(LOG_DIR, f"log_check_{count}_{timestamp}.json")

        #write dictionary directly to a JSON file 
        with open(file_path, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"[{count}/{iterations}] Generated JSON Log: {file_path}")

        # Pause execution if not on the final iteration
        if count < iterations:
            time.sleep(interval)


if __name__ == "__main__":
     run_json_monitor(iterations=4, interval=3)
     print("JSON Monitoring complete. All structured logs saved successfully!")

    