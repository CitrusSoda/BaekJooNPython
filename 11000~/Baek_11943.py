x, y = map(int, input().split())
a, b = map(int, input().split())

if x + b < a + y:
    print(x + b)
else:
    print(a + y)