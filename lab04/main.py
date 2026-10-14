from stats import parse_record
import sys
#lines = sys.stdin.read().splitlines()
lines = ["Азов;24.5;2026-07-01","Азов;25.5;2026-07-02 ","trash","Таганрог;30;2026-07-01"]
#lines = sys.stdin.read().splitlines()
c=0
gen=[]
for x in lines:
    gen.append(parse_record(x))
for x in gen:


print(c)




