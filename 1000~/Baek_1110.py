x = int(input())
cal = x
i = 0
while True:
    div_sum = (cal % 10) + (cal // 10)
    cal = (cal % 10) * 10 + div_sum % 10
    i += 1
    if cal == x:
        print(i)
        break