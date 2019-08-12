#count ( < 100 )
def less_hundred(n):
    count = 0
    for i in range(n):
        count += 1
    print(count)
#count ( >= 100 and < 1000)
def more_hundred(n):
    count = 99
    for i in range(100, n + 1):
        num = str(i)
        list_n = list(map(int, num))
        if (list_n[0] - list_n[1]) == (list_n[1] - list_n[2]):
            count += 1
    print(count)
#main
n = int(input())

if n < 100:
    less_hundred(n)
elif n == 1000:
    print(144)
else:
    more_hundred(n)
