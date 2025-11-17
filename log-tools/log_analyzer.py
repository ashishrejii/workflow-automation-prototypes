import re
from datetime import datetime

def analyze_logs(log_file):
    """
    Analyzes a system log file and returns:
    - Count of ERROR, WARNING, INFO entries
    - Unique error messages
    - Log start and end timestamps
    """

    error_count = 0
    warning_count = 0
    info_count = 0
    unique_errors = set()
    timestamps = []

    with open(log_file, "r") as f:
        for line in f:
            line = line.strip()

            # Count by log level
            if "ERROR" in line:
                error_count += 1
                unique_errors.add(line)
            elif "WARNING" in line:
                warning_count += 1
            elif "INFO" in line:
                info_count += 1

            # Extract timestamp (YYYY-MM-DD HH:MM:SS)
            ts_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
            if ts_match:
                timestamps.append(ts_match.group())

    return {
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count,
        "unique_errors": list(unique_errors),
        "log_start": timestamps[0] if timestamps else None,
        "log_end": timestamps[-1] if timestamps else None
    }


if __name__ == "__main__":
    print(analyze_logs("sample_logs.txt"))
