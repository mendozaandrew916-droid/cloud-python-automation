import os
import json
from datetime import datetime

LOG_DIR = "system_logs"
REPORT_FILE = "system_health_report.md"

CPU_THRESHOLD = 10.0
DISK_THRESHOLD = 30.0

def generate_health_report():
    """Reads json telemetry logs and generates a structured Markdown health report."""
    if not os.path.exists(LOG_DIR):
        print(f"DIRECTORY '{LOG_DIR}' does not exist.")
        return

    json_files = [f for f in os.listdir(LOG_DIR) if f.startswith("realtime_log_") and f.endswith(".json")]

    if not json_files:
        print("NO real-time JSON log files found to report on.")
        return

    total_cpu = 0.0
    total_memory = 0.0
    total_disk = 0.0
    alerts = []

    for file_name in json_files:
        file_path = os.path.join(LOG_DIR, file_name)
        with open (file_path, "r") as f:
            data = json.load(f)

        metrics = data["metrics"]
        cpu = metrics["cpu_usage_percent"]
        memory = metrics["memory_usage_percent"]
        disk = metrics["disk_usage_percent"]

        total_cpu += cpu
        total_memory += memory
        total_disk += disk

        #Collect threshold violations

        if cpu > CPU_THRESHOLD:
            alerts.append(f"- **{file_name}**: HIGH CPU Usage ('{cpu}%') breaches limit ('{CPU_THRESHOLD}%')")
        if disk > DISK_THRESHOLD:
            alerts.append(f"-**{file_name}**: HIGH Disk Usage ('{disk}'%) breaches limit ('{DISK_THRESHOLD}%')")
    


    log_count = len(json_files)
    avg_cpu = total_cpu / log_count
    avg_memory = total_memory / log_count
    avg_disk = total_disk / log_count
    report_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #Constuct formatted Markdown content
    report_content =f"""# System Health & Telemetry Executive Report
**Generated On:** '{report_timestamp}'
**Environment:** 'codesspace-linux'
**Engineer:** Andrew Mendoza

---
## Fleet Average ({log_count} Log Analyzed)
| Metric | Average Value | Status |
| :--- | :--- | :--- |
| **CPU Usage** | '{avg_cpu:.2f}%' | {' Warning' if avg_cpu > CPU_THRESHOLD else ' Normal'} |
| **RAM Usage** | '{avg_memory:.2f}%' | Normal |
| **Disk Usage** | '{avg_disk:.2f}%' | {' Warning' if avg_disk > DISK_THRESHOLD else ' Normal'} |

---

## Triggered Incedents ({len(alerts)})
"""

    if alerts: 
        for alert in alerts:
            report_content += f"{alert}\n"
    else:
        report_content += "*No active alerts detected across telemetry checks.*\n"

    #Write the report content to file
    with open(REPORT_FILE, "w") as f:
        f.write(report_content)

    print(f"Health report successfully written to '{REPORT_FILE}'!")

if __name__ == "__main__":
    generate_health_report()