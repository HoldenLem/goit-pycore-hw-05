VALID_EXTENSIONS = {'.txt', '.log'}
VALID_LEVELS = {'INFO', 'DEBUG', 'ERROR', 'WARNING'}


def is_valid(path) -> bool:
    if not path.exists():
        print("File does not exist.")
        return False

    if not path.is_file():
        print("Path is not a file.")
        return False

    if path.suffix.lower() not in VALID_EXTENSIONS:
        print("File should have .txt or .log extension.")
        return False

    return True


def level_exist(level: str):
    if level.upper().strip() in VALID_LEVELS:
        return True
    print('second argument should be in: info, debug, error, warning')
    return False
