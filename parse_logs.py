import os
import json

LOG_DIR = "system_logs"

#Thresholds for trigerring alerts
CPU_THRESHOLD = 10.0
DISK_THRESHOLD = 30.0

def analyze_realtime_logs():
    """Parses JSON logs, calculates system averages, and flags threshold alerts. """
    if not os.path.exists(LOG_DIR):
        print(f"Directory '{LOG_DIR}' does not exist.")
        return

    # Filter specifically for our new realtime JSON logs
    json_files = [f for f in os.listdir(LOG_DIR) if f.startswith("realtime_log_") and f.endswith(".json")]

    if not json_files:
        print("NO real-time JSON log files found to analyze.")
        return

    total_cpu = 0.0
    total_memory = 0.0
    total_disk = 0.0
    alerts_triggered = 0
    log_count = len(json_files)

    print(f"Analyzing {log_count} Real-TimeJSON log files...\n")

    for file_name in json_files:
        file_path = os.path.join(LOG_DIR, file_name)

        #Read JSON file

        with open(file_path, "r") as f:
            data = json.load(f)
        
        #Extracted nested metrics
        metrics = data["metrics"]
        cpu = metrics["cpu_usage_percent"]
        memory = metrics["memory_usage_percent"]
        disk = metrics["disk_usage_percent"]

        total_cpu += cpu
        total_memory += memory
        total_disk += disk

        #Check for threshold breaches
        has_alert = False
        alert_reasons = []

        if cpu > CPU_THRESHOLD:
            has_alert = True
            alert_reasons.append(f"High CPU ({cpu}%)")

        if disk > DISK_THRESHOLD:
            has_alert = True
            alert_reasons.append(f"High Disk({disk}%)")

        if has_alert:
            alerts_triggered += 1
            print(f"[ALERT] {file_name} -> {', '.join(alert_reasons)}")    
        else:
            print(f"[OK] {file_name} -> CPU: {cpu}% | RAM: {memory}% | DISK: {disk}%")

    
    avg_cpu = total_cpu / log_count
    avg_memory = total_memory / log_count
    avg_disk = total_disk / log_count

    print("\n--- Real-Time Fleet Summary ---")
    print(f"Files Analyzed:         {log_count}")
    print(f"Total Alerts Raised:    {alerts_triggered}")
    print(f"Average CPU Usage:      {avg_cpu:.2f}%")
    print(f"Average Memory Usage:   {avg_memory:.2f}%")
    print(f"Average Disk Usage:     {avg_disk:.2f}%")
    print("----------------------------------")

if __name__ == "__main__":
    analyze_realtime_logs()