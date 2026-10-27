from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
with open("events.log", encoding="utf-8") as log:
    lines = list(log)

counts = count_levels(lines)

print(sum(
    count for level, count in counts.items()
    if level != "BROKEN"
))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

errors = top_errors(lines, 5)
report = format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)
