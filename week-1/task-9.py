# Task 9: Lucky ticket
ticket = input().strip()
if len(ticket) != 6:
    print("NO")
else:
    first_sum = sum(int(d) for d in ticket[:3])
    last_sum = sum(int(d) for d in ticket[3:])
    print("YES" if first_sum == last_sum else "NO")