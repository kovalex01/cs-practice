from logstats import parse_event, count_levels, format_report, top_errors



path = input().strip()

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)

with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 5)



error_count = counts.get("ERROR", 0)
broken_count = counts.get("BROKEN", 0)

total = sum(
    count
    for level, count in counts.items()
    if level != "BROKEN"
)
print(total)
print(error_count)
print(broken_count)


with open("report.txt", "w", encoding="utf-8") as report:
    report.write(format_report(counts, errors))