import sys

num, less_num = map(int, sys.stdin.readline().split())
num_array = list(map(int, sys.stdin.readline().split()))
for i in range(num):
    if num_array[i] < less_num:
        print(num_array[i], end=' ')