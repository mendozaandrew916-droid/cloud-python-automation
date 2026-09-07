import os 
import time
from datetime import datetime

LOG_DIR = "system_logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Simulated monitoring loop (Runs 4 times then stops)
def run_monitor(iterations=4, interval=3):

    print(f"Starting Cloud Monitor (Running {iterations} checks every {interval}...\n)")

    for count in range (1, iterations + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(LOG_DIR, f"log_check_{count}_{timestamp}.txt")

        with open(file_path, "w") as f:
            f.write(f"Check #{count}\nTimestamp: {datetime.now()}\nServer Status: ALL SYSTEMS GREEN - ANDREW MENDOZA\n")

        print(f"[{count}/{iterations}] Generated: {file_path}")

        # Pause execution if not on the final iteration
        if count < iterations:
            time.sleep(interval)


if __name__ == "__main__":
     run_monitor(iterations=4, interval=3)
     print("Monitoring complete. All logs saved successfully!")

    