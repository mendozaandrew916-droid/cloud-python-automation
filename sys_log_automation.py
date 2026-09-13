import os 
import time
import json
import psutil
from datetime import datetime

LOG_DIR = "system_logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def capture_system_metrics():
    """Capture Live CPU, Memory, and Disc metrics from the Linux OS."""
    return{
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent
    }

def run_realtime_monitor(iterations=3, interval=2):
    """Runs the monitoring loop using live hardware data."""
    print(f"Starting Real-Time Cloud Monitor ({iterations} checks every {interval}s)...\n)")

    for count in range (1, iterations + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        #Call function to get real live data
        live_metrics = capture_system_metrics()
        log_data = {
            "check_id": count,
            "timestamp": str(datetime.now()),
            "environment": "codespsaces-linux",
            "server_status": "ALL SYSTEMS GREEN",
            "engineer": "ANDREW MENDOZA",
            "metrics": live_metrics
        }

        file_path = os.path.join(LOG_DIR, f"realtime_log_{count}_{timestamp}.json")

        #write dictionary directly to a JSON file 
        with open(file_path, "w") as f:
            json.dump(log_data, f, indent=4)

        print(f"[{count}/{iterations}] Saved Live Log: {file_path}")
        print(f"    CPU: {live_metrics['cpu_usage_percent']}% | RAM: {live_metrics['memory_usage_percent']}% | DISK: {live_metrics['disk_usage_percent']}%\n")
        
        # Pause execution if not on the final iteration
        if count < iterations:
            time.sleep(interval)


if __name__ == "__main__":
     run_realtime_monitor(iterations=3, interval=2)
 

    