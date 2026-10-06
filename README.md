# Cloud-Native Python System Monitoring & Automation Pipeline

![Cloud Python Automation Pipeline](https//github.com/mendozaandrew916-droid/cloud-python-automation/actions/workflows/automation_ci.yml/badge.svg)

An automated, cross-platform infrastructure telemetry and monitoring suite built in Python. Features real-time log ingestion, threshold-alerting, log retention policy enforcement, automated unit testing (`pytest`), dynamic executive report generation, and multi-environment GitHub Actions CI/CD matrix integration.

---

## Architecture & Core Components

| Component | Technology | Description
| :--- | :--- | :--- |
| **Telemetry Ingestion** | `psutil`, `json` | Captures CPU, RAM, and disk utilization metrics into structured JSON telemetry logs. |
| **Log Analysis & Alerts** | Python, `os`, `glob` | Parses generated telemetry logs and flags system resource breaches against defined thresholds. |
| **Report Generation** | Markdown | Aggregates fleet averages and triggered incidents into an executive status report (`system_health_report.md`). |
| **Log Retention** | Python `os.remove` | Automatically enforces retention policies, purging stale log files to save disk storage. |
| **Unit Testing** | `pytest` | Validates metric parsing logic, threshold checks, and mock filesystem operations before deployment. |
| **Pipeline Orchestrator**| `subprocess`, `sys` | Sequentially executes testing, logging, parsing, reporting, and retention cleanup with error handling. |
| **CI/CD Automation** | GitHub Actions | Executes parallel cross-platform matrix builds (`Linux`, `Windows`, `macOS`), scheduled cron jobs, and artifact delivery. |

---

# Quickstart (Local Execution)

### 1. Prerequisites & Installation
```bash
git clone [https://github.com/mendozaandrew916-droid/cloud-python-automation.git](https://github.com/mendozaandrew916-droid/cloud-python-automation.git)
cd cloud-python-automation
pip install psutil pytest
