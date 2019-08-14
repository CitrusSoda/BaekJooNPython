def hanoi(n, from_pole, temp_pole, to_pole):
    if n == 1:
        print(from_pole, to_pole)
    else:
        hanoi(n - 1, from_pole, to_pole, temp_pole)
        print(from_pole, to_pole)
        hanoi(n - 1, temp_pole, from_pole, to_pole)

case = int(input())

count = 0
for i in range(case):
    count = count * 2
    count += 1

print(count)
hanoi(case, 1, 2, 3)