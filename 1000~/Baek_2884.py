h, m = map(int, input().split())

cal = (h * 60 + m) - 45

new_h = cal // 60
new_m = cal % 60

if new_h == -1:
    new_h = 23

print(new_h, new_m)