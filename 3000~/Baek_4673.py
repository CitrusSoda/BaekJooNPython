def f_num(a):
    #자릿수 덧셈
    sum = a
    while a != 0:
        x = a % 10
        sum += x
        a = a // 10

    return sum
#f_num 배열 생성
b = []
for i in range(10000):
    b.append(f_num(i + 1))
#f_num에 있으면 패스 아니면 출력
for i in range(10000):
    if (i + 1) in b:
        pass
    else:
        print(i + 1)






