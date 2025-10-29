from collections import Counter


def parse_log_line(line: str) -> dict:
    line = line.strip()
    if not line:
        return {}
    keys = ['date', 'time', 'level', 'text']
    values = line.split(None, 3)
    if len(values) < 4:
        return {}
    return dict(zip(keys, values))


def load_logs(file_path: str) -> list[dict]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                rec = parse_log_line(line)
                if rec:
                    logs.append(rec)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print(f"Error: Permission denied: {file_path}")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file (encoding issue): {file_path}")
    return logs


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    result = [log for log in logs if log.get('level') == level.upper()]
    return result


def count_logs_by_level(logs: list[dict]) -> dict:
    levels = [log.get("level") for log in logs if "level" in log]
    return dict(Counter(levels))


def display_log_counts(counts: dict):
    level = 'Рівень логування'
    count = 'Кількість'
    print(f"{level:<{len(level)}} {'|':<1} {count:<{len(count)}}")
    print("-" * 29)
    for key, value in counts.items():
        print(f"{key:<{len(level)}} {'|':<1} {value:<{len(count)}}")
