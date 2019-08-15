case = int(input())

for i in range(case):
    read = input().split()

    for j in range(len(read[1])):
        print(read[1][j] * int(read[0]), end='')
    print()