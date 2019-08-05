import sys

case = int(sys.stdin.readline())
for i in range(case):
    x, y = map(int, sys.stdin.readline().split())
    sum = x + y
    print(sum)