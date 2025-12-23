a = input().strip()
b = input().strip()

count = 0
bb = b + b
m = len(b)

for i in range(len(a) - m + 1):
    if a[i:i+m] in bb:
        count += 1

print(count)
