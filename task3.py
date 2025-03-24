import sys
import os
from typing import Callable
from collections import Counter

def read_log_file(file_path): # define function for reading log file
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    log_entries = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    log_entries.append(log_entry)
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    return log_entries

def parse_log_line(line): # define function for parsing log
    parts = line.split()
    if len(parts) < 4:
        print(f"Warning: Invalid log line format: {line}")
        return None
    try:
        date = parts[0]
        time = parts[1]
        level = parts[2]
        message = " ".join(parts[3:])
        return {
            "Date": date,
            "Time": time,
            "Level": level,
            "Message": message,
        }
    except Exception as e:
        print(f"Error parsing log line: {line}, error: {e}")
        return None

def filter_by_level(log_data, level): # define function for filtering log
    if not isinstance(log_data, list) or not all(isinstance(entry, dict) for entry in log_data):
        print("Error: Invalid log data format.")
        return []
    if not isinstance(level, str):
        print("Error: Invalid level format. Level must be a string.")
        return []
    filtered_logs = [entry for entry in log_data if entry.get("Level") == level.upper()]
    return filtered_logs

def count_logs_by_level(log_data): # define function for counting log
    if not isinstance(log_data, list) or not all(isinstance(entry, dict) for entry in log_data):
        print("Error: Invalid log data format.")
        return {}
    if not log_data:
        return {}
    levels = [entry.get("Level") for entry in log_data if entry.get("Level")]
    level_counts = Counter(levels)
    return dict(level_counts)

def format_log_counts(level_counts): # define function for formatting log    
    if not isinstance(level_counts, dict):
        print("Error: Invalid input format for format_log_counts. Expected a dictionary.")
        return ""
    if not level_counts:
        return "No log entries found."
    max_level_length = max(len(level) for level in level_counts)
    header = f"{'Level':<{max_level_length}} | Count"
    separator = "-" * (max_level_length + 1) + "-+-------"
    formatted_output = [header, separator]
    for level, count in level_counts.items():
        formatted_output.append(f"{level:<{max_level_length}} | {count}")
    return "\n".join(formatted_output)

def main(USER_PATH): # define main function
    log_data = read_log_file(USER_PATH)
    log_data_INFO = filter_by_level(log_data, "INFO")
    count_level_log = count_logs_by_level(log_data) 
    if log_data:        
        level_counts = count_logs_by_level(log_data)        
        formatted_counts = format_log_counts(level_counts)
        print(formatted_counts)

if __name__ == "__main__": 
    USER_PATH = sys.argv[1] # Get user path    
    main(USER_PATH) # Call main function