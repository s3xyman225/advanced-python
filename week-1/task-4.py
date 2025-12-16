# Task 4: Sum from 1 to N
N = int(input())
if N > 0:
    total = sum(range(1, N + 1))
else:
    total = sum(range(N, 2))  # For negative N
print(total)