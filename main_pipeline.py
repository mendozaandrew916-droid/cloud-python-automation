import sys
import subprocess
from datetime import datetime

#Define the sequence of automation tasks to execute
PIPELINE_STEPS = [
    ("0. Automated Unit testing (pytest)", ["pytest", "test_pipeline.py"]),
    ("1. Live Telemetry Collection", ["python3", "sys_log_automation.py"]),
    ("2. Real-Time log analysis", ["python3", "parse_logs.py"]),
    ("3. Executive Report Generation", ["python3", "report_generator.py"]),
    ("4. Automated Log Retention Cleanup", ["python3", "cleanup_logs.py"])
]

def run_pipeline():
    """Orchestrates the execution of all system automation scripts sequentially."""
    start_time = datetime.now()
    print("==================================================")
    print(" STARTING CLOUD AUTOMATION PIPELINE ")
    print(f"Timestamp: {start_time.strftime('%Y-%m-%d %H-%M-%S')}")
    print("==================================================\n")

    for step_name, command in PIPELINE_STEPS:
        print(f"------------ [{step_name}] ------------")

        #Execute the sub-command and capture execution status
        result = subprocess.run(command, text = True)
        
        if result.returncode == 0:
            print(f"Success: {step_name} completed.\n")
        else: 
            print(f"Failed: {step_name} exited with status code {result.returncode}.")
            print("Pipeline execution halted due to failure.")
            sys.exit(result.returncode)
        
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    print("==================================================")
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print(f"Total Execution Time: {duration:.2f} seconds")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()

