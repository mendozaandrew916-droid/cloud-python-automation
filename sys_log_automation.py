import os 
import time
from datetime import datetime

LOG_DIR = "system_logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def run_monitor(iterations=3, interval=5):
    print(f"Starting Cloud Monitor (Running {iterations} checks every {intervals}...\n)")

    for count in range (1, iteration + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_poth = os.path.join(LOG_DIR, f"log_check_{count}_{time}.txt")

        with open(file_poth, "w") as f:
            f.write(f"Check #{count}\nTimestamp: {datetime.now()}\nStatus: OPERATIONAL\n")

        print(f"[{count}/{iterations}] Generated: {file_poth}")

        if count < iterations:
            time.sleep(interval)


        if __name__ == "__main__":
            run_monitor()
