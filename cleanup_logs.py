import os
import glob

LOG_DIR = "system_logs"

def cleanup_old_logs(keep_recent=3):
    """Deletes older log files, preserving only the most recent N logs."""
    if not os.path.exists(LOG_DIR):
        print(f"Directory '{LOG_DIR}' does not exist.")
        return

    #Find all JSON log files in the directory
    log_files = glob.glob(os.path.join(LOG_DIR, "*.json"))

    #Sort files by creation/modification time (oldest first)
    log_files.sort(key=os.path.getmtime)

    total_files = len(log_files)
    if total_files <= keep_recent:
        print(f"Total logs  ({total_files}) <= retain limit ({keep_recent}). No cleanup needed.")
        return

    #Determine files to remove
    files_to_delete = log_files[:total_files - keep_recent]

    print(f"Cleaning up {len(files_to_delete)} old log file(s)...\n")
    for file_path in files_to_delete:
        os.remove(file_path)
        print(f"Deleted: {file_path}")

    print(f"\nCleanup complete! kepth the {keep_recent} most recent logs.")

if __name__ == "__main__":
    cleanup_old_logs(keep_recent=3)
