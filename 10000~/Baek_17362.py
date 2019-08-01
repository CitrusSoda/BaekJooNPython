import sys

num = int(sys.stdin.readline())

if num % 8 == 1:
    print("1")
elif num % 8 == 2 or num % 8 == 0:
    print("2")
elif num % 8 == 3 or num % 8 == 7:
    print("3")
elif num % 8 == 4 or num % 8 == 6:
    print("4")
else:
    print("5")