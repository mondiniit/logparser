import re
from datetime import datetime


def get_iso_datetime() :
    return datetime.now().isoformat()


def replace_file_times(log_file_path):
    pattern = re.compile(r'(UTC\s[A-Z][a-z]*\s[0-9]*\s[0-9]*:[0-9]*:[0-9]*)')
    current_time = get_iso_datetime()
    with open(log_file_path, 'r') as f:
        file_lines = f.readlines()
        f.seek(0)
        out = f.read()
        # print(tempFile.read())
        for line in file_lines:
            matches = re.findall(pattern, line)
            for match in matches:
                out = out.replace(match, current_time)
    with open(log_file_path, 'w') as f:
        f.write(out)
    return out


def main():
    log_file_path = "out.txt"
    print(replace_file_times(log_file_path))


if __name__ == '__main__':
    main()
