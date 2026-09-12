import os
import json

LOG_DIR = "system_logs"

def analyze_logs():
    if not os.path.exists(LOG_DIR):
        print(f"Directory '{LOG_DIR}' does not exist.")
        return

    # List all files ending with .json
    json_files = [f for f in os.listdir(LOG_DIR) if f.endswith(".json")]

    if not json_files:
        print("NO json log files found to analyze.")
        return

    total_cpu = 0.0
    total_memory = 0.0
    log_count = len(json_files)

    print(f"Analyzing {log_count} JSON log files...\n")

    for file_name in json_files:
        file_path = os.path.join(LOG_DIR, file_name)

        #Read JSON file

        with open(file_path, "r") as f:
            data = json.load(f)

        cpu = data["metrics"]["cpu_usage_percent"]
        memory = data["metrics"]["memory_usage_percent"]

        total_cpu += cpu
        total_memory += memory

        print(f"Parsed {file_name} -> CPU: {cpu}%, Memory: {memory}%")
    
    avg_cpu = total_cpu / log_count
    avg_memory = total_memory / log_count

    print("\n--- System Health Summary ---")
    print(f"Average CPU Usage: {avg_cpu:.2f}%")
    print(f"Average Memory Usage: {avg_memory:.2f}%")
    print("----------------------------------")

if __name__ == "__main__":
    analyze_logs()