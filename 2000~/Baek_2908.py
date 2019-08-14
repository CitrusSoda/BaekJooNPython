num = map(int, input().split())

list_num = list(num)
reverse_num1 = str(list_num[0])[::-1]
reverse_num2 = str(list_num[1])[::-1]

if reverse_num1 < reverse_num2:
    print(reverse_num2)
else:
    print(reverse_num1)