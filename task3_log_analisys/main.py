def parse_log_line(line: str) -> dict # для парсингу рядків логу.
def функцію load_logs(file_path: str) -> list # для завантаження логів з файлу.
def функцію filter_logs_by_level(logs: list, level: str) -> list # для фільтрації логів за рівнем.
def функцію count_logs_by_level(logs: list) -> dict # для підрахунку записів за рівнем логування.


python [main.py](<http://main.py/>) /path/to/logfile.log