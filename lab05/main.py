from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
path = input().strip()

with open(path, encoding="utf-8") as log:
    lines = list(log)

counts = count_levels(lines)
errors = top_errors(lines, 5)

print(sum(
    count for level, count in counts.items()
    if level != "BROKEN"
))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

with open("report.txt", "w", encoding="utf-8") as report_file:
    report_file.write(format_report(counts, errors))
