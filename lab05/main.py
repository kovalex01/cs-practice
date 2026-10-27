from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

import os

path = input().strip()

if not path:
    print("Ошибка: имя файла не введено")
elif not os.path.isfile(path):
    print(f"Ошибка: файл не найден: {path}")
else:
    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)

    print(sum(
        count for level, count in counts.items()
        if level != "BROKEN"
    ))
    print(counts.get("ERROR", 0))
    print(counts.get("BROKEN", 0))


