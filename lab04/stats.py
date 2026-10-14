def parse_record(line: str) -> dict | None:
    p=line.strip().split(';')
    if len(p)!=3:
        return None
    dic = {
        "city": p[0],
        "temp": p[1],
        "date": p[2]
    }
    return dic
#def read_valid(lines: list[str]) -> list[dict]:
 #   for x in lines:





