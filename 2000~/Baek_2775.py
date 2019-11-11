testcase = int(input())

for _ in range(testcase):
    floor = int(input())
    room = int(input())

    num = [i for i in range(1, room + 1)]

    for _ in range(floor):
        for j in range(1, room):
            num[j] += num[j-1]
    print(num[-1])