from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}


def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError

    time, level, message = parts

    if level not in LEVELS:
        raise ValueError

    return {
        "time": time,
        "level": level,
        "message": message
    }


def count_levels(lines: list[str]) -> dict:
    counts = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            continue

        level = event["level"]
        counts[level] = counts.get(level, 0) + 1

    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
        except ValueError:
            continue

        if event["level"] == "ERROR":
            message = event["message"]
            errors[message] = errors.get(message, 0) + 1

    result = [[message, count] for message, count in errors.items()]
    result.sort(key=lambda x: (-x[1], x[0]))

    return result[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    result = ["Отчёт по журналу", ""]

    for level, count in counts.items():
        if level != "BROKEN":
            result.append(f"{level}: {count}")

    result += ["", "Частые ошибки:"]

    for message, count in errors:
        result.append(f"- {message} — {count}")

    return "\n".join(result) + "\n"



path = input()

with open(path.strip(), encoding="utf-8") as log:
    counts = count_levels(log)


    with open(path.strip(), encoding="utf-8") as log2:
        errors = top_errors(log2, 5)

print(sum(
    count for level, count in counts.items()
    if level != "BROKEN"
))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as report:
    report.write(format_report(counts, errors))


