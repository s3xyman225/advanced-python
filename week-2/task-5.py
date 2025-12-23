import re

pattern = re.compile(r'^[ABCEHKMOPTXY][0-9]{3}[ABCEHKMOPTXY]{2}$')

n = int(input())
for _ in range(n):
    plate = input().strip()
    print("Yes" if pattern.match(plate) else "No")
