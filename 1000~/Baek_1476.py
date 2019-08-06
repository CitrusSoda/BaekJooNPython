earth, sun, moon = map(int, input().split())
year = 1
x = 1
y = 1
z = 1
while True:
    if earth == x and sun == y and moon == z:
        break

    year += 1
    x = x % 15 + 1
    y = y % 28 + 1
    z = z % 19 + 1

print(year)

