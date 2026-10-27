from logstats import count_levels, format_report, top_errors, parse_event
ALLOWED_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
path = input().strip()

with open(path, encoding="utf-8") as log:
    lines = list(log)

counts = count_levels(lines)
errors = top_errors(lines, 5)

report = format_report(counts, errors)

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print(counts["DEBUG"] + counts["INFO"] + counts["WARNING"] + counts["ERROR"])
print(counts["ERROR"])
print(counts["BROKEN"])
