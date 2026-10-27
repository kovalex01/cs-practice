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
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

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
    result.sort(key=lambda item: (-item[1], item[0]))

    return result[:n]


def format_report(counts: dict, errors: list[list]) -> str:
    lines = ["Отчёт по журналу", ""]

    for level, count in counts.items():
        if level != "BROKEN":
            lines.append(f"{level}: {count}")

    lines.append("")
    lines.append("Частые ошибки:")

    for message, count in errors:
        lines.append(f"- {message} — {count}")

    return "\n".join(lines) + "\n"