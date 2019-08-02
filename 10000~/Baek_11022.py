import sys

num = int(sys.stdin.readline())
for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    sum = x + y
    print("Case #", i + 1,": ", x, " + ", y, " = ", sum, sep='')