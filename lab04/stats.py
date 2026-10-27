from collections import defaultdict
def parse_record(line: str) -> dict:
    try:
        city, temperature, date = line.strip().split(";")

        city = city.strip()
        temperature = temperature.strip().replace(",", ".")
        date = date.strip()

        if not city or not date:
            return None

        return {
            "city": city,
            "temperature": float(temperature),
            "date": date
        }

    except (ValueError, TypeError):
        return None

def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        record = parse_record(line)

        if record is not None:
            records.append(record)

    return records


def average_by_city(records: list[dict]) -> dict:
    temperatures = defaultdict(list)

    for record in records:
        temperatures[record["city"]].append(record["temperature"])

    return {
        city: round(sum(values) / len(values), 1)
        for city, values in temperatures.items()
    }


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)

    if not averages:
        return ""

    return min(averages, key=lambda city: (-averages[city], city))





