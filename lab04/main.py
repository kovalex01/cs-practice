from collections import defaultdict
from stats import parse_record, average_by_city, warmest_city, read_valid
import sys
lines = sys.stdin.read().splitlines()

records = read_valid(lines)


total_non_empty = sum(1 for line in lines if line.strip())
skipped = total_non_empty - len(records)

averages = average_by_city(records)
warmest = warmest_city(records)

print(len(records))
print(skipped)

if warmest:
    print(averages[warmest])
