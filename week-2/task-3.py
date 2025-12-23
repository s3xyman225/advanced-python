eq = input().strip()

if eq[0] == 'x':
    a = int(eq[2])
    b = int(eq[4])
    if eq[1] == '+':
        print(b - a)
    else:
        print(b + a)

elif eq[2] == 'x':
    a = int(eq[0])
    b = int(eq[4])
    if eq[1] == '+':
        print(b - a)
    else:
        print(a - b)

else:
    a = int(eq[0])
    b = int(eq[2])
    if eq[1] == '+':
        print(a + b)
    else:
        print(a - b)
