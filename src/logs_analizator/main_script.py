import sys
from pathlib import Path
from src.logs_analizator.analizator import (
    load_logs,
    count_logs_by_level,
    display_log_counts,
    filter_logs_by_level,
)
from src.logs_analizator.verifier import level_exist, is_valid

"""
The log analyzer script:
    - Reads and analyzes a log file provided as the first
      command-line argument.
    - Displays statistics of log entries grouped by log level
      (INFO, DEBUG, ERROR, WARNING).
    - If the optional second argument is provided, prints
      detailed log entries of that level.
    - Handles common file-related errors and invalid
      log levels.
"""


def main():
    if len(sys.argv) < 2:
        print("Error: Please provide log file path as the "
              "first argument.")
        print("Usage: python main.py <log_file> [log_level]")
        return

    if len(sys.argv) > 3:
        print("Warning: Only first two arguments will be used "
              "(path and log level).")

    log_file = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) >= 3 else None

    path = Path(log_file).expanduser().resolve()
    if not is_valid(path):
        return
    logs = load_logs(str(path))

    if not logs:
        print("problem with the file")
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        if not level_exist(level):
            return
        lvl = level.upper()
        subset = filter_logs_by_level(logs, lvl)
        print(f"\nДеталі логів для рівня {lvl}:")
        if not subset:
            print("(немає записів)")
            return

        for r in subset:
            print(f"{r['date']} {r['time']} {r['level']} {r['text']}")


if __name__ == '__main__':
    main()
