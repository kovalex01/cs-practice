ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Негодная строка")

    timestamp, level, message = parts

    if level not in ALLOWED_LEVELS:
        raise ValueError("Неизвестный уровень")

    if not message:
        raise ValueError("Пустое сообщение")

    return {
        "time": timestamp,
        "level": level,
        "message": message
    }


def count_levels(lines: list[str]) -> dict:
    counts = {
        "DEBUG": 0,
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "BROKEN": 0
    }

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1

    return counts


def top_errors(lines: list[str], n: int) -> list[list]:
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)

            if event["level"] == "ERROR":
                message = event["message"]
                errors[message] = errors.get(message, 0) + 1

        except ValueError:
            continue

    result = [[message, count] for message, count in errors.items()]

    result.sort(key=lambda x: (-x[1], x[0]))

    return result[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = []

    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "BROKEN"]:
        lines.append(f"{level}: {counts[level]}")

    lines.append("")
    lines.append("TOP ERRORS:")

    for message, count in errors:
        lines.append(f"{message}: {count}")

    return "\n".join(lines)