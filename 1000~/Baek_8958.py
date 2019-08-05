case = int(input())

for i in range(case):
    ox = list(input())

    count = 0
    num = 1
    for j in range(len(ox)):
        if ox[j] == "O":
            count += num
            num += 1
        else:
            num = 1
    print(count)