def cal(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return cal(n - 3) + cal(n - 2) + cal(n - 1)


test = int(input())

for i in range(test):
    inp = int(input())
    print(cal(inp))
