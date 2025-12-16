# Task 3: Swap integer and fractional parts
A = float(input())  # e.g., 123.45
integer_part = int(A)
fractional_part = int(round((A - integer_part) * 100))

new_number = fractional_part + integer_part / 100
print(f"{new_number:.2f}")