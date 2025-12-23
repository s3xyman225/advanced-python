items = input().split()

freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Purchase frequency:")
for k, v in freq.items():
    print(f"{k}: {v}")

max_item = max(freq, key=freq.get)
print("Most popular item:", max_item)

once = [k for k, v in freq.items() if v == 1]
print("Purchased once:", " ".join(once))

print("Sorted by frequency:")
for k, v in sorted(freq.items(), key=lambda x: -x[1]):
    print(k, v)
