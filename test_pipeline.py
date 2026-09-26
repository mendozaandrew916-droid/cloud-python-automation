import os
import json
import pytest
from report_generator import CPU_THRESHOLD, DISK_THRESHOLD

def test_threshold_values():
    """Veryify threshold constant are non-negative floats/ints."""
    assert CPU_THRESHOLD >= 0
    assert DISK_THRESHOLD >= 0

def test_log_file_parsing(tmp_path):
    """Test JSON parsing and metric extraction using a temporary mock log file."""
    #Create a mock log directory using pytest
    mock_log_dir = tmp_path / "system_logs"
    mock_log_dir.mkdir()

    sample_log = mock_log_dir / "realtime_log_test.json"
    sample_data = {
        "timestamp": "2026-09-26 12:00:00",
        "metrics": {
            "cpu_usage_percent": 15.5,
            "memory_usage_percent": 45.0,
            "disk_usage_percent": 55.2
        }
    }
    sample_log.write_text(json.dumps(sample_data))

    #Read and parse back the mock file
    with open(sample_log, "r") as f:
        data = json.load(f)

    #Assert metric extraction integrity 
    assert "metrics" in data
    assert data["metrics"]["cpu_usage_percent"] == 15.5
    assert data["metrics"]["cpu_usage_percent"] > CPU_THRESHOLD