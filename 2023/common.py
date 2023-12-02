def read_file_to_list(file_path: str) -> list[str]:
    lines_raw = open(file_path).readlines()
    lines_sanitized = [line.strip() for line in lines_raw]
    return lines_sanitized
