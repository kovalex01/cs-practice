from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

print(sum(
    count for level, count in counts.items()
    if level != "BROKEN"
))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))


