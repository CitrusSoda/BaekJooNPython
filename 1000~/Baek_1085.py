x, y, w, h = map(int, input().split())
x_short = 0
y_short = 0

if x > (w - x):
    x_short = (w - x)
else:
    x_short = x

if y > (h - y):
    y_short = (h - y)
else:
    y_short = y

if x_short > y_short:
    print(y_short)
else:
    print(x_short)