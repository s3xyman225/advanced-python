num1 = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
num2 = float(input("Second number: "))

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2 if num2 != 0 else "Error: Division by zero!"
else:
    result = "Invalid operation"

print(f"{num1} {op} {num2} = {result}")